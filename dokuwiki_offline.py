import sys
import os
import logging
import re
from urllib.parse import urlparse
from urllib import request
from ssl import _create_unverified_context
from datetime import datetime
import json

from dokuwiki import DokuWiki, DokuWikiError, date
import click

# set logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)-8s : %(message)s',
                    datefmt='%m-%d %H:%M',
                    )
logger = logging.getLogger('wiki')


def validate_url(ctx, param, url: str):
    """
    Validate URL and schema.

    :param ctx: click context
    :param param: parameter name
    :param url: parameter value
    :return: value
    """
    try:
        parsed_url = urlparse(url)
        if all([parsed_url.scheme, parsed_url.netloc]):
            if parsed_url.scheme in ["https", "http"]:
                return url
        raise click.BadParameter('Not a valid URL')
    except (ValueError, Exception):
        raise click.BadParameter('Not a valid URL')


@click.command()
@click.option(
    '--url',
    prompt='URL to a Dokuwiki',
    callback=validate_url,
    help='URL to a Dokuwiki i.e. https://mywiki.example'
)
@click.option('--username', prompt=True, help="Login username")
@click.option('--password', prompt=True, help="Login password")
@click.option('--skipcert', is_flag=True, default=False, help="Skip https certificate checks")
def dump(url: str, username: str, password: str, skipcert: bool) -> None:
    """
    A tool to download and store all pages and media files from Dokuwikis through the xmlrpl api.

    \f
    :param url: Dokuwiki URL
    :param username: Login username
    :param password: Login password
    :param skipcert: Skip certificate checks
    :return: None
    """
    dump_folder = os.path.join("dumps", urlparse(url).hostname)

    try:
        if skipcert:
            wiki = DokuWiki(url, username, password, context=_create_unverified_context())
        else:
            wiki = DokuWiki(url, username, password)
        pages = wiki.pages
    except (DokuWikiError, Exception) as err:
        logger.error("Connection error: {}".format(err))
        sys.exit(-1)

    # Load html template
    with open("template.tpl") as template_file:
        template = template_file.read()

    # Load JSON file with file versions
    try:
        versions = json.load(open(os.path.join(dump_folder, "versions.json")))
    except FileNotFoundError:
        versions = {"pages": {}, "medias": {}}

    for page in pages.list():

        page_version = str(date(pages.info(page['id'])['lastModified']))

        if not versions['pages'].get(page['id'], "") == page_version:

            filename = "{}/{}.html".format(dump_folder, str(page['id']).replace(":", "/"))
            os.makedirs(os.path.dirname(filename), exist_ok=True)

            root_path = ""
            # traverse down to root
            for fdown in range(0, filename.count("/") - 1):
                root_path = "../{}".format(root_path)

            with open(filename, "w", encoding='utf-8') as file:
                logger.info("Updating {}".format(page['id']))

                html = pages.html(page['id'])

                # find all local links and convert them to relative file links
                for url_match in re.finditer(r"<a[\s]+(?:[^>]*?\s+)?href=([\"'])(/.*?)\1", html, re.MULTILINE):
                    new_url = urlparse(url_match.group(2)[1:].replace(":", "/")).path + ".html"

                    if "_media" in new_url:  # fix media download urls
                        new_url = new_url.replace("_media/", "")
                        new_url = new_url.replace(".html", "")
                    new_url = root_path + new_url  # fix absolute paths with relative urls
                    html = html.replace(url_match.group(2), new_url)

                # fix img paths
                for img_match in re.finditer(r"<img\s+(?:[^>]*?\s+)?src=([\"'])(/.*?)\1", html, re.MULTILINE):
                    new_url = urlparse(img_match.group(2)[1:].replace(":", "/")).path
                    new_url = new_url.replace("_media/", "")
                    new_url = root_path + new_url
                    html = html.replace(img_match.group(2), new_url)

                # replace template tags with values
                html = template.replace("{{body_content}}", html)  # process template
                html = html.replace("{{root_link}}", root_path)  # replace rootpaths
                html = html.replace("{{page_title}}", page['id'].split(":")[-1].capitalize())  # replace page title
                html = html.replace("{{path}}", page['id'].capitalize())  # replace page id
                html = html.replace("{{wiki_title}}", wiki.title)
                html = html.replace("{{download_date}}", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                html = html.replace("{{last_modified}}", str(date(pages.info(page['id'])['lastModified'])))

                file.write(html)

                versions['pages'][page['id']] = page_version
        else:
            logger.info("No update needed for page {}".format(page['id']))

    # Loop all media files
    for media in wiki.medias.list():

        media_version = str(date(wiki.medias.info(media['id'])['lastModified']))

        if not versions['medias'].get(media['id'], "") == media_version:

            logger.info("Updating media {}".format(media['id']))

            # print(wiki.medias.info(media['id']))

            filename = "{}/{}".format(dump_folder, str(media['id']).replace(":", "/"))
            os.makedirs(os.path.dirname(filename), exist_ok=True)

            # Write media to file
            wiki.medias.get(media['id'], dirpath=os.path.dirname(filename), overwrite=True)

            versions['medias'][media['id']] = media_version

        else:
            logger.info("No update needed for media {}".format(media['id']))

    # Download stylesheet
    try:
        if skipcert:
            data = request.urlopen("{}/lib/exe/css.php".format(url), context=_create_unverified_context()).read()
        else:
            data = request.urlopen("{}/lib/exe/css.php".format(url)).read()

        with open("{}/style.css".format(dump_folder), "wb") as stylesheet:
            stylesheet.write(data)
    except Exception as err:
        logger.error("Stylesheet download error: {}".format(err))

    # Save versions to json file
    json.dump(versions, open(os.path.join(dump_folder, "versions.json"), "w"), indent=4)


if __name__ == "__main__":
    dump()

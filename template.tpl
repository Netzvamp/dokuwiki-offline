<!DOCTYPE html>
<html>
<head>
    <title>{{page_title}} [{{wiki_title}}]</title>
    <meta name="viewport" content="width=device-width,initial-scale=1"/>
    <link rel="stylesheet" type="text/css" href="{{root_link}}style.css"/>
</head>
<body>
<div id="dokuwiki__site">
    <div id="dokuwiki__top" class="site dokuwiki mode_show tpl_dokuwiki loggedIn  home  ">
        <div id="dokuwiki__header">
            <div class="headings group">
                <h1><a href="{{root_link}}start.html"><img src="{{root_link}}wiki/dokuwiki-128.png" width="64"
                                                           height="64" alt=""><span>{{wiki_title}}</span></a></h1>
            </div>
            <div class="breadcrumbs">
                <div class="youarehere"><span class="home">{{path}}</span></div>
            </div>

        </div>
        <div class="wrapper group">
            <div id="dokuwiki__content">
                <div class="page group">
                    {{body_content}}
                </div>
            </div>
        </div>
        <div id="dokuwiki__footer">
            <div class="pad">
                Download: {{download_date}} - Last modified: {{last_modified}} - Created with <a
                    href="https://github.com/Netzvamp/dokuwiki_offline" target="_blank">dokuwiki_offline</a>
            </div>
        </div>
    </div>
</div>
<script type="text/javascript" charset="utf-8" src="{{root_link}}jquery.js"></script>
<script type="text/javascript" charset="utf-8" src="{{root_link}}javascript.js"></script>
<script type="text/javascript">/*<![CDATA[*/
    DOKU_BASE='{{root_link}}';
    JSINFO = {};
/*!]]>*/</script>
</body>
</html>
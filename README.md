# Dokuwiki offline
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![Open Source Love svg2](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/) [![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0.html)

A tool to download and store all pages and media files from Dokuwiki through the XML-RPC API, possible thanks to the excellent python dokuwiki package (https://pypi.org/project/dokuwiki/)!

## Precompiled binarys
[Download Releases](https://github.com/Netzvamp/dokuwiki_offline/releases)

## Usage

    dokuwiki_offline [OPTIONS]
    
    Options:
      --url TEXT       URL to a Dokuwiki i.e. https://mywiki.example
      --username TEXT  Login username
      --password TEXT  Login password
      --skipcert       Skip https certificate checks
      --force          Skip local versioncheck and force download
      --help           Show this message and exit.

    Example:
    
    dokuwiki_offline --url https://mywiki.example --username Testuser --password mypassword123 --skipcert
    
    This will create a dump folder with a domain name subfolder with all html.

## Development / Build

### Preparation
    
Developed with Python 3.7, but should also work with Python 3.5.
    
    # Prepare a venv in the current directory and install the requirements with
    pip install -r requirements.txt

### Build a binary package/ Executable with PyInstaller

    # Install pyinstaller
    pip install pyinstaller
    
    # Build a binary with the spec file
    pyinstaller dokuwiki_offline.spec
    
PyInstaller creates a 'dist/dokuwiki_offline' folder, that can be moved, 
copied and distributed.

## History

* 1.0: 2018-12-12
    * Added force parameter to ignore versions and just overwrite
    * Include JS scripts
    * Exclude /_export/... urls
    
* 1.0-r1: 2018-12-05
    * Only download new and updated files. File modification dates are stored in json file in the dump 
    * Added the wiki title, download and last modification date to the template file
    * Extended URL validation
    * Documentation fixes
    
* 1.0-beta1: 2018-12-03
    * Initial release
    
## Todo

- [ ] Output folder as paramter

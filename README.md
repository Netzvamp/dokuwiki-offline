# Dokuwiki offline

A tool to download and store all pages and media files from Dokuwikis through the xmlrpl api.

## Preparation
    
    # Prepare a venv in the current directory and install the requirements
    pip install -r requirements.txt

## Usage

    python dokuwiki_offline.py [OPTIONS]
    
    Options:
      --url TEXT       URL to a Dokuwiki
      --username TEXT  Login username
      --password TEXT  Login password
      --skipcert       Skip https certificate checks
      --help           Show this message and exit.

Tested with Python 3.7.

## Build a binary package/ Executable with PyInstaller

    # Install pyinstaller
    pip install pyinstaller
    
    # Build a binary with the spec file
    pyinstaller dokuwiki_offline.spec
    
PyInstaller creates a 'dist/dokuwiki_offline' folder, that can be moved, 
copied and distributed.
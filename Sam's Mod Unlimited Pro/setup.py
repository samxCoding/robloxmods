from setuptools import setup

APP=['ModLoaderScript.py']
OPTIONS = {
        'argv_emulation': True,
}

(
    app=APP
    options={'py2app': OPTIONS},
    setup_require=['py2app']
)
# This error can't be fixed. If you fixed this error you will lose security.py
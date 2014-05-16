"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['GitSyncApp.py']
DATA_FILES = [
    'MenuIcon.png',
    'GitSyncIcon.icns',
]
OPTIONS = {
    'argv_emulation': True,
    'packages': [
        'rumps',
        'fabric',
        'gitsync',
        #'fsevents',
        'yaml',
    ],
    'plist': {
        'LSUIElement': True,
    },
    'iconfile': 'GitSyncIcon.icns',
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    include_package_data=True,
    setup_requires=[
        'py2app'
    ],
)

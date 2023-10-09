#!/usr/bin/python3
'''
    Fabric script (based on the file 3-deploy_web_static.py)
    that deletes out-of-date archives, using the function do_clean
'''

from datetime import datetime
from fabric.api import *
from os import *

env.hosts = ["54.160.103.40", "52.91.148.127"]


def do_clean(number=0):
    """Deletes out-of-date archives of the static files.
    """
    archives = listdir('versions/')
    archives.sort(reverse=True)
    start = int(number)
    if not start:
        start += 1
    if start < len(archives):
        archives = archives[start:]
    else:
        archives = []
    for archive in archives:
        unlink('versions/{}'.format(archive))
    command = "rm -rf $("
    command += "find /data/web_static/releases/ -maxdepth 1 -type d -iregex"
    command += " '/data/web_static/releases/web_static_.*' "
    command += "| sort -r | tr '\\n' ' ' | cut -d ' ' -f{}-)".format(start + 1)
    run(command)

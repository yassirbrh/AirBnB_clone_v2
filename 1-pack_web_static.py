#!/usr/bin/python3
'''
    Fabric script that generates a .tgz archive from
    the contents of the web_static folder
'''
from datetime import datetime
from fabric.api import local
from os import path


def do_pack():
    """ Create a .tgz archive from the contents of web_static. """
    dt = datetime.utcnow()
    year = dt.year
    month = dt.month
    day = dt.day
    hour = dt.hour
    minute = dt.minute
    second = dt.second
    file = "versions/web_static_"
    file += "{}{}{}{}{}{}.tgz".format(year, month, day, hour, minute, second)
    if path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file

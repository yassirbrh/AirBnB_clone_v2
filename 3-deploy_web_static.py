#!/usr/bin/python3
'''
    Fabric script (based on the file 2-do_deploy_web_static.py) that creates
    and distributes an archive to your web servers, using the function deploy
'''

from datetime import datetime
from fabric.api import *
from os import path

env.hosts = ["54.160.103.40", "52.91.148.127"]


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


def do_deploy(archive_path):
    """ Distributes the archive to the web servers. """
    if path.exists(archive_path):
        path_parts = archive_path.split('/')
        archive = path_parts[-1].split('.')[0]
        if put(archive_path, "/tmp/{}".format(path_parts[-1])).failed is True:
            return False

        command = "mkdir -p /data/web_static/releases/{}/".format(archive)
        if run(command).failed is True:
            return False

        command = "tar -xzf /tmp/{} -C ".format(path_parts[-1])
        command += "/data/web_static/releases/{}/".format(archive)
        if run(command).failed is True:
            return False

        command = "rm /tmp/{}".format(path_parts[-1])
        if run(command).failed is True:
            return False

        command = "mv /data/web_static/releases/{}/web_static/".format(archive)
        command += "* /data/web_static/releases/{}/".format(archive)
        if run(command).failed is True:
            return False

        command = "rm -rf /data/web_static/releases/{}/".format(archive)
        command += "web_static/"
        if run(command).failed is True:
            return False

        if run("rm -rf /data/web_static/current").failed is True:
            return False

        command = "ln -s /data/web_static/releases/{}/ ".format(archive)
        command += "/data/web_static/current"
        if run(command).failed is True:
            return False

        print("New version deployed!")
        return True

def deploy():
    """ Creates and distributes an archive to your web servers """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)

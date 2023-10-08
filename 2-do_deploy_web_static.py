#!/usr/bin/python3
'''
    Fabric script that generates a .tgz archive from
    the contents of the web_static folder and
    distributes an archive to your web servers, using the function do_deploy
'''
from fabric.api import *
from os import path

env.user = "ubuntu"
env.hosts = ["54.160.103.40", "52.91.148.127"]


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

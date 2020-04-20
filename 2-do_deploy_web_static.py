#!/usr/bin/python3
""" Fabric module script that distributes an archive """
from fabric.api import put, run, env
from os import *
import os.path
from datetime import datetime

t = datetime.now()

env.hosts = ['35.237.146.194', '35.243.176.223']
env.user = 'ubuntu'


def do_pack():
    """ Method to generate the .tgz file """
    makedirs('versions', exist_ok=True)
    time = 'versions/web_static_{}{}{}{}{}{}.tgz'\
           .format(t.year, t.month, t.day, t.hour, t.minute, t.second)
    check = local("tar -cvzf " + time + " ./web_static/")
    if check.succeeded:
        return t
    return None


def do_deploy(archive_path):
    """ Method that distributes and archive to web servers """

    if os.path.exists(archive_path) is False:
        return False

    try:
        put(archive_path, "/tmp/")
        filename = os.path.basename(archive_path)
        (file_s, ext) = os.path.splitext(filename)
        run("mkdir -p /data/web_static/releases/{}/".format(file_s))
        run("tar -xzvf /temp/{} -C /data/web_static/releases/{}/".
            format(filename, file_s))
        run("rm -f /tmp/{}".format(filename))
        run("mv /data/web_static/releases/{}/web_static/* {}{}/".
            format(file_s, rel_path, filename))
        run("rm -rf /data/web_static/releases/{}/web_static".format(file_s))
        run("rm -rf /data/web_static/current")
        run("ln -sf /data/web_static/releases/{}/ /data/web_static/current".
            format(file_s))

        return True

    except:
        return False

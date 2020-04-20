#!/usr/bin/python3
"""
Fabric module script that creates and
distributes an archive to web server
"""
from fabric.api import put, run, env,local
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
        return time
    return None


def do_deploy(archive_path):
    """ Method that distributes and archive to web servers """

    if os.path.exists(archive_path):

        put(archive_path, "/tmp/")
        filename = os.path.basename(archive_path)
        (file, ext) = os.path.splitext(filename)
        rel_path = "/data/web_static/releases/"
        run("mkdir -p {}{}/".format(rel_path, file))
        run("tar -xzvf /tmp/{} -C {}{}/".format(filename, rel_path, file))
        run("rm -f /tmp/{}".format(filename))
        run("mv {}{}/web_static/* {}{}/".format(rel_path,
                                                file, rel_path, file))
        run("rm -rf {}{}/web_static".format(rel_path, file))
        run("rm -rf /data/web_static/current")
        run("ln -sf {}{}/ /data/web_static/current".format(rel_path, file))

        return True
    return False

def deploy():
    """ Method that creates and distributes an archive """
    packing = do_pack()
    if packing is False:
        return False

    return do_deploy(packing)

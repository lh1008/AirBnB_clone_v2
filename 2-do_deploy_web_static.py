#!/usr/bin/python3
""" Fabric module script that distributes an archive """
from fabric.api import *
from os import *
from datetime import datetime

t = datetime.now()

env.user = 'ubuntu'
env.hosts = ['35.237.146.194', '35.243.176.223']
# env.user = 'root'
# env.hosts = ['770e6f93930c@19.hbtn-cod.io']
# env.password = '3f8972ab387289f35b7d'


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
    path = archive_path
    put(archive_path, "/tmp/")
    filename = os.path.basename(path)
    (file, ext) = os.path.splitext(filename)
    rel_path = "/data/web_static/releases/"
    run("mkdir -p {}{}/".format(rel_path, file))
    run("tar -xzvf /temp/{} -C {}{}/".format(filename, rel_path, file))
    run("rm -f /tmp/{}".format(filename))
    run("mv {}{}/web_static/* {}{}/".format(rel_path, file, rel_path, filename))
    run("rm -rf {}{}/web_static".format(rel_path, file))
    run("rm -rf /data/web_static/current")
    run("ln -sf {}{}/ /data/web_static/current".format(rel_path, file))

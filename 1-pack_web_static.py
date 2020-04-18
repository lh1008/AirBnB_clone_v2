#!/usr/bin/python3
""" Fabric module script that generates a .tgz archive """
from fabric.api import local
from os import path, makedirs
from datetime import datetime

t = datetime.now()


def do_pack():
    """ Method to generate the .tgz file """
    makedirs('versions', exist_ok=True)
    time = 'versions/web_static_{}{}{}{}{}{}.tgz'\
           .format(t.year, t.month, t.day, t.hour, t.minute, t.second)
    check = local("tar -cvzf " + time + " ./web_static/")
    if check.succeeded:
        return t
    return None

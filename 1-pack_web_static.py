#!/usr/bin/python3
""" Fabric module script that generates a .tgz archive """
from fabric.api import local
from os import path, mkdir
from datetime import datetime

t = datetime.now()


def do_pack():
    """ Method to generate the .tgz file """
    if path.exists('./versions'):
        return None
    else:
        mkdir('versions')
        time = 'versions/web_static_{}{}{}{}{}{}.tgz'\
            .format(t.year, t.month, t.day, t.hour, t.minute, t.second)
        local("tar -cvzf " + time + " ./web_static/")
        if local:
            return t

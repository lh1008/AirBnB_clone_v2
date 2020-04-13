#!/usr/bin/python3
""" Fabfile module """
from fabric.api import *

env.user = 'ubuntu'
env.hosts = ['35.237.146.194', '35.243.176.223']


def up_load():
    put("0-setup_web_static.sh", '/home/ubuntu')

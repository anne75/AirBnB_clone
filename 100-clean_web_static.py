#!/usr/bin/python3
"""
This is module 100-clean_web_static
This module is a fabfile to clean up after deployment
run as fab -f 100-clean_web_static.py do_clean:number=2
-i my_ssh_private_key -u ubuntu > /dev/null 2>&1
"""
from fabric.api import *
from fabric.contrib.files import exists
import os

env.hosts = ['54.204.151.7', '54.90.224.219']


@runs_once
def clean_local(number=0):
    """
    clean local archives directory versions
    Args:
    number: number of archives to keep
    """
    # list all archives
    os.chdir("versions/")
    res = local("ls -1t", capture=True).split("\n")
    if number == 0:
        number += 1
    if len(res) > number:
        for f in res[number:]:
            local("rm -f {}".format(f))


def clean_server(number=0):
    """
    clean previous versions of web_static
    Args:
    number: number of previous versions to keep
    """
    path = "/data/web_static/releases"
    with cd(path):
        res = sudo("ls -1t").split("\r\n")
    res = [f for f in res if "web_static" in f]
    if number == 0:
        number += 1
    if len(res) > number:
        res = res[number:]
        with cd(path):
            for f in res:
                sudo("rm -rf {}".format(f))


def do_clean(number=0):
    """
    remove archive files here and old versions of web_static on the
    servers
    Args:
    number: number of files to keep
    """
    number = int(number)
    clean_local(number)
    clean_server(number)

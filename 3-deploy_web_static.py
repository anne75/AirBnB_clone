#!/usr/bin/python3
"""
This is module 3-deploy_web_static
This module is a fabfile to deploy a static web site from here to 2 servers
Run as
fab -f 3-deploy_web_static.py deploy -i my_ssh_private_key -u ubuntu
"""
# it looks like this is not working, cpy pastinf files instead
# do_pack = __import__('1-pack_web_static').do_pack
# vdo_deploy = __import__('2-do_deploy_web_static').do_deploy
import time
from fabric.api import *
import os.path
import sys


env.hosts = ['54.204.151.7', '54.90.224.219']
archive_path = None


def do_pack():
    """
    function that tars a directory in a dedicated directory
    """
    filename = "web_static_{:s}.tgz".format(time.strftime("%Y%m%d%H%M%S"))
    try:
        local("sudo mkdir -p versions")
        local("sudo tar -cvzf versions/{} web_static/".format(filename))
        return "versions/{}".format(filename)
    except:
        pass


def do_deploy(archive_path):
    """
    checks for a tar file and deploys it
    Args
        archive_path: path to archive
    """
    if not os.path.isfile(archive_path):
        return False

    try:
        # upload file
        put(archive_path, "/tmp")

        # untar and clean
        filename = archive_path.split("/")[-1]
        dirname = "/data/web_static/releases/{}".format(filename.split(".")[0])
        sudo("mkdir -p {}".format(dirname))
        sudo("tar -xzf /tmp/{} -C {}".format(filename, dirname))
        sudo("rm /tmp/{}".format(filename))
        sudo("mv {}/web_static/* {}".format(dirname, dirname))
        sudo("rm -rf {}/web_static".format(dirname))
        sudo("rm -rf /data/web_static/current")
        sudo("ln -s {} /data/web_static/current".format(dirname))
        return True
    except:
        return False


def deploy():
    """
    Combine the 2 previous modules to tar a folder containing a static web
    an upload to servers
    """
    global archive_path
    if archive_path is None:
        archive_path = do_pack()
    if archive_path is None:
        return False

    return do_deploy(archive_path)

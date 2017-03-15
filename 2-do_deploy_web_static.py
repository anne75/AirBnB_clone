#!/usr/bin/python3
"""
This is module 2-do_deploy_web_static
This module is a fabfile to deploy a tar file to 2 servers
run it as
fab -f 2-do_deploy_web_static.py do_deploy:archive_path=<path to tar file>
 -i my_ssh_private_key -u ubuntu
"""
from fabric.api import *
import os.path


env.hosts = ['54.204.151.7', '54.90.224.219']


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
        sudo("mv {}/web_static/* {}".format(dirname))
        sudo("rm -rf {}/web_static".format(dirname))
        sudo("ln -sf {} /data/web_static/current".format(dirname))
        return True
    except:
        return False

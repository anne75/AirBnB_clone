#!/usr/bin/python3
"""
This is module 3-deploy_web_static
This module is a fabfile to deploy a static web site from here to 2 servers
Run as
fab -f 3-deploy_web_static.py deploy -i my_ssh_private_key -u ubuntu
"""
do_pack = __import__('1-pack_web_static').do_pack

do_deploy = __import__('2-do_deploy_web_static').do_deploy

archive_path = None


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

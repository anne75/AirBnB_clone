#!/usr/bin/python3
"""
This is module pack_web_static
This module is a fabfile, run it like fab -f 1-pack_web_static.py do_pack
"""
from fabric.api import local
import time


def do_pack():
    """
    function that tars a directory in a dedicated directory
    """
    filename = "web_static_{:s}.tgz".format(time.strftime("%Y%m%d%H%M%S"))
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/{} web_static/".format(filename))
    except Exception:
        pass

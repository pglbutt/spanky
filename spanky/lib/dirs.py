import pwd
import grp
import os
from subprocess import call


class DirInit(object):

    def __init__(self, yaml_config):
        self.config = yaml_config

    def build(self):
        for directory in self.config:
            try:
                uid = pwd.getpwnam(directory['user']).pw_uid
            except Exception:
                raise Exception('User %s does not exist' % directory['user'])
            
            gid = grp.getgrnam(directory['group']).gr_gid

            os.mkdir(directory['dir'], directory['mode'])
            os.chown(directory['dir'], uid, gid)

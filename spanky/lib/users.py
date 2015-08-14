from subprocess import call


class UserInit(object):

    def __init__(self, yaml_config):
        self.config = yaml_config


    def create_user(self, user_conf):
        cmd = [
            'useradd',
            '-U', # create group with
            user_conf['username']
        ]
        if call(cmd):
            raise Exception()

    def build(self):
        for user in self.config:
            self.create_user(user)

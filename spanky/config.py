"""
Create our config based on $base/etc/spanky

Generally, config files should be YAML or scripts.
"""
import os
import yaml


class Config(object):
    def __init__(self, base='/'):
        self.base = base

    def get(self, path):
        return os.path.join(self.base, path)

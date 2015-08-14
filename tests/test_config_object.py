import os

from spanky.config import Config

HERE = os.path.dirname(os.path.abspath(__file__))


class TestConfigObject(object):

    def setup(self):
        self.config = Config(HERE)

    def test_config_is_like_dict(self):
        assert self.config.get('example')

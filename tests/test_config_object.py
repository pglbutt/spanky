import os

from spanky import config

HERE = os.path.dirname(os.path.abspath(__file__))

class TestYAMLConfig(object):

    def test_load_config_file(self):
        c = config.YAMLConfig(os.path.join(HERE, 'etc', 'spanky', 'example.yml'))
        assert c()[0]['foo'] == 'bar'


class TestConfigObject(object):

    def setup(self):
        self.config = config.Config(os.path.join(HERE, 'etc', 'spanky'))

    def test_load_config_file(self):
        conf = self.config.load('example.yml')
        assert conf[0]['foo'] == 'bar'

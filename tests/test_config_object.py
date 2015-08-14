import os

from spanky import config

HERE = os.path.dirname(os.path.abspath(__file__))

class TestYAMLConfig(object):

    def test_load_config_file(self):
        c = config.YAMLConfig(os.path.join(HERE, 'etc', 'spanky', 'example.yml'))
        assert c()[0]['foo'] == 'bar'


class TestScriptConfig(object):

    def test_load_config_file(self):
        c = config.ScriptConfig(os.path.join(HERE, 'etc', 'spanky', 'script'))
        script = c()
        assert script.run


class TestConfigObject(object):

    def setup(self):
        self.config = config.Config(os.path.join(HERE, 'etc', 'spanky'))

    def test_load_config_file(self):
        conf = self.config.load('script')

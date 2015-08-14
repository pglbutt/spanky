import pytest

from mock import patch, Mock

from spanky.resources import package


class TestPackageResource(object):

    def test_package_install(self):
        pack = package.Package('nginx')
        pack._ok = Mock()
        pack._ok.return_value = 'install ok installed'

        pack.installed = Mock()
        pack.installed.return_value = True

        pack.install()

        expected = [
            'apt-get', 'install', '-y', 'nginx'
        ]
        pack._ok.assert_called_with(expected)

    def test_package_remove(self):
        pack = package.Package('nginx')
        pack._ok = Mock()
        pack._ok.return_value = 'is not installed'

        pack.installed = Mock()
        pack.installed.return_value = False

        pack.remove()

        expected = [
            'apt-get', 'remove', '-y', 'nginx'
        ]
        pack._ok.assert_called_with(expected)

    def test_package_installed(self):
        pack = package.Package('nginx')
        pack._ok = Mock()
        pack._ok.return_value = 'install ok installed'

        assert pack.installed()

        expected = [
            'dpkg', '-s', 'nginx'
        ]
        pack._ok.assert_called_with(expected)

        pack._ok.return_value = 'nginx is not installed'

        assert not pack.installed()

        expected = [
            'dpkg', '-s', 'nginx'
        ]
        pack._ok.assert_called_with(expected)

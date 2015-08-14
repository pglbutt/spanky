import pytest

from mock import patch, Mock

from spanky.lib import users


class TestCreateUsers(object):

    def setup(self):
        self.conf = [
            {'username': 'foo'},
            {'username': 'bar'},
        ]
        self.user_init = users.UserInit(self.conf)

    def test_build(self):
        self.user_init.create_user = Mock()

        self.user_init.build()

        assert len(self.user_init.create_user.mock_calls) == 2

    @patch.object(users, 'call')
    def test_create_users(self, call):
        call.return_value = 0
        self.user_init.create_user({'username': 'foo'})
        assert call.called

    @patch.object(users, 'call')
    def test_create_users_raises_error_on_fail(self, call):
        call.return_value = 1
        assert pytest.raises(Exception, self.user_init.create_user, {'username': 'foo'})

    @patch.object(users, 'call')
    def test_useradd_command(self, call):
        call.return_value = 0

        self.user_init.create_user({
            'username': 'foo',
        })

        expected = [
            'useradd', '-U', 'foo'
        ]
        call.assert_called_with(expected)

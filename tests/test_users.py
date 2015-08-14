from mock import patch

from spanky.lib import users


class TestCreateUsers(object):

    def setup(self):
        self.conf = [
            {'username': 'foo'},
            {'username': 'bar'},
        ]
        self.user_init = users.UserInit(self.conf)

    @patch.object(users, 'call')
    def test_create_users_from_config(self, call):
        self.user_init.build()
        assert call.called

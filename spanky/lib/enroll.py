import redis


class Enroller(object):

    def __init__(self, config):
        self.config = config

    @property
    def conn(self):
        if not hasattr(self, '_conn'):
            self._conn = redis.StrictRedis(host='localhost', port=6379, db=0)
        return self._conn

    def join(self, name, host, port):
        self.conn.lpush(name, '%s:%s' % (host, port))

    def enrolled(self, name):
        return self.conn.lrange(name, 0, -1)


def main():
    e = Enroller({})
    e.join('foo', 'bar', 8080)
    print(e.enrolled('foo'))

if __name__ == '__main__':
    main()

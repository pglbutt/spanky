from contextlib import contextmanager

import redis


class Enroller(object):

    def __init__(self, config):
        self.config = config

    @property
    def conn(self):
        if not hasattr(self, '_conn'):
            self._conn = redis.StrictRedis(
                host=self.config.get('host', 'localhost'),
                port=int(self.config.get('port', 6379)),
                db=0
            )
        return self._conn

    def value(self, host, port):
        return '%s:%s' % (host, port)

    def clear(self, name):
        self.conn.delete(name)

    def join(self, name, host, port):
        self.conn.sadd(name, self.value(host, port))

    def enrolled(self, name):
        return self.conn.smembers(name)

    def leave(self, name, host, port):
        self.conn.srem(name, self.value(host, port))


class roster(object):

    def __init__(self, config, name):
        self.config = config
        self.enroller = Enroller(self.config)
        self.name = name

    def __iter__(self):
        for member in self.enroller.enrolled(self.name):
            yield member



class enroll(object):

    def __init__(self, config, name, host, port):
        self.enroller = Enroller(config)
        self.name = name
        self.host = host
        self.port = port
        self.args = (self.name, self.host, self.port)

    def __enter__(self):
        self.enroller.join(*self.args)

    def __exit__(self, *args):
        print('leaving: %s %s %s' % self.args)
        self.enroller.leave(*self.args)


def main():
    e = Enroller({})
    e.clear('foo')
    e.join('foo', 'bar', 8080)
    e.join('foo', 'bar', 9090)
    print(e.enrolled('foo'))

if __name__ == '__main__':
    main()

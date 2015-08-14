import subprocess


class Package(object):

    def __init__(self, name):
        self.name = name

    def install(self):
        print "Installing %s" % self.name
        command = ['apt-get', 'install', '-y', self.name]
        output = self._ok(command)
        if not self.installed():
            raise Exception('Package was not installed! output: %s' %
                            output)

    def remove(self):
        print "Removing %s" % self.name
        command = ['apt-get', 'remove', '-y', self.name]
        output = self._ok(command)
        if self.installed():
            raise Exception('Package was not removed! output: %s' %
                            output)

    def installed(self):
        command = ['dpkg', '-s', self.name]
        output = self._ok(command)
        if 'is not installed' in output:
            return False
        if 'install ok installed' in output:
            return True
        raise Exception('Package is in undetermined state, output: %s' %
                        output)

    def _ok(self, command):
        try:
            return subprocess.check_output(command, stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as e:
            return e.output
        except Exception as e:
            return 'Command %s failed miserably' % str(command)

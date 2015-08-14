from spanky.resources import package

try:
    p = package.Package('nginx')
    print p.name
    p.install()
    p.remove()
except Exception as e:
    print e.message

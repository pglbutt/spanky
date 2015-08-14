import os


from wsgiref.simple_server import make_server

# A relatively simple WSGI application. It's going to print out the
# environment dictionary after being updated by setup_testing_defaults
def simple_app(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/plain')]

    start_response(status, headers)
    return [os.environ['PORT']]


def main():
    port = int(os.environ.get('PORT', 8000))
    httpd = make_server('', port, simple_app)
    print "Serving on port %s..." % port
    httpd.serve_forever()

if __name__ == '__main__':
    main()

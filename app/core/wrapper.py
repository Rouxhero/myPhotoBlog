import cherrypy

def auth(func):
    def wrapper(*args, **kwargs):
        if not cherrypy.session.get('user'):
            raise cherrypy.HTTPRedirect('/login')
        return func(*args, **kwargs)
    return wrapper

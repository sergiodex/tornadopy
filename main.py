import tornado.web
import tornado.ioloop
import tornado.autoreload

class HomeRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("web/dist/index.html")

class AdminRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("web/dist/admin.html")

class FrPortalRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("web/dist/frPortal.html")

class LoginRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("web/dist/login.html")

class LoginStoreRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("web/dist/loginStore.html")

class ManageUsersRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("web/dist/loginStore.html")

class StatsRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("web/dist/stats.html")

if __name__ == "__main__":

    public_static_paths = [
        'index.html',
        'admin.html',
        'frPortal.html',
        'login.html',
        'loginStore.html',
        'manageUsers.html',
        'stats.html',
    ]

    tornado.autoreload.start()
    for path in public_static_paths:
        tornado.autoreload.watch("web/dist/" + path)

    app = tornado.web.Application([
        (r"/", HomeRequestHandler),
        (r"/admin", AdminRequestHandler),
        (r"/frPortal", FrPortalRequestHandler),
        (r"/login", LoginRequestHandler),
        (r"/loginStore", LoginStoreRequestHandler),
        (r"/manageUsers", ManageUsersRequestHandler),
        (r"/stats", StatsRequestHandler)
    ])

    app.listen(8881)
    print("I'm listening on port 8881")
    tornado.ioloop.IOLoop.current().start()
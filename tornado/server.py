import tornado.web
import tornado.ioloop
import tornado.autoreload
import psycopg2
from config import config


class HomeRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("../web/dist/index.html")


class AdminRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("../web/dist/admin.html")


class FrPortalRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("../web/dist/frPortal.html")


class LoginRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("../web/dist/login.html")


class LoginStoreRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("../web/dist/loginStore.html")


class ManageUsersRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("../web/dist/loginStore.html")


class StatsRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("../web/dist/stats.html")


def connect():
    """ Connect to the PostgreSQL database server """
    connection = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print("Connecting to the PostgreSQL database...")
        connection = psycopg2.connect(**params)

        # create a cursor
        cursor = connection.cursor()

        query = "select * from account"
        cursor.execute(query)

        # Selecting rows from account table using cursor.fetchall
        users = cursor.fetchall()

        # Print each row and it's columns values
        for row in users:
            print("username = ", row[1])
            print("email  = ", row[3], "\n")

        # close the communication with the PostgreSQL
        cursor.close()
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL >>", error)

    finally:
        if connection is not None:
            connection.close()
            print("Database connection closed.")


if __name__ == "__main__":

    public_static_paths = [
        "index.html",
        "admin.html",
        "frPortal.html",
        "login.html",
        "loginStore.html",
        "manageUsers.html",
        "stats.html",
    ]

    tornado.autoreload.start()
    for path in public_static_paths:
        tornado.autoreload.watch("web/dist/" + path)

    app = tornado.web.Application(
        [
            (r"/", HomeRequestHandler),
            (r"/admin", AdminRequestHandler),
            (r"/frPortal", FrPortalRequestHandler),
            (r"/login", LoginRequestHandler),
            (r"/loginStore", LoginStoreRequestHandler),
            (r"/manageUsers", ManageUsersRequestHandler),
            (r"/stats", StatsRequestHandler),
        ]
    )

    app.listen(8881)
    print("I'm listening on port 8881")
    connect()
    tornado.ioloop.IOLoop.current().start()

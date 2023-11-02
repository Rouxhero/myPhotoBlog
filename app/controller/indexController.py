# -*- coding: utf-8 -*-
# oOoOo Author oOoOo
#      Rouxhero
# -------------------

import cherrypy
from faker import Faker
from app.controller.core.Controller import Controller
from app.core.wrapper import auth
from app.models.page import Page
from app.models.user import User

class indexController(Controller):
    

    def index(self):
        users = User().get_all()
        print(users)
        return self.render('client/index',{
            "users": users
        })

    @auth
    def admin(self):
        pages = Page().get_all()
        return self.render('admin/index',{
            "pages": pages
        })

    @auth
    def pages(self):
        pages = Page().get_all()
        return self.render('admin/pages',{
            "pages": pages
        })
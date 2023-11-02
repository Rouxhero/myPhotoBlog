# -*- coding: utf-8 -*-
# oOoOo Author oOoOo
#      Rouxhero
# ------------------


import cherrypy
from faker import Faker
from app.controller.core.Controller import Controller
from app.core.mailer import Mailer
from app.core.tools import hashP
from app.models.page import Page
from app.models.user import User

class loginController(Controller):
    

    def login(self, email, password):
        user = User().get(email=email)
        if user:
            if user['password'] == hashP(password):
                cherrypy.session['user'] = user
                return self.redirect('/admin')
        return self.render('admin/login',{
            "error": "Invalid credentials"
        })
    
    def login_g(self):
        return self.render('admin/login')


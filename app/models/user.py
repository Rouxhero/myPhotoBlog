# -*- coding: utf-8 -*-
# oOoOo Author oOoOo
#      Rouxhero
# -------------------

from app.models.core import Model


class User(Model):

    fields = {
        "username": ("","required"),
          "password":  ("","required"),
          "email":  ("","required"),
          "last_login":  ("",False)}

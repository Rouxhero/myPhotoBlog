# -*- coding: utf-8 -*-
# oOoOo Author oOoOo
#      Rouxhero
# -------------------

from app.models.core import Model


class Component(Model):

    fields = {
        "name": ("","required"),
        "template":  ("","required"),
        "setting":  ({},"required")
    }

# -*- coding: utf-8 -*-
# oOoOo Author oOoOo
#      Rouxhero
# -------------------

import json
import cherrypy
from faker import Faker
from app.controller.core.Controller import Controller
from app.core.mailer import Mailer
from app.core.wrapper import auth
from app.models.component import Component
from app.models.page import Page
from app.models.user import User

class pageController(Controller):
    
    @auth
    def index(self, id:list):
        page_name = id[0]
        id_page = id[1]
        page = Page().get(id=id_page)
        components = Component().get_all()
        for c in page['elements']['composant']:
            comp = Component().get(id=c['element_id'])
            c['object'] = comp
        layout = {}
        return self.render('admin/page_edit',{
            "page": page,
            "composants": components,
            "layout": layout
        })
    
    @auth
    def preview(self, id:int):
        page = Page().get(id=id)
        return "TODO"  

    @auth
    def get_component(self, id_e:int, id_p:int):
        component = Component().get(id=id_e)
        if component is None:
            raise cherrypy.HTTPError(404, "Component not found")
        return self.render('admin/page/compo_editor',{
            "e": component
        })
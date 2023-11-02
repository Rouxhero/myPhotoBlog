# -*- coding: utf-8 -*-
# oOoOo Author oOoOo
#      Rouxhero
# -------------------
import cherrypy
from app.core.tools import env,config


class Controller:
    """
    Controller class
    """    
    
    def __init__(self):
        pass

    def render(self, name:str, data:dict={})->str:
        """
        Render a Jinja template

        Args:
            name (str): template Name
            data (dict, optional): Data to add on the template. Defaults to {}.

        Returns:
            str: _description_
        """            
        if not "context" in data:
            data["context"] = {
                "uri":"http://"+config['host']+":8000"+"/",
            }
        template = env.get_template(name + ".html")
        output = template.render(data)
        return output

    def redirect(self, path:str)->str:
        """
        Redirect to a path

        Args:
            path (str): Path to redirect

        Returns:
            str: _description_
        """        
        raise cherrypy.HTTPRedirect(path)

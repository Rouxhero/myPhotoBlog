from app.controller.auth.loginController import loginController
from app.controller.indexController import indexController
from app.controller.pageController import pageController
from app.core.route import Route


routes = [
    Route("/", "GET", indexController, "index"),
    Route("/admin", "GET", indexController, "admin"),
    Route("/admin/pages", "GET", indexController, "pages")    
    ]

pages = [
    Route("/admin/pages/edit", "GET", pageController, "index"),
    Route("/admin/pages/preview" , "GET", pageController, "preview"),
    Route("/pages/component/get", "GET", pageController, "get_component"),
]

routes = routes + pages
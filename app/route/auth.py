from app.controller.auth.loginController import loginController
from app.core.route import Route


routes = [
    Route("/editor", "GET", loginController, "login_g"),
    Route("/editor", "POST", loginController, "login")]


from system.core.controller import *

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)

        # self.load_model('User')

   
    def index(self):
        return self.load_view('/users/index.html')

    def login(self):
        return self.load_view('/users/login.html')



from system.core.controller import *

class Locations(Controller):
    def __init__(self, action):
        super(Locations, self).__init__(action)
        # self.load_model('WelcomeModel')

   
    def index(self):
        return self.load_view('locations/index.html')


    # def location(self, id): #we will user this once db set up
    def location(self):
        return self.load_view('/locations/location.html')
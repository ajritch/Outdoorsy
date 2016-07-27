
from system.core.controller import *

class Locations(Controller):
    def __init__(self, action):
        super(Locations, self).__init__(action)
        self.load_model('Location')

   
    def index(self):
        return self.load_view('locations/index.html')


    # def location(self, id): #we will user this once db set up
    def location(self):
        return self.load_view('/locations/location.html')

    def search(self):
    	return self.load_view('/locations/search.html')

    def add(self):
        info = request.form
        add_status = self.models['Location'].add(info)
        if add_status['status'] == False:
            flash(add_status['error'])
            return self.load_view('/partials/search.html')
        return redirect('/location')
        

from system.core.controller import *

class Locations(Controller):
    def __init__(self, action):
        super(Locations, self).__init__(action)
        self.load_model('Location')

   
    def index(self):
        return self.load_view('locations/index.html')


    def location(self, id):
        location = self.models['Location'].get_by_id(id)
        return self.load_view('/locations/location.html', location = location)

    def search(self):
    	return self.load_view('/locations/search.html')

    def add(self):
        #DELETE ME BEFORE PUSHING TO GIT!!!!
        key = "KEEEEY"
        info = request.form
        if not info['address'] == "":
            url = "https://maps.googleapis.com/maps/api/geocode/json?address=" + info['address'] + "&key=" + key
            url.replace(" ", "+")
        add_status = self.models['Location'].add(info)
        if add_status['status'] == False:
            for error in add_status['errors']:
                flash(error)
            return self.load_view('/partials/search.html')
        else:
            return '/location/' + str(add_status['id'])
            # return redirect('/location/' + str(add_status['id']))
            
        
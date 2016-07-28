
from system.core.controller import *

class Locations(Controller):
    def __init__(self, action):
        super(Locations, self).__init__(action)
        self.load_model('Location')
        self.load_model('Review')

   
    def index(self):
        all_reviews = self.models['Review'].show_all()
        locations = self.models['Location'].get_all()
        favorites = self.models['Location'].get_favorites(session['id'])
        return self.load_view('locations/index.html', all_reviews = all_reviews, locations = locations, favorites = favorites)


    def location(self, id):
        location = self.models['Location'].get_by_id(id)
        reviews = self.models['Review'].get_all_by_id(id)
        return self.load_view('/locations/location.html', location = location, reviews = reviews)

    def search(self):
        locations = self.models['Location'].get_all()
    	return self.load_view('/locations/search.html', locations = locations)

    def add(self):
        #DELETE ME BEFORE PUSHING TO GIT!!!!
        key = "AIzaSyBdiquOm9WFMncLQxflWIf6_P6wJxxUKbM"
        info = request.form
        if not info['address'] == "":
            url = "https://maps.googleapis.com/maps/api/geocode/json?address=" + info['address'] + "&key=" + key
            url.replace(" ", "+")
        add_status = self.models['Location'].add(info)
        if add_status['status'] == False:
            for error in add_status['errors']:
                flash(error)
            return self.load_view('/locations/partials/search.html')
        else:
            return '/location/' + str(add_status['id'])
            # return redirect('/location/' + str(add_status['id']))

    def add_favorite(self, id):
        self.models['Location'].add_favorite(session['id'], id)
        #due to AJAX this won't acutally redirect
        return redirect('/location/' + str(id))

    def edit_description(self, id):
        info = request.form
        self.models['Location'].edit_description(info, id)
        location = self.models['Location'].get_by_id(id)
        return self.load_view('/locations/partials/description.html', location = location)

    def remove_favorite(self, id):
        self.models['Location'].remove_favorite(session['id'], id)
        favorites = self.models['Location'].get_favorites(session['id'])
        return self.load_view('/locations/partials/favorites.html', favorites = favorites)

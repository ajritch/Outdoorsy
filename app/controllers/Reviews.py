
from system.core.controller import *

class Reviews(Controller):
    def __init__(self, action):
        super(Reviews, self).__init__(action)
        self.load_model('Review')
        
   
    def add(self, id):
        info = request.form
        print info
        self.models['Review'].add(info, id, session['id'])
        print "model went through"
        reviews = self.models['Review'].get_all_by_id(id)
        return self.load_view('/locations/partials/reviews.html', reviews = reviews)

    def delete(self, location_id, review_id):
        self.models['Review'].delete(review_id)
        reviews = self.models['Review'].get_all_by_id(location_id);
        return self.load_view('/locations/partials/reviews.html', reviews = reviews)
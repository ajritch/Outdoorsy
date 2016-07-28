
from system.core.controller import *

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)

        self.load_model('User')

   
    def index(self):
        return self.load_view('/users/index.html')

    def login(self):
        return self.load_view('/users/login.html')

    def register(self):
    	#print request.form
    	new_user={
    		"fbname": request.form['fbname'],
    		"fbid": request.form['fbid'],
    		"fbtoken": request.form['fbtoken']
    	}
        session['token'] = request.form['fbtoken']

    	add_user = self.models['User'].add_submit(new_user)
        if add_user['status'] == True:
            session['id'] = add_user['id']
            session['name'] = new_user['fbname']
            #redirecting actually happens via the post in login.html
            return redirect('/home')
        else:
            return redirect('/login')
            
        




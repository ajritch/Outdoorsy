
from system.core.controller import *

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)

        self.load_model('User')

   
    def index(self):
        return self.load_view('/users/index.html')

    def login(self):
        return self.load_view('/users/login.html')

    def logout(self):
        session.clear()
        return redirect('/')

    def register(self):
        return self.load_view('/users/register.html')

    def do_login(self):
        info = {
            'email': request.form['email'],
            'password': request.form['password']
        }
        login_status = self.models['User'].do_signin(info)
        if login_status['status'] == False:
            flash(login_status['error'])
            return redirect('/login')
        else:
            session['id'] = login_status['id']
            session['name'] = login_status['first_name']
            return redirect('/home')

    def do_register(self):
    	#print request.form
    	info = {
            'first_name' : request.form['first_name'],
            'last_name' : request.form['last_name'],
            'email' : request.form['email'],
            'password' : request.form['password'],
            'conf_password': request.form['conf_password']
        }
        add_status = self.models['User'].add_user(info)
        if add_status['status'] == False:
            for error in add_status['errors']:
                flash(error)
            if 'id' not in session:
                return redirect('/register')
            else:
                return redirect('/users/new')
        else:
            if 'id' not in session:
                session['id'] = add_status['id']
                session['name'] = add_status['first_name']
            return redirect('/home')
            
        




""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

class User(Model):
    def __init__(self):
        super(User, self).__init__()

    def do_signin(self, info):
        #get info from database
        query = "SELECT * FROM users WHERE email = :email"
        data = {'email': info['email']}
        user = self.db.query_db(query, data)
        #is the email registered yet?
        if len(user) == 0:
            return {'status': False, 'error': "That email is not registered to a user."}
        #does the entered password match?
        if not self.bcrypt.check_password_hash(user[0]['password'], info['password']):
            return {'status': False, 'error': "Incorrect password."}
        else:
            return {'status': True, 'id': user[0]['id'], 'first_name': user[0]['first_name']}

    def add_user(self, info):

        errors = []
        #check: has this email already been entered?
        query = "SELECT * FROM users WHERE email = :email"
        data = {'email': info['email']}
        user = self.db.query_db(query, data)
        if len(user) > 0:
            errors.append("That email address has already been registered.")
        #standard validations
        if not EMAIL_REGEX.match(info['email']):
            errors.append("Invalid email address.")
        if len(info['first_name']) < 2 or len(info['last_name']) < 2:
            errors.append("Name fields must contain at least 2 letters.")
        if not info['first_name'].isalpha() or not info['last_name'].isalpha():
            errors.append("Name fields must only contain letters.")
        if len(info['password']) < 8:
            errors.append('Password must contain at least 8 characters.')
        if not re.compile(r'\d').search(info['password']):
            errors.append("Password must contain at least 1 number.")
        if info['password'] != info['conf_password']:
            errors.append("Confirmation password must match password.")

        if errors:
            return {'status': False, 'errors': errors}
        else:
            query = ("INSERT INTO users " +
                    "(first_name, last_name, email, password, created_at, updated_at) " +
                    "VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())")
            data = {
                'first_name': info['first_name'],
                'last_name': info['last_name'],
                'email': info['email'],
                'password': self.bcrypt.generate_password_hash(info['password']),
            }
            new_id = self.db.query_db(query, data)
            return {'status': True, 'id': new_id, 'first_name': info['first_name']}


    def add_submit(self, new_user):
        # errors = []
        # if errors:
        #     return {'status': False, "errors": errors}

        check_query = "SELECT * FROM users WHERE fb_id = :id"
        check_data = {'id': new_user['fbid']}
        check_user = self.db.query_db(check_query, check_data)
        if len(check_user) > 0:
            update_query = "UPDATE users SET fb_token = :fb_token, name = :name, updated_at = NOW() WHERE fb_id = :fb_id"
            update_data = {
                'fb_token': new_user['fbtoken'],
                'fb_id': new_user['fbid'],
                'name': new_user['fbname']
            }
            return {'status': True, 'id': check_user[0]['id']}
        else:
            add_query = "INSERT INTO users (name, fb_id, fb_token, created_at, updated_at) VALUES (:name, :fb_id, :fb_token, NOW(), NOW())"
            add_data = {
                'name': new_user['fbname'],
                'fb_id': new_user['fbid'],
                'fb_token': new_user['fbtoken']
            }
            id = self.db.query_db(add_query, add_data)
            return {'status': True, 'id': id}
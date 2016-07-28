""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model

class User(Model):
    def __init__(self):
        super(User, self).__init__()

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
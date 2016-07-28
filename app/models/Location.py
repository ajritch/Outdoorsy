""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model

class Location(Model):
    def __init__(self):
        super(Location, self).__init__()

    def add(self, info):
        errors = []
        if info['name'] == '':
            errors.append('You must enter a location name.')
        if not (info['address'] or (info['latitude'] and info['longitude'])):
            errors.append('You must enter either an address or a pair of coordinates.')
        if errors:
            return {'status': False, 'errors': errors}
        query = "INSERT INTO locations (name, latitude, longitude, created_at) VALUES (:name, :latitude, :longitude, NOW())"
        data = {
            'name': info['name'],
            'latitude': info['latitude'],
            'longitude': info['longitude']
        }
        id = self.db.query_db(query, data)
        return {'status': True, 'id': id}

    def get_by_id(self, id):
        query = ('SELECT * FROM locations ' +
                'WHERE id = :id')
        data = {'id': id}
        return self.db.query_db(query, data)[0]

    def add_favorite(self, user_id, location_id):
        data = {
            'user_id': user_id,
            'location_id': location_id
        }
        #first, check if it's there already
        check_query = "SELECT * FROM favorites WHERE user_id = :user_id AND location_id = :location_id"
        check = self.db.query_db(check_query, data)
        if len(check) > 0:
            return {'status': False}

        query = ("INSERT INTO favorites (user_id, location_id) " +
                "VALUES (:user_id, :location_id)")
        return self.db.query_db(query, data)

    def edit_description(self, info, id):
        query = "UPDATE locations SET description = :description, updated_at = NOW() WHERE id = :id"
        data = {
            'description': info['description'],
            'id': id
        }
        return self.db.query_db(query, data)

    def get_all(self):
        return self.db.query_db("SELECT * FROM locations")

    def get_favorites(self, id):
        query = ("SELECT location_id, name FROM favorites " +
                "JOIN locations ON favorites.location_id = locations.id " +
                "WHERE favorites.user_id = :id") 
        data = {'id': id}
        return self.db.query_db(query, data)

    def remove_favorite(self, user_id, location_id):
        query = "DELETE FROM favorites WHERE user_id = :user_id AND location_id = :location_id"
        data = {
            'user_id': user_id,
            'location_id': location_id
        }
        return self.db.query_db(query, data)
    


    """
    Below is an example of a model method that queries the database for all users in a fictitious application
    
    Every model has access to the "self.db.query_db" method which allows you to interact with the database

    def get_users(self):
        query = "SELECT * from users"
        return self.db.query_db(query)

    def get_user(self):
        query = "SELECT * from users where id = :id"
        data = {'id': 1}
        return self.db.get_one(query, data)

    def add_message(self):
        sql = "INSERT into messages (message, created_at, users_id) values(:message, NOW(), :users_id)"
        data = {'message': 'awesome bro', 'users_id': 1}
        self.db.query_db(sql, data)
        return True
    
    def grab_messages(self):
        query = "SELECT * from messages where users_id = :user_id"
        data = {'user_id':1}
        return self.db.query_db(query, data)

    """
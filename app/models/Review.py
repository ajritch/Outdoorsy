
from system.core.model import Model

class Review(Model):
    def __init__(self):
        super(Review, self).__init__()

    def add(self, info, location_id, user_id):
        query = ("INSERT INTO reviews (content, created_at, updated_at, user_id, location_id) " +
                "VALUES (:content, NOW(), NOW(), :user_id, :location_id)")
        data = {
            'content': info['content'],
            'user_id': user_id,
            'location_id': location_id
        }
        return self.db.query_db(query, data)


    def get_all_by_id(self, location_id):
        query = ("SELECT reviews.id as id, location_id, content, reviews.updated_at, user_id, name " +
                "FROM reviews JOIN users ON reviews.user_id = users.id " +
                "WHERE reviews.location_id = :location_id")
        data = {'location_id': location_id}
        return self.db.query_db(query, data)

    def show_all(self):
        query = "SELECT users.name, locations.name AS location, reviews.content, reviews.rating, reviews.created_at, reviews.updated_at, reviews.user_id AS user_id, reviews.location_id AS location_id FROM reviews LEFT JOIN users ON reviews.user_id = users.id LEFT JOIN locations ON reviews.location_id = locations.id ORDER BY reviews.created_at DESC LIMIT 5"
        return self.db.query_db(query)

    def delete(self, id):
        query = "DELETE FROM reviews WHERE id = :id"
        data = {'id': id}
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
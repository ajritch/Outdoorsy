"""
    Routes Configuration File

    Put Routing rules here
"""
from system.core.router import routes

"""
    This is where you define routes
    
    Start by defining the default controller
    Pylot will look for the index method in the default controller to handle the base route

    Pylot will also automatically generate routes that resemble: '/controller/method/parameters'
    For example if you had a products controller with an add method that took one parameter 
    named id the automatically generated url would be '/products/add/<id>'
    The automatically generated routes respond to all of the http verbs (GET, POST, PUT, PATCH, DELETE)
"""
routes['default_controller'] = 'Users'
routes['GET']['/login'] = 'Users#login'
routes['GET']['/logout'] = 'Users#logout'
routes['GET']['/register'] = 'Users#register'
routes['POST']['/login'] = 'Users#do_login'
routes['GET']['/home'] = 'Locations#index'
routes['GET']['/search'] = 'Locations#search'
routes['POST']['/register'] = 'Users#do_register'
routes['POST']['/location/add'] = 'Locations#add'
routes['GET']['/location/<int:id>'] = 'Locations#location'
routes['POST']['/reviews/add/<int:id>'] = 'Reviews#add'
routes['GET']['/locations/add_favorite/<int:id>'] = 'Locations#add_favorite'
routes['POST']['/locations/<int:id>/edit_description'] = 'Locations#edit_description'
routes['GET']['/remove_favorite/<int:id>'] = 'Locations#remove_favorite'
routes['GET']['/reviews/delete/<int:location_id>/<int:review_id>'] = 'Reviews#delete'



"""
    You can add routes and specify their handlers as follows:

    routes['VERB']['/URL/GOES/HERE'] = 'Controller#method'

    Note the '#' symbol to specify the controller method to use.
    Note the preceding slash in the url.
    Note that the http verb must be specified in ALL CAPS.
    
    If the http verb is not provided pylot will assume that you want the 'GET' verb.

    You can also use route parameters by using the angled brackets like so:
    routes['PUT']['/users/<int:id>'] = 'users#update'

    Note that the parameter can have a specified type (int, string, float, path). 
    If the type is not specified it will default to string

    Here is an example of the restful routes for users:

    routes['GET']['/users'] = 'users#index'
    routes['GET']['/users/new'] = 'users#new'
    routes['POST']['/users'] = 'users#create'
    routes['GET']['/users/<int:id>'] = 'users#show'
    routes['GET']['/users/<int:id>/edit' = 'users#edit'
    routes['PATCH']['/users/<int:id>'] = 'users#update'
    routes['DELETE']['/users/<int:id>'] = 'users#destroy'
"""

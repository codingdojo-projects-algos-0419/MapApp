from config import app
from server.controllers import locations

app.add_url_rule('/location/<location_id>', view_func=locations.view_location, endpoint='locations:view_location', methods=['POST', 'GET'])
app.add_url_rule('/location/<location_id>/like', view_func=locations.like, endpoint='locations:like', methods=['POST', 'GET'])
app.add_url_rule('/location/<location_id>/remove_like', view_func=locations.remove_like, endpoint='locations:remove_like', methods=['POST', 'GET'])

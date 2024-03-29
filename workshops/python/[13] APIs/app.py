from flask import Flask, request
from flask_restx import Api, Resource, fields

flask_app = Flask(__name__)
app = Api(app = flask_app, 
		  version = "1.0", 
		  title = "Name Recorder", 
		  description = "Manage names of various users of the application")

name_space = app.namespace('names', description='Manage names')
model = app.model('Name Model', 
				  {'name': fields.String(required = True,
    					  				 description="Name of the person",
    					  				 help="Name cannot be blank.")})

list_of_names = {}

@name_space.route("/<int:id>")
class MainClass(Resource):
	def get(self, id):
		try:
			return { 'status': "Person retrieved", 'name' : list_of_names[id] }
		except KeyError as e:
			name_space.abort(500, e.__doc__, status = "Could not retrieve information", statusCode = "500")
		except Exception as e:
			name_space.abort(400, e.__doc__, status = "Could not retrieve information", statusCode = "400")

	@app.expect(model)		
	def post(self, id):
		try:
			list_of_names[id] = request.json['name']
			return { 'status': "New person added", 'name': list_of_names[id] }
		except KeyError as e:
			name_space.abort(500, e.__doc__, status = "Could not save information", statusCode = "500")
		except Exception as e:
			name_space.abort(400, e.__doc__, status = "Could not save information", statusCode = "400")

flask_app.run(debug=True)
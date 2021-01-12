from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
#establish location of where our database is
DB_URL = 'postgresql://postgres:passy123@localhost:5432/sneaker_app'
app.config["SQLALCHEMY_DATABASE_URI"] = DB_URL
#initialize db object to use SQLALCHEMY
db = SQLAlchemy(app)

class VideoModel(db.Model):
	ID = db.Column(db.Integer, primary_key = True)
	#nullable = False means this field has to have this information, a video will have some kind of name
	name = db.Column(db.String(100), nullable = False)
	views = db.Column(db.Integer, nullable = False)
	likes = db.Column(db.Integer, nullable = False)

	#String representation of what these videos will look like
	#Only h appens when you decide to print the representation of this obejct
	def __repr__(self):
		return f"Video(name = {name}, views = {views}, likes = {likes})"

#db.create_all()


names = {"tim":{"age": 19, "gender":"male"},
		 "billy": {"age": 26, "gender": "male"}}

class HelloWorld(Resource):
	def get(self, name):
		return names[name]

	def put(self, name):
		print(request.form)
		return {}


#Assures we are sending/receiving the correct information
#make sure we are receving all the fields in the request
#establishes the correct type and fields for the data we are receiving
#what we should display to the sender if they dont send us the correct argument
video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video is required", required = True)
video_put_args.add_argument("views", type=str, help="Views of the video")
video_put_args.add_argument("likes", type=str, help="Likes of the video")



videos={}


def abort_if_video_id_doesnt_exist(video_id):
	if video_id not in videos:
		abort(404, message = "Video ID does not exist")

def abort_if_video_id_exists(video_id):
	if video_id in videos:
		abort(409, message = "VIdeo ID already exists")


class Video(Resource):
	def get(self, video_id):
		result = VideoModel.query.get(id=video_id)
		return result

	def put(self, video_id):
		abort_if_video_id_exists(video_id)
		args = video_put_args.parse_args()
		videos[video_id] = args
		return videos[video_id], 201
		#can send a response code to the person who is sending the request
		#return videos[video_id], 201

	def delete(self, video_id):
		abort_if_video_id_doesnt_exist(video_id)
		del videos[video_id]
		return "", 204

api.add_resource(Video, "/video/<int:video_id>")

'''
This is using a particular index, which is indexed by name, to look for the indexed data in the database or where data is stored.
This uses the HelloWorld class that uses a GET method to return data

names = {"tim":{"age": 19, "gender":"male"},
		 "billy": {"age": 26, "gender": "male"}}

class HelloWorld(Resource):
	def get(self, name):
		return names[name]

From this example, we can use other classes like /about or /user/ID to return data from api
Think about use cases for this for the sneakers API

Also from this example, think about ways the API queries data from an actual PROD database
'''

'''
class Video(Resource):
	def get(self, video_id):
		return videos[video_id]

	def put(self, video_id):
		return 

api.add_resource(Video, "/video/<int:video_id>")
'''

#use request.method to check the request

#api.add_resource(HelloWorld, "/helloworld/<string:name>")

if __name__ == "__main__":
	app.run(debug=True)
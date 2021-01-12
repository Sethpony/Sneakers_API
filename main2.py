from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
import psycopg2

app = Flask(__name__)
api = Api(app)
#establish location of where our database is
DB_URL = 'postgresql://postgres:passy123@localhost:5432/sneaker_app'
app.config["SQLALCHEMY_DATABASE_URI"] = DB_URL
#initialize db object to use SQLALCHEMY
db = SQLAlchemy(app)

#Re-check nullable or not... Think about it is it essential to have retail price in there or only sale price etc. Business cases and usage....
class SneakerModel(db.Model):
	Index_ID = db.Column(db.Integer, primary_key = True)
	Order_Date = db.Column(db.DateTime, nullable = False)
	Brand = db.Column(db.String(255), nullable = False)
	Sneaker_Name = db.Column(db.String(255), nullable = False)
	Sale_Price = db.Column(db.Float, nullable = False)
	Retail_Price = db.Column(db.Float, nullable = False)
	Release_Date = db.Column(db.DateTime, nullable = False)
	Shoe_Size = db.Column(db.Float, nullable = False)
	Buyer_Region = db.Column(db.String(255))

	#String representation of what these videos will look like
	#Only h appens when you decide to print the representation of this obejct
	def __repr__(self):
		return f"Sneaker(Index_ID = {Index_ID}, Order_Date = {Order_Date}, Brand = {Brand}, Sneaker_Name = {Sneaker_Name}, Sale_Price = {Sale_Price}, Retail_Price = {Retail_Price}, Release_Date = {Release_Date}, Shoe_Size = {Shoe_Size}, Buyer_Region = {Buyer_Region})"

#db.create_all()
#Assures we are sending/receiving the correct information
#make sure we are receving all the fields in the request
#establishes the correct type and fields for the data we are receiving
#what we should display to the se nder if they dont send us the correct argument


sneaker_put_args = reqparse.RequestParser()
sneaker_put_args.add_argument("ID", type=str, help="ID of the sneaker is required", required = True)
sneaker_put_args.add_argument("Order_date", type=str, help="Order date of the sneaker is required")
sneaker_put_args.add_argument("Brand", type=str, help="Brand of the sneaker is required")
sneaker_put_args.add_argument("Sneaker_Name", type=str, help="Name of the sneaker is required", required = True)
sneaker_put_args.add_argument("Sale_Price", type=str, help="Sale Price of the sneaker is required")
sneaker_put_args.add_argument("Retail_Price", type=str, help="Retail Price of the sneaker is required")
sneaker_put_args.add_argument("Release_Date", type=str, help="Release Date of the sneaker is required", required = True)
sneaker_put_args.add_argument("Shoe_Size", type=str, help="Shoe size of the sneaker is required")
sneaker_put_args.add_argument("Buyer Region", type=str, help="Buy Region of the sneaker is required")

#insert resource fields here - SERIALIZING THESE OBJECTS
#define what we want the fields to be
#Create a dictionary called resource_fields define fields from Model that I want to return if I return a specific object
#ID field here is equal to fields.string, that's the type of field that it is
resource_fields = {
	'Index_ID': fields.String,
	'Order_Date': fields.DateTime,
	'Brand': fields.String,
	'Sneaker_Name': fields.String,
	'Sale_Price': fields.Float,
	'Retail_Price': fields.Float,
	'Release_Date': fields.DateTime,
	'Shoe_Size': fields.Float,
	'Buyer_Region': fields.String
}

#def abort_if_sneaker_id_doesnt_exist(sneaker_id):
	#if sneaker_id not in db.ID:0
		#abort(404, message = "Sneaker ID does not exist")

#def abort_if_sneaker_id_exists(sneaker_id):
	#if sneaker_id in videos:
		#abort(409, message = "Sneaker ID already exists")


class Sneaker(Resource):
	@marshal_with(resource_fields)
	def get(self, sneaker_id):
		result = SneakerModel.query.limit(5).all()
		return result
	'''
	def put(self, sneaker_id):
		abort_if_sneaker_id_exists(sneaker_id)
		args = sneaker_put_args.parse_args()
		#sneaker[sneaker_id] =args
		video[video_id] = args
		return videos[video_id], 201
		#can send a response code to the person who is sending the request
		#return videos[video_id], 201

	def delete(self, sneaker_id):
		abort_if_sneaker_id_doesnt_exist(sneaker_id)
		#del sneaker[sneaker_id]
		del videos[video_id]
		return "", 204
	'''
api.add_resource(Sneaker, "/sneaker/<int:sneaker_id>")

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
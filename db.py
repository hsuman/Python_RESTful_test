from mongoengine import *
import json
connect('prtdb')

class Users(Document):
    Id = IntField(required=True, max_length=10)
    fname = StringField(required=True, max_length=50)
    lname = StringField(required=True, max_length=50)
    latitude = FloatField(required=True, max_length=10)
    longitude = FloatField(required=True, max_length=10)

    def get_users():
    	return Users.objects()

    def get_users_by_id(id):
    	user = Users.objects(Id=id)	
    	if user:
            return user
    	else:
            return None	


    def create_users(request):  
    	if not Users.get_users_by_id(request.json['id']):
    	    return Users(Id=request.json['id'],fname=request.json['fname'],lname=request.json['lname'],latitude=request.json['latitude'],
    		    longitude=request.json['longitude']).save()
    	else:    
    	    return None

    def update_user(user_id, request):  
        return Users.objects(Id=user_id).update(**json.loads(request.data))	

    def delete_user(user_id):  
        return Users.objects(Id=user_id).delete()
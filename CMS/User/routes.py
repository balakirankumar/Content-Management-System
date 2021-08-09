from flask import request, Blueprint, jsonify, send_from_directory, send_file
from CMS.model import User
from CMS import db,app,bcrypt
from .validation import  validate
import json

user = Blueprint('user',__name__)


@user.route('/user/register',methods=["POST"])
def register():
    data=request.json
    if data:
        if all((data.get('email'),data.get('password'),data.get('fullname'),data.get('phonenumber'),data.get('pincode'))):
            verifed=validate(**{"email":data.get('email'),'password':data.get('password'),"fullname":data.get('fullname'),"phonenumber":data.get('phonenumber'),"pincode":data.get('pincode')})
            print("VERIFIED",verifed)
            if verifed :
                email = data.get('email')
                password = bcrypt.generate_password_hash(data.get('password'))
                fullname = data.get('fullname')
                address = data.get('address')
                phonenumber = data.get('phonenumber')
                city = data.get('city')
                state = data.get('state')
                country = data.get('country')
                pincode = data.get('pincode')
                if User.query.filter_by(email=email).first():
                    return jsonify({"Error":f"User already exist with {email}. Please use other email"})
                user=User(email=email,password=password,fullname=fullname,address=address,phonenumber=phonenumber,city=city,
                    state=state,country=country,pincode=pincode)
                db.session.add(user)
                db.session.commit()
                return jsonify({"status":"Successfull registration use email and password ","email":user.email,"fullname":user.fullname})
            else:
                return jsonify({"Error":"Make sure that all requied fields match required criteria",
                                "email" : "Make sure you enter valid email address",
                                "password":"Minimum 8 characters with 1 upper case and 1 lower case",
                                "fullname":"firstname lastname",
                                "phonenumber":"Integer with 10 digit number",
                                "pincode":"Integer with 6 digit number"
                                })
        else:
            schema={
                "Error" : "Missing data. Refer below fields to post correct",
                "required fields":{
                    "email" : "email",
                    "password":"password",
                    "fullname":"fullname",
                    "phonenumber":"phonenumber",
                    "pincode":"pincode",
                    },
                "optional fields":{
                    "address":"address",
                    "city":"city",
                    "state":"state",
                    "country":"country",
                }
            }
            return jsonify(schema),201
    else:
        return {"data":"No Json data recieved"},201

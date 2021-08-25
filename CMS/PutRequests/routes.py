from flask import request, Blueprint, jsonify
from CMS.model import User,Content
from CMS import db,bcrypt
from .util import download_pdf
import json


put = Blueprint('putRequests',__name__)



@put.route('/uploadFile/<int:id>',methods=["PUT"])
def uploadFile(id):
    try:
        data=request.json
        if data:
            return jsonify({"Error":"Need only File data to upload file"}),400
        print(data)
        if request.authorization :
            username=request.authorization.get('username')
            password=request.authorization.get('password')
            user=User.query.filter_by(email=username).first()
            content=Content.query.get(id)
            if user:
                if bcrypt.check_password_hash(user.password,password):
                    if content:
                        if content.author.email == user.email:
                            if request.files and request.files.get('file').filename.split('.')[-1] in ['txt','pdf']:
                                file=request.files.get('file')
                                name=download_pdf(file)
                                content.document="localhost:5000/user/post/document/download/"+name
                                db.session.commit()
                                return jsonify({"title" : content.title, "body":content.body, "summary": content.summary, "document":content.document, "tags":json.loads(content.tags),"author":content.author.email}),200
                            else:
                                return jsonify({"requiredFields":{"file" :f"type of pdf file required but given {request.files.get('file').filename.split('.')[-1]}"}}),400
                        else:
                            return jsonify({"Error":"You can edit only your post. Sorry for that."}),401
                    else:
                        return jsonify({"Error":f"Make sure that post with id {id} exists."}),404
                else:
                    return jsonify({"Error":"Password wrong. Please try again"}),401
            else:
                return jsonify({"Error":"Authorization failed. Make sure you enter valid username and password"}),401
        else:
            return jsonify({"Error":"You need need to add authorization to access it."}),401

    except Exception as E:
        print(dir(E))
        return jsonify({'Error':{"required":"keyword 'file' missing.","cause":str(E.__cause__),"doc":str(E.__doc__),"traceback":str(E.__traceback__),"args":str(E.args)}}),400













@put.route('/updatepost/<int:id>',methods=["PUT"])
def updatePost(id):
    try:
        data=request.json
        if request.authorization :
            username=request.authorization.get('username')
            password=request.authorization.get('password')
            user=User.query.filter_by(email=username).first()
            content=Content.query.get(id)
            if user:
                if bcrypt.check_password_hash(user.password,password):
                    if data:
                        if content:
                            if content.author.email == username:
                                if data.get('tags') is None or isinstance(data.get('tags'),list) :
                                    content.title = data.get('title') if data.get('title') else content.title
                                    content.body = data.get('body') if data.get('body') else content.body
                                    content.summary = data.get('title') if data.get('summary') else content.summary
                                    content.tags = json.dumps(data.get('tags')) if data.get('tags') else content.tags
                                    db.session.commit()
                                    return jsonify({"title" : content.title, "body":content.body, "summary": content.summary, "document":content.document, "tags":json.loads(content.tags),"author":content.author.email}),201
                                else:
                                    return  jsonify({"requiredFields":{"title" :"String:title", "body":"String:body", "summary": "String:summary"},"optionalFields":{"tags":"list:[tags]"}}),400
                            else:
                                return jsonify({"Error":"You can edit only your post. Sorry for that."}),401
                        else:
                            return jsonify({"Error":f"Make sure that post with id {id} exists."}),404
                    else:
                        return jsonify({"Error":"Need json data please."}),400
                else:
                    return jsonify({"Error":"Password wrong. Please try again"}),401
            else:
                return jsonify({"Error":"Authorization failed. Make sure you enter valid username and password"}),401
        else:
            return jsonify({"Error":"You need need to add authorization to access it."}),401
    except Exception as E:
        return jsonify({'Error':{"required":"keyword 'file' missing.","cause":str(E.__cause__),"doc":str(E.__doc__),"traceback":str(E.__traceback__),"args":str(E.args)}}),400

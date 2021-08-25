from flask import request, Blueprint, jsonify
from CMS.model import User,Content
from CMS import db, bcrypt,app
from .util import download_pdf
import json, os


post = Blueprint('postRequests',__name__)


@post.route('/addpost',methods=["POST"])
def addPost():
    try:
        # data=request.json
        data=json.loads(request.form.get('data'))
        if request.authorization :
            username=request.authorization.get('username')
            password=request.authorization.get('password')
            print(password)
            user=User.query.filter_by(email=username).first()
            if user:
                if bcrypt.check_password_hash(user.password,password):
                    if data.get('title') and data.get('body') and data.get('summary') :
                        name="Did'nt upload any thing"
                        if request.files.get('document') and request.files.get('document').filename.split('.')[-1] in ['txt','pdf']:
                            name=f"localhost:{app.config['PORT']}/post/document/download/"+download_pdf(request.files.get('document'))
                        content = Content(title = data.get('title'), body=data.get('body'), summary=data.get('summary'), document=name, tags=json.dumps(data.get('tags')), author=user)
                        db.session.add(content)
                        db.session.commit()
                        return jsonify({"title" : content.title, "body":content.body, "summary": content.summary, "document":content.document, "tags":json.loads(content.tags),"author":content.author.email,"id":content.id}),201
                    else:
                        return jsonify({"requiredFields":{"title" :"title", "body":"body", "summary": "summary"},"optionalFields":{"tags":["tags"]}}),400
                else:
                    return jsonify({"Error":"Password wrong. Please try again"}),401
            else:
                return jsonify({"Error":"Authorization failed. Make sure you enter valid username and password"}),401
        else:
            return jsonify({"Error":"You need need to add authorization to access it."}),401
    except Exception as E:
        print(dir(E))
        return jsonify({'Error':{"required":"json data missing.","cause":str(E.__cause__),"doc":str(E.__doc__),"traceback":str(E.__traceback__),"args":str(E.args)}}),400

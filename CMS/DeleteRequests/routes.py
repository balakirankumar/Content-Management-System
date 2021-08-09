from flask import request, Blueprint, jsonify, send_from_directory
from CMS.model import User,Content
from CMS import db, bcrypt
import json


delete = Blueprint('deleteRequest',__name__)

@delete.route("/user/post/delete/<int:id>",methods=["DELETE"])
def deletePost(id):
    try:
        if request.authorization :
            username=request.authorization.get('username')
            password=request.authorization.get('password')
            user=User.query.filter_by(email=username).first()
            if user:
                if bcrypt.check_password_hash(user.password,password):
                    content=Content.query.get(id)
                    if content:
                        if content.author.email == username:
                            filename=content.document
                            db.session.delete(content)
                            db.session.commit()
                            os.remove(f"static/documents/{filename}")
                            return jsonify({"title" : content.title, "body":content.body, "summary": content.summary, "document":"deleted", "tags":json.loads(content.tags),"author":content.author.email}),201
                        else:
                            return jsonify({"Error":"You can delete only your post. Sorry for that."}),403
                    else:
                        return jsonify({"Error":f"Make sure that post with id {id} exists."}),404
                else:
                    return jsonify({"Error":"Password wrong. Please try again"}),401
            else:
                return jsonify({"Error":"Authorization failed. Make sure you enter valid username and password"}),401
        else:
            return jsonify({"Error":"You need need to add authorization to access it."}),401
    except Exception as E:
        return jsonify({"url":"'/post/delete/<id>'"}),400

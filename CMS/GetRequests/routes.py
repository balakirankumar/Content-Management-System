from flask import request, Blueprint, jsonify, send_from_directory
from CMS.model import User,Content
import json


get = Blueprint('getRequest',__name__)



@get.route('/user/post/all')
def allPosts():
    data=Content.query.all()
    if data:
        l=[]
        for i in data:
            d={}
            d['id']=i.id;d['title']=i.title;d['body']=i.body;d['summary']=i.summary
            d['document']=i.document;d['tags']=json.loads(i.tags);d['author']=i.author.fullname
            l.append(d)
        return jsonify(l),200
    else:
        return jsonify({"posts":"No posts are there"}),200



@get.route('/user/post/searchbyid/<int:id>')
def singlePost(id):
    print(id)
    data=Content.query.get(id)
    if data:
        d={}
        d['id']=data.id;d['title']=data.title;d['body']=data.body;d['summary']=data.summary
        d['document']=data.document;d['tags']=json.loads(data.tags);d['author']=data.author.fullname
        return jsonify(d),200
    else:
        return jsonify({"Error":f"Post with id of {id} does'nt exist"}),404


@get.route('/user/post/searchbyauthor/<string:fullname>')
def postByAuthor(fullname):
    print(fullname)
    user=User.query.filter(User.fullname.contains(fullname)).all()
    print(user)
    if user :
        l=[]
        for i in user:
            data=Content.query.filter_by(author=i)
            for j in data:
                d={}
                d['id']=j.id;d['title']=j.title;d['body']=j.body;d['summary']=j.summary
                d['document']=j.document;d['tags']=json.loads(j.tags);d['author']=j.author.fullname
                l.append(d)
        if l:
            return jsonify(l),200
        else:
            return jsonify({'success':f"User with email '{email}' has not posted any thing"}),200
    else:
        return jsonify({'Error':f"Users with email containing '{email}' does'nt exist"}),404




@get.route('/user/posts/searchbytitle/<string:title>')
def postByTitle(title):
    data=Content.query.filter(Content.title.contains(title)).all()
    print(data)
    if data :
        l=[]
        for i in data:
            print("i",i)
            d={}
            d['id']=i.id;d['title']=i.title;d['body']=i.body;d['summary']=i.summary
            d['document']=i.document;d['tags']=json.loads(i.tags);d['author']=i.author.fullname
            l.append(d)
        return jsonify(l),200
    else:
        return jsonify({"success":f"No posts with title with '{title}'"}),200



@get.route('/user/posts/searchbytags/<string:tag>')
def postByTag(tag):
    data=Content.query.filter(Content.tags.contains(tag)).all()
    print(data)
    if data :
        l=[]
        for i in data:
            print("i",i)
            d={}
            d['id']=i.id;d['title']=i.title;d['body']=i.body;d['summary']=i.summary
            d['document']=i.document;d['tags']=json.loads(i.tags);d['author']=i.author.fullname
            l.append(d)
        return jsonify(l),200
    else:
        return jsonify({"success":f"No posts with tags '{tag}'"}),200




@get.route('/user/post/document/download/<string:path>',methods=["GET"])
def downloadfile(path):
    return send_from_directory("static/documents/",path, as_attachment=True),200

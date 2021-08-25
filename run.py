from CMS import app

if __name__ == '__main__' :
    app.config['PORT']=5001
    app.run(port=app.config['PORT'])

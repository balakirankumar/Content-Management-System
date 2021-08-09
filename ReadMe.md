# Content Management System(CMS)

### CMS is just like BlogPost but with slight difference is using only by API's

### Download here [project](url) to run locally

### Extract the folder

### Open terminal and move to location you wish

```bash
unzip Content-Management-System-master.zip  -d .
```

### Create virtual environment

```bash
python3 -m venv CMS_ENV
```

### Activate virtual environment by

```bash
source CMS_ENV/bin/activate
```


### move to directory `Content-Management-System-master`
```bash
cd Content-Management-System-master
```

### Install required modules from `Requirements.txt`

```bash
pip install -r requirements.txt
```

Run the application by command

```bash
python run.py
```
1. ### ***GET REQUESTS***
    1. Get all 'Posts' at  
[http://localhost:5000/user/post/all](http://localhost:5000//user/post/all)

   2. Search Post by `Postid` at   
      [http://localhost:5000/user/post/searchbyid/1](http://localhost:5000/user/post/searchbyid/1)

   3. Search Post by `Author` at                            
 [http://localhost:5000/user/post/searchbyauthor/fullname](http://localhost:5000/user/post/searchbyauthor/fullname)

   4. Search Post by `Title` at                                
 [http://localhost:5000/user/posts/searchbytitle/title](http://localhost:5000/user/posts/searchbytitle/title)  

   5. Search Post by `Tag` at                                     
 [http://localhost:5000/user/posts/searchbytags/tag](http://localhost:5000/user/posts/searchbytags/tag)

   6. Download file attached to post with document url [http://localhost:5000/user/post/document/download/<string:filename>](http://localhost:5000/user/post/document/download/<string:filename>)


2. ### ***POST REQUESTS***

   1. Add a Post by authorizing  
[http://localhost:5000/user/post/addpost](http://localhost:5000/user/post/addpost)

   2. Register `User` using   
[http://localhost:5000/user/register](http://localhost:5000/user/register)


3. ### ***PUT REQUESTS***
   1. Update Post using `Postid` by authorizing                 
    [http://localhost:5000/user/post/updatepost/<int:id>](http://localhost:5000/user/post/updatepost/<int:id>)


   2. Upload file using `Postid` by authorizing using           
    [http://localhost:5000/user/post/uploadfile/<int:id>](http://localhost:5000/user/post/uploadfile/<int:id>)

4. ### ***DELETE REQUEST***

    1. Delete post with `Postid` by authorizing using               
        [http://localhost:5000/user/post/delete/<int:id>](http://localhost:5000/user/post/delete/<int:id>)



#### Json Schemas for
1.  User Registration

       ```json
       {
           "email" : "String: email",
           "password" : "String: password",
           "fullname" :"String: fullname",
           "phonenumber":"Integer: phonenumber ",
           "pincode" : "Integer: pincode",
           "address" :"String: address",
           "city" :"String: city",
           "state" :"String: state",
           "country" :"String: country",
       }
      ```
2.  Adding Post
      
     should add only form data(-F) in curl or postman(i.e json data as a string ). 

       ```Json
       {
            'data' ='{"title" :"Testing @ form data","body" :"Have an idea uploading file and data at atime","summary": "Tesing an someone try","tags":["#Testing","#Idea"]}'
           'document' ="type of [jpg, jpeg, pdf]"
       }
      ```

3.  Update Post's details
       ```Json
       {
           "title" :"String :title",
           "body" :"String :body",
           "summary": "String :summary"
           "tags" :"list:[tags]"
       }
       ```


4.   Update Post's file

        ```Json
        {  
            "file" : type(['pdf', 'jpg']
        }
      ```
5.    Delete Requires no Schema


#### Tree Structure

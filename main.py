from fastapi import FastAPI
import json 
import sys
import uuid
import uvicorn

app = FastAPI(title="Rahmoon Topics API Server", description="Free API for Topics and Posts")

f1= open('data/topics.json')
topics= json.load(f1)
f1.close()

f2= open('data/posts.json')
posts= json.load(f2)
f2.close()



def serialize_topics():
    f= open('data/topics.json','w')
    json.dump(topics,f)
    f.close()
    
def serialize_posts():
    f= open('data/posts.json','w')
    json.dump(posts,f)
    f.close()

#----------------------------FROM here Topics Endpoints -------------------------------


@app.get("/get/topics",tags=["Topics Endpoints"]) 
def readAllTopics():
    return topics

#-------------------------------------------
@app.get("/get/topicbyid/{id}",tags=["Topics Endpoints"])
def readOneTopicById(id:str):
    for one in topics:
        if one["id"]==id:
            return one
    return f"Sorry no topic with this id: {id}"

#-------------------------------------------
@app.get("/get/searchtopic/{txt}",tags=["Topics Endpoints"])
def readtopicbyall(txt:str):
    if txt == "*":
        return(topics)
    res=[]
    for x in topics:
        if x["title"].lower().find(txt.lower())>=0:
            res.append(x)
        if x["body"].lower().find(txt.lower())>=0:
            res.append(x)
    return(res)


#-------------------------------------------

@app.post("/post/topics",tags=["Topics Endpoints"])
def createTopic(topic:dict):
    try:
        new_uuid=uuid.uuid4().hex
        topic["id"]= new_uuid
        topics.insert(0,topic)
        serialize_topics()
        return {"status":True,"id":new_uuid}
    except:
        return {"status":False}

#---------------------------------------------------------

@app.delete("/delete/topics/{id}",tags=["Topics Endpoints"])
def deleteTopicById(id:str):
    for one in topics:
        if (one["id"]==id):
            try:
                topics.remove(one)
                serialize_topics()
                return {"status":True,"message":"Deletted Succesfully"}
            except:
                return {"status":False,"message":"Server Error"}
    return {"status":False,"message":"Not Found"}
#----------------------------------------------------

@app.put("/put/topics",tags=["Topics Endpoints"])
def updateTopic(topic:dict):
    idx=0
    for one in topics:
        if one["id"] ==topic["id"]:
            try:
                topics.insert(idx,topic)
                topics.remove(one)
                serialize_topics()
                return {"status":True,"message":"Updated Succesfully"}
            except:
                return {"status":False,"message":"Server Error"}
        idx+=1
    return {"status":False,"message":"Not Found"}


#----------------------------FROM here Posts Endpoints -------------------------------

@app.get("/get/posts",tags=["Posts Endpoints"]) 
def readAllPosts():
    return posts
# ==================================================================================================
@app.get("/get/searchpost/{txt}",tags=["Posts Endpoints"])
def search(txt:str):
    if txt=='*':
        return posts

    result=[]
    for x in posts:
        if x["user"].lower().find(txt.lower())>=0:
            result.append(x)
        elif x["content"].lower().find(txt.lower())>=0:
            result.append(x)    
        elif x["title"].lower().find(txt.lower())>=0:
            result.append(x)
    return(result)
# ===========================================================================
@app.get("/get/postbyid",tags=["Posts Endpoints"])
def readpostsbyid(id:str):
    for x in posts:
        if x["id"]==id:
            return (x)
# ========================================================================
@app.post("/create/post",tags=["Posts Endpoints"])
def createpost(post:dict):
        new_uuid=uuid.uuid4().hex
        post["id"]= new_uuid
        posts.insert(0,post)
        serialize_posts()
        return {"status":True, "id":new_uuid}

# ==============================================================================================
@app.delete("/delete/post/{id}",tags=["Posts Endpoints"])
def deletepost(id:str):
    for x in posts:
        if x["id"]==id:
            try:
                posts.remove(x)
                serialize_posts()
                return {"status":True,"Message":"deleted succesfully"}
            except:
                {"status":False,"message":"Server Error"}
    return{"status":False,"message":"Not Found"}
# =====================================================================================
@app.put("/update/post",tags=["Posts Endpoints"])
def updatepost(post:dict):
    idn=0
    for q in posts:
        if q["id"] ==post["id"]:
            try:
                posts.insert(idn,post)
                posts.remove(q)
                serialize_posts()
                return{"status":True,"message":"Updated Succesfully"}
            except:
                return {"status":False,"message":"Server Error"}
        idn+=1
    return {"status":False,"message":"Not Found"}






#--------------Running The App-------------------
if __name__=='__main__':
    uvicorn.run('main:app',host='0.0.0.0',port=88, reload=True)

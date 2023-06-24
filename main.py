from fastapi import FastAPI


app = FastAPI(title="Rahmoon Topics API Server")


topics:list[dict] = list([
        {"id":1,"title":"Topic 1", "body":"slkjs skjskjs skjsks kjs"},
        {"id":2,"title":"Topic 2", "body":"slkjs skjskjs skjsks kjs"},
        {"id":3,"title":"Topic 3", "body":"slkjs skjskjs skjsks kjs"},
        {"id":4,"title":"Topic 4", "body":"slkjs skjskjs skjsks kjs"},
        {"id":5,"title":"Topic 5", "body":"slkjs skjskjs skjsks kjs"},
        {"id":6,"title":"Topic 6", "body":"slkjs skjskjs skjsks kjs"}
    ])

#=================================================

@app.get("/get/topics") # End point posts
def readAllTopics():
    return topics

#-------------------------------------------
@app.get("/get/topicbyid/{id}")
def readOneTopicById(id:int):
    for one in topics:
        if one["id"]==id:
            return one
    
    return f"Sorry no topic with this id: {id}"

#-------------------------------------------
@app.get("/get/topicbytitle/{title}")
def readOneTopicByTitle(title:str):
    for x in topics:
        if x["title"].lower()==title.lower():
            return x
    
    return f"Sorry no topic with this title: {title}"

#-------------------------------------------




@app.post("/post/topics")
def createTopic(topic:dict):
    topics.append(topic)
    return topics

#---------------------------------------------------------

@app.delete("/delete/topics/{id}")
def deleteTopicById(id:int):
    for one in topics:
        if (one["id"]==id):
            topics.remove(one)
            return topics
    
#----------------------------------------------------

@app.put("/put/topics")
def updateTopic(topic:dict):
    idx=0
    for one in topics:
        if one["id"] ==topic["id"]:
            topics.insert(idx,topic)
            topics.remove(one)
            return topics
        idx+=1


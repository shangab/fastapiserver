from fastapi import FastAPI
from pydantic import BaseModel

#tes of push

app = FastAPI(title="Rahmoon Server")


class Topic(BaseModel):
    id:int
    title:str
    body:str


topics= list([
        {"id":1,"title":"Topic 1", "body":"slkjs skjskjs skjsks kjs"},
        {"id":2,"title":"Topic 2", "body":"slkjs skjskjs skjsks kjs"},
        {"id":3,"title":"Topic 3", "body":"slkjs skjskjs skjsks kjs"}
    ])

@app.get("/") # Root end point
async def root():
    return {"message": "Hello World"}
#=================================================

@app.get("/topics") # End point posts
def posts():
    return topics

@app.post("/topics")
def createTopic(topic:Topic):
    topics.append(topic)
    return topics

@app.delete("/topics/{id}")
def deleteTopicById(id:int):

    for topic in topics:
        if (topic["id"]==id):
            topics.remove(topic)
            break
    
    return topics


@app.put("/topics")
def updateTopic(topic:Topic):
    
    for one in topics:
        if one["id"]==topic["id"]:
            topics.remove(one)
            topics.append(topic)
            break
    
    topics
    

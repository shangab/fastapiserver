topics= list([
        {"id":1,"title":"Topic 1", "body":"slkjs skjskjs skjsks kjs"},
        {"id":2,"title":"Topic 2", "body":"slkjs skjskjs skjsks kjs"},
        {"id":3,"title":"Topic 3", "body":"slkjs skjskjs skjsks kjs"}
    ])


idx=0
for one in topics:
    if one["id"]==2:
        topics.remove(one)
        topics.insert(idx, {"id":2,"title":"aaaaaaaaTopic 2", "body":"aaaaaaaaslkjs skjskjs skjsks kjs"})
        break
    idx=idx+1

print(topics)
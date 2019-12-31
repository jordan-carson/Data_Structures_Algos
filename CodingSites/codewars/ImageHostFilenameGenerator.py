import uuid

def generateName():
    return str(uuid.uuid4())[:6]


print(generateName())
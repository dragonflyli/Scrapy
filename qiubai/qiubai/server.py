import pymongo
from flask import Flask, render_template
from settings import MONGO_URI, MONGO_DATABASE

app = Flask(__name__)

@app.route('/')
def hello():
    client = pymongo.MongoClient(MONGO_URI)
    db = client[MONGO_DATABASE]
    jokes = db["QiubaiItem"].find()
    client.close()
    return render_template("qiubai_index.html", p_jokes=jokes)

if __name__ == "__main__":
    app.run(host = '0.0.0.0')

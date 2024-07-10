from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return {"message":"Hello world (Python app) with Docker"}

app.run()


# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def index():
#   return 'Hello World Docker!'

# if __name__ == '__main__':
#   #app.run()
#   app.run(host="0.0.0.0", port=5000, debug=True)



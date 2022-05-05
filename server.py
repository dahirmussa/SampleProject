from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
    
    
@app.route("/page2")
def page2():
    return "<p>Hello this is the second page</p>"
    
    
    
@app.route("/page3")
def page3():
    return "<p>Hello this is the third page</p>"
    


#example 6661    
@app.route("/getNumber")
def page4():
    return "10"

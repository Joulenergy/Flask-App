from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    # name = request.args.get("name")
    # return render_template('index.html', username=name)
    # but usually people just name=name and the first name is referring to the name we will use in the html
    return render_template("index.html")

@app.route("/greet")
def greet():
    name = request.args.get("name") 
    # doing "name", "world" doesn't work to prevent hello, [blank] from happening
    # since submit with name field empty will still have the /greet?name=
    # and will not just be /greet
    return render_template("greet.html", name=name)

if __name__ == "__main__":
    app.run(debug=True)
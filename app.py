from flask import Flask,render_template,request,url_for,redirect

app=Flask(__name__)


@app.route('/')
def main_page():
    return render_template("index2.html")
    
@app.route("/register")
def register():
    print(request.method)
    return render_template("register.html")
    
    
@app.route("/stats")
def stats():
    return render_template("stats.html")

@app.route("/reporter")
def reporter():
    return render_template("reporter.html")


@app.route("/done")
def done():
    return render_template("done.html")
@app.route("/contact")
def contact():
    return render_template("contact.html")

    


if __name__=="__main__":
    app.run(debug=True,port=8000)
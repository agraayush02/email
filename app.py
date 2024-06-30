from flask import Flask,render_template,request
import pickle

app = Flask(__name__)


pipe = pickle.load(open("Naive_model.pkl","rb"))

@app.route('/', methods=["GET","POST"])
def main_function():
    if request.method == "POST":
        text = request.form
        # print(text)
        emails = text['email']
        print(emails)
        
        list_email = [emails]
        # print(list_email)
        output = pipe.predict(list_email)[0]
        print(output)


        return render_template("show.html", prediction = output)
    
    else:
        return render_template("index.html")


if __name__ == '__main__':
    # The `app.run(debug=False)` statement is used to run the Flask application. When `debug` is set
    # to `False`, it means that the Flask application will not run in debug mode. Debug mode is
    # typically used during development to provide additional information and features for debugging,
    # but it is recommended to set it to `False` when deploying the application in a production
    # environment for security and performance reasons.
    app.run(debug=False)
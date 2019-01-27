from flask import Flask, request
from caesar import rotate_string
app = Flask(__name__)
app.config['DEBUG'] = True
form = """
<!doctype html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form methods="post">
            <div>
                <label for="rot">Rotate by:</label>
                <input id="rot"type="text" name="rot" value="0">
            </div>
            <textarea type="text" name="text">{0}</textarea>
            <br>
            <input id="text"type="submit" value="Submit Query">
        </form>
    </body>
</html>
"""
@app.route("/")
def index():
    return form.format("")
@app.route("/", methods=['POST'])

def encrypt():
    y = int(request.form['rot'])
    x = request.form['text']
    encrypt = rotate_string(x, y)
    print (encrypt)
    return form.format(encrypt)
app.run()
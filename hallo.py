from flask import Flask
from  flask import send_from_directory
app = Flask(__name__)

@app.route('/image/<path:path>')
def image(path):
    return send_from_directory("image",path)



@app.route("/")
def hello_world():
    return """
<a href="/me">
      <img src="/image/emoji-holy-moly.gif" alt="holy moly"
           width="1000" height="480" /><br />
      HTML For Babies
</a>"""
@app.route("/me")
def eden():
    return """<p>Hello, Eden!</p>
<a href="/papa" >
  Click here
</a>"""

@app.route("/papa")
def papa():
    return """<p>Hello, papa!</p>
<a href="/mama" >
  Click here
</a>"""
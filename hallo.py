from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return """<p>Hello, World!</p>
<a href="/me" >
  Click here
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
from SoC import *
from flask import Flask

app = Flask(__name__)

mysoc = SoC()
print(mysoc.boot())
mysoc.run()


@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    hello()
    app.run(host="0.0.0.0")
    # app.run(host="0.0.0.0", port=config.PORT, debug=config.DEBUG_MODE)

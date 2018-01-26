from flask import Flask, request, render_template
from flask import jsonify
import sys
import os
import subprocess

fname = "index.html"

# Rest Server
app = Flask(__name__)
@app.route('/<path:path>')
def static_file(path):
    return app.send_static_file(path)



# Executing Command
def run_cmd(cmd):
    try:
        print(str(cmd))
        return subprocess.check_output(cmd, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as ex:
        print "return code", ex.returncode
        print "cmd execution returned exit status", ex.output.strip()

def main():
    # create a soft link /tmp/data.js to static/data.js
    cpath = os.path.dirname(os.path.abspath(__file__)) + "/static/data.js"
    cmd = ["rm", cpath]
    run_cmd(cmd)
    cmd = ["ln", '-s', '/tmp/data.js', cpath]
    run_cmd(cmd)
    app.run(host="0.0.0.0", port=5000, debug=True)


if __name__ == '__main__':
    main()

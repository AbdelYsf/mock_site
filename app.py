import os
from os.path import abspath, join

from flask import Flask, Response

app = Flask(__name__)


@app.route("/")
def hello():
    return '''
        <html><body>
        <a href="/getFile_1">download 1.</a>
       
        </body></html>
        '''


@app.route("/getFile_1")
def getFile_1():
    root_path = os.path.join(abspath(join(os.getcwd(), os.pardir)), 'mock_site/files')
    path_to_file = os.path.join(root_path, "conciliation_etat.xlsx")
    with open(path_to_file, 'rb') as file:
        data = file.read()

    return Response(
        data,
        headers={"Content-disposition":
                     "attachment; filename=conciliation_etat.xlsx"})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

import os
import time
import argparse
import tempfile
import PyPDF2
import datetime
from reportlab.pdfgen import canvas
from PIL import image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.utils import ImageReader
import time
from flask import Flask, request
#!pip install Flask-RESTful
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'Hello World..!'}
class Multi(Resource):
    def get(self, num):
        return {'result' : num*10}

api.add_resource(HelloWorld, '/')
api.add_resource(Multi, '/multi/<int:num>')

if __name__ == '__main__':
    app.run(debug=True)



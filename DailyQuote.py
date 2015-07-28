#!/usr/bin/env python
from flask import Flask, request, Response,  make_response
from flask.ext import restful
import json
from PyLexa import *
import requests
import json


VERSION = '1.0'
SECRET_KEY = '1234'
app = Flask(__name__)
api = restful.Api(app)


@api.representation('application/json')
def output_json(data, code, headers=None):
    resp = make_response(json.dumps(data), code)
    resp.headers.extend(headers or {})
    return resp

def getdailyquote():
    resp = requests.get('http://api.theysaidso.com/qod')
    data = json.loads(resp.text)
    quote = data['contents']['quotes'][0]['quote']
    return quote

def build_response():
    mysession = SessionAttribute()
    myspeech = OutputSpeech("PlainText", getdailyquote())
    response = Response(outputspeech=myspeech)
    mybody = ResponseBody(session=mysession, response=response)
    return output_json(mybody.parameters, 200)


class AlexaWebService(restful.Resource):
    def post(self):
        json_data = request.json
        response = build_response()
        print json_data
        return response


api.add_resource(AlexaWebService, '/api/quote')


if __name__ == '__main__':
    app.secret_key = SECRET_KEY
    app.run(host='0.0.0.0', debug=True)

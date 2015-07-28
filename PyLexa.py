'''
Alexa Python v1.0
A basic python wrapper for Alexa responses
'''


class SessionAttribute(object):

    def __init__(self, version="1.0"):
        self.version = version
        self.parameters = self._get_parameters()

    def _get_parameters(self):
        obj = {"version": self.version}
        return obj


class OutputSpeech(object):

    def __init__(self, type, text):
        self.type = type
        self.text = text
        self.parameters = self._get_parameters()

    def _get_parameters(self):
        obj = {}
        obj['type'] = self.type
        obj['text'] = self.text
        return obj



class Card(object):

    def __init__(self, type, title, content):
        self.type = type
        self.title = title
        self.content = content

    def _parameters(self):
        obj = {'type': self.type,
               'title': self.title,
               'content': self.content,
               }
        return obj

    def __str__(self):
        return json.dumps(self._parameters())


class Response(object):
    def __init__(self, outputspeech=None, card=None, reprompt=None):
        self.outputspeech = outputspeech
        self.card = card
        self.reprompt = reprompt
        self.parameters = self._get_parameters()

    def _get_parameters(self):
        obj = {"outputSpeech": self.outputspeech._get_parameters()}
        return obj



class ResponseBody(object):
    """
    Class which generates the Alexa response
    """
    def __init__(self, session=None, response=None, end=True):
        self.session = session
        self.response = response
        self.version = "1.0"
        self.end = end
        self.parameters = self._get_parameters()

    def _get_parameters(self):
        obj = {"version": self.version,
               "response": self.response.parameters,
               "shouldEndSession": self.end}
        return obj

    def __repr__(self):
        return json.dumps(self._parameters())


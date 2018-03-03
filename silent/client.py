from .wrapper import Network
import json


class Client:

    def __init__(self, args):
        self._args = args
        self._payload = {}
        self._response = None

    def _api_request(self):
        self._response = Network.post_request(self._payload)

    def run(self):
        self._payload['filename'] = self._args.file

        self._payload['expiry'] = self._args.expiry

        self._api_request()

        print("\n {0}".format(self._response.status_code))
        print(self._response.reason)
        res = json.loads(self._response.text)
        if res['success']:
            print('Your link to share : {0}'.format(res['link']))
            print('Expires in {0}'.format(res['expiry']))
        else:
            print('Upload failed, try again :(')



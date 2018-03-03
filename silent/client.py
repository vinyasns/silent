from .wrapper import Network


class Client:
    FILE_IO_URL = 'https://file.io'
    SET_EXPIRY_URL = '/?expires='

    def __init__(self, args):
        self._args = args
        self._payload = {}
        self._response = None

    def _api_request(self):
        self._response = Network.post_request(self._payload)

    def run(self):
        self._payload['filename'] = self._args.file

        if self._args.expiry:
            self._payload['expiry'] = self._args.expiry

        self._api_request()

        print(self._response)


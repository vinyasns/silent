from clint.textui.progress import Bar as ProgressBar
from requests_toolbelt import MultipartEncoder, MultipartEncoderMonitor

import requests
import magic

FILE_IO_URL = 'https://file.io'
SET_EXPIRY_URL = '/?expires='


class Network:

    @staticmethod
    def _create_callback(encoder):
        encoder_len = encoder.len
        bar = ProgressBar(expected_size=encoder_len, filled_char='*')

        def _callback(monitor):
            bar.show(monitor.bytes_read)

        return _callback

    @staticmethod
    def _create_upload(filename):
        m = magic.Magic(mime=True)
        tt = m.from_file(filename)
        return MultipartEncoder({'file': (filename, open(filename, 'rb'), tt)})

    @staticmethod
    def post_request(payload):
        filename = payload['filename']
        expiry = payload['expiry']
        url = FILE_IO_URL
        if expiry:
            url = url + SET_EXPIRY_URL + expiry
        encoder = Network._create_upload(filename)
        callback = Network._create_callback(encoder)
        monitor = MultipartEncoderMonitor(encoder, callback)
        response = requests.post(url, data=monitor, headers={'Content-Type': monitor.content_type})
        return response

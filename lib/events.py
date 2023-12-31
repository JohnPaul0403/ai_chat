from .extensions import sock
from .gpt_responses import get_gpt4_response

@sock.route('/echo')
def echo(sock):
    while True:
        data = sock.receive()
        response = get_gpt4_response(data)
        sock.send(response)
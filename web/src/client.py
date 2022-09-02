from bottle import route, run

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("../src/debug.log"),
        logging.StreamHandler()
    ]
)


@route('/hello')
def hello():
    logging.info('Hello World!')
    return "Hello World!"


logging.info('start client')
run(host='0.0.0.0', port=8080, debug=True)
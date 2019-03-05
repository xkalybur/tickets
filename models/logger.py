import logging

class Log():
    logger = logging.getLogger(__name__)
    def __init__(self):
        handler = logging.FileHandler(
            '/usr/lib/python3/dist-packages/odoo/addons/tickets/tickets.log','w'
        )
        handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)



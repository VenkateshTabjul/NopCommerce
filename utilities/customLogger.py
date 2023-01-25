import logging


class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename="K:\\VenkateshTabjul\\NopCommerce\\Logs\\NopCommerce.log", encoding='utf-8',
                            format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p')
        # logging.debug('This message should go to the log file')
        # logging.info('So should this')
        # logging.warning('And this, too')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

# lg = LogGen.loggen()
# lg.info("hk")
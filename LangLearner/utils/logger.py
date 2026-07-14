import logging
import os



BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)



LOG_DIR = os.path.join(
    BASE_DIR,
    "logs"
)


LOG_FILE = os.path.join(
    LOG_DIR,
    "app.log"
)



if not os.path.exists(LOG_DIR):

    os.makedirs(LOG_DIR)



logging.basicConfig(

    filename=LOG_FILE,

    level=logging.INFO,

    format=
    "%(asctime)s - %(levelname)s - %(message)s"

)





class Logger:


    @staticmethod
    def info(message):

        logging.info(message)



    @staticmethod
    def warning(message):

        logging.warning(message)




    @staticmethod
    def error(message):

        logging.error(message)




    @staticmethod
    def exception(message):

        logging.exception(message)



    @staticmethod
    def debug(message):

        logging.debug(message)
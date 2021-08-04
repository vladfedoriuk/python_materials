import logging
import datetime

"""
The defined levels, in order of increasing severity, are the following:

DEBUG
INFO
WARNING
ERROR
CRITICAL
"""

"""
The most commonly used classes defined in the logging module are the following:

Logger: This is the class whose objects will be used in the application code directly to call the functions.

LogRecord: Loggers automatically create LogRecord objects that have all the information related 
to the event being logged, like the name of the logger, the function, the line number, the message, and more.

Handler: Handlers send the LogRecord to the required output destination, like the console or a file. 
Handler is a base for subclasses like StreamHandler, FileHandler, SMTPHandler, HTTPHandler, and more. 
These subclasses send the logging outputs to corresponding destinations, like sys.stdout or a disk file.

Formatter: This is where you specify the format of the output by specifying a string format that lists out 
the attributes that the output should contain.
"""


def default_logger():
    """
    Notice that the debug() and info() messages didn’t get logged.
    This is because, by default, the logging module logs the messages
    with a severity level of WARNING or above.
    :return: None
    """
    logging.debug("this is a debug message")
    logging.info("this is an info message")
    logging.warning("This is a warning message")
    logging.error("This is an error message")
    logging.critical("This is a critical message")


def logging_basic_config():
    """
    Some of the commonly used parameters for basicConfig() are the following:

    level: The root logger will be set to the specified severity level.
    filename: This specifies the file.
    filemode: If filename is given, the file is opened in this mode. The default is a, which means append.
    format: This is the format of the log message.
    :return: None
    """
    logging.basicConfig(
        level=logging.DEBUG,
        filename="example.log",
        filemode="w",
        format=" %(asctime)s: %(name)s - %(levelname)s - %(message)s",
        datefmt="%d-%b-%y %H:%M:%S",
    )
    logging.debug("this will get printed")
    logging.warning(msg="something else")
    logging.info("admin logged in")

    """
    It should be noted that calling basicConfig() to configure 
    the root logger works only if the root logger has not been configured before. 
    Basically, this function can only be called once.
    """
    # %(asctime)s adds the time of creation of the LogRecord.


def formatting():
    name = "Vlad"
    logging.debug("%s logged in", name)
    logging.error(f"{name} raised an error")
    try:
        2 / 0
    except ZeroDivisionError as e:
        logging.error("Exception occurred", exc_info=True)
        logging.exception(
            "Exception occurred"
        )  # should be only called in the exception handler
        logging.critical("Exception occurred", exc_info=True)


def logger_object():
    """
    Multiple calls to getLogger() with the same name will return a reference to the same Logger object,
     which saves us from passing the logger objects to every part where it’s needed. Here’s an example:
    :return:
    """
    my_logger = logging.getLogger(__name__)
    my_logger.error("log from my_logger")

    """
    “It is recommended that we use module-level loggers by passing __name__ as 
    the name parameter to getLogger() to create a logger object as the name of the logger itself would tell us 
    from where the events are being logged. __name__ is a special built-in variable in Python 
    which evaluates to the name of the current module.”
    """


def logger_handlers():
    """
    This is useful if you want to set multiple handlers for the same logger but want
    different severity levels for each of them.
    """

    logger = logging.getLogger(__name__)

    # create handlers
    c_handler = logging.StreamHandler()  # for console logging
    f_handler = logging.FileHandler("example.log", mode="w")  # for file logging
    c_handler.setLevel(logging.WARNING)
    f_handler.setLevel(logging.ERROR)

    # create formatters for handlers
    c_format = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
    f_format = logging.Formatter(
        "%(asctime)s - %(name)s -  %(levelname)s - %(message)s",
        datefmt="%d-%b-%y %H:%M:%S",
    )
    c_handler.setFormatter(c_format)
    f_handler.setFormatter(f_format)

    # add handlers to the logger
    logger.addHandler(f_handler)
    logger.addHandler(c_handler)

    logger.warning("This is a warning ")
    logger.error("This is an error ")

    """
    Here, logger.warning() is creating a LogRecord that holds all 
    the information of the event and passing it to 
    all the Handlers that it has: c_handler and f_handler.
    
    c_handler is a StreamHandler with level WARNING and takes the info from 
    the LogRecord to generate an output in the format specified and prints it to the console. 
    f_handler is a FileHandler with level ERROR, and it ignores this LogRecord as its level is WARNING.
    
    When logger.error() is called, c_handler behaves exactly as before, 
    and f_handler gets a LogRecord at the level of ERROR, so it proceeds to generate an output just like c_handler, 
    but instead of printing it to console, it writes it to the specified file
    """


def file_configuration():
    import logging.config

    logging.config.fileConfig("file.conf", disable_existing_loggers=False)
    logger = logging.getLogger("sampleLogger")
    logger.debug("this is a debug message from a file_conf")
    logger.error("this is an error message from a file_conf")


if __name__ == "__main__":
    # logging_basic_config()  # must be called first
    # default_logger()
    # formatting()
    # logger_object()
    # logger_handlers()
    file_configuration()

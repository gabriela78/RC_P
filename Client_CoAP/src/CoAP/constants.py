from enum import Enum



# For a new Confirmable message, the initial timeout is set
#  to a random duration (often not an integral number of seconds)
#  between ACK_TIMEOUT and (ACK_TIMEOUT * ACK_RANDOM_FACTOR)
#  and the retransmission counter is set to 0

class Param(Enum):
    DEFAULT_VERSION = 1
    ACK_TIMEOUT = 2
    ACK_RANDOM_FACTOR  = 1.5
    MAX_RETRANSMIT = 4
    RETRANSMISSION_COUNTER=0

TYPE_CON_MSG=0
TYPE_NON_CON_MSG = 1
TYPE_ACK = 2
TYPE_RST = 3

# class Type(Enum):
#     CON_MSG = 0
#     NON_CON_MSG = 1
#     ACK = 2
#     RST = 3

CODE_EMPTY = 0
CODE_GET = 1
CODE_POST = 2
CODE_SEARCH = 8

# class Code(Enum):
#     EMPTY = 0
#     GET = 1
#     POST = 2
#     SEARCH = 8

CLASS_METHOD = 0
CLASS_SUCCESS = 1
CLASS_CLIENT_ERROR = 4
CLASS_SERVER_ERROR = 5

# class Class(Enum):
#     METHOD = 0
#     SUCCESS = 1
#     CLIENT_ERROR = 4
#     SERVER_ERROR = 5
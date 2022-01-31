# ERROR CODES
ERRCODE1 = 'FAILED TO INITIALIZE API'
ERRCODE2 = 'API NOT ACTIVE; ENABLE API ON CONTROLLER'
ERRCODE3 = 'INVALID API COMMAND'
ERRCODE4 = 'UNABLE TO PARSE COMMAND'
ERRCODE5 = 'AUTHENTICATION FAILURE'
ERRCODE6 = 'UNKNOWN COMMAND; CHECK COMMAND SYNTAX'

# XML DICT DEFINITIONS
NETBOX = 'NETBOX-API'
SESSION = '@sessionid'
CMD = 'COMMAND'
CMDNAME = '@name'
NUM = '@num'
PRM = 'PARAMS'

# COMMAND NAMES
ADDUSR = 'AddPerson'
DELUSR = 'RemovePerson'
MODUSR = 'ModifyPerson'

# NAMES
FIRST = 'FIRSTNAME'
LAST = 'LASTNAME'

# ACCESS LEVELS
ACCLVL = 'ACCESSLEVEL'
ACCLVLS = 'ACCESSLEVELS'

# PORTAL CONTROL
PORTAL = 'PORTALKEY'
UNLOCK = 'UnlockPortal'
LOCK = 'LockPortal'
MOMUNLOCK = 'MomentaryUnlockPortal'


def login(username, password):
    account = {CMDNAME: 'Login', NUM: '1', PRM: {'USERNAME': username, 'PASSWORD': password}}
    return account


def user(first=str, last=str, **kwargs):
    usr = {FIRST: first, LAST: last}
    if kwargs:
        if kwargs['accesslevel'] is not None:
            usr[ACCLVL] = kwargs['accesslevel']
    return usr


def modify_user(command, usr):
    return {CMDNAME: command, NUM: '1', PRM: usr}


def getportal(key):
    return {PORTAL: str(key)}


def momentary(key):
    return {CMDNAME: MOMUNLOCK, NUM: '1', PRM: key}

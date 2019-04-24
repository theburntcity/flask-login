from configparser import ConfigParser

 
def dbconfig(filename=r'backend\dbandsupport.ini', section='postgresql'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)
    # retrieve flask section and get all parameters for connecting to the db
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db 
 
def skconfig(filename=r'backend\dbandsupport.ini', section='flask'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)
    # retrieve flask section and look for skey
    skey = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            skey[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return skey 

from dataclasses import dataclass
from backend.config import skconfig
from backend.dbstuff import ownerconnect


# get the skey
thekey = skconfig()
skey = thekey.get('secret_key')

# get owner info
info = ownerconnect()

# the reason for frozen set to true is to keep everything locked down.
@dataclass(frozen=True)
class Access():
    user = str
    pwrd = str

Access.user = info[1]
Access.pwrd = info[2] 

# print(Access.user, Access.pwrd)
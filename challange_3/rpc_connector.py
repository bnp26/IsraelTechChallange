import rpyc
from rpyc.utils.server import ThreadedServer

conn = rpyc.classic.connect("localhost")    # use default TCP port (18812)


print conn

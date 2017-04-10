import pyjsonrpc

http_client = pyjsonrpc.HttpClient(
    url = "http://hack.israeltechallenge.com:8000",
    username = "ITC"
)

#^[k-n3-5#]{2,4}$
#klmn345#
options = "klnb345#"
	for

print http_client.call("help")
print http_client.call("ping")
username = 'ITC'
password = '123456'
print http_client.call("login", username, password)

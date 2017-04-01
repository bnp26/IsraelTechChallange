from qam.qam_proxy import QAMProxy, QAMMethodNotFoundException, QAMException

qam_server = QAMProxy(hostname="http://hack.israeltechallenge.com", port=8000, username='ITC', password='ITC', vhost='/', server_id='qamserver', client_id='qamproxy')

result = qam_proxy.my_instance.help()

print result

qam_server.close()


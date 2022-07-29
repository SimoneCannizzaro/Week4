import http.client

host = input("Inserire IP del sistema target : ")
port = input("Inserire la porta del sistema target (default:80):")

if(port == ""):
    port = 80

try:
    connection = http.client.HTTPConnection(host, port)
    connection.request('OPTIONS', 'http://192.168.50.101/phpMyAdmin/phpMyAdmin.html')
    response = connection.getresponse()
    print("I metodi abilitati sono: ", response.getheader('allow'))
    connection.close()

except ConnectionRefusedError:
    print("Connessione fallita")




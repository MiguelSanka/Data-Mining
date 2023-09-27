from urllib import request

# Definimos la URL del archivo a descargar
remote_url = 'https://drive.google.com/u/0/uc?id=1cswtjwdg_YEO0jR0kV1nSAMQABTU-rRy&export=download'

# Definimos el nombre del archivo local a guardar
local_file = 'crimen_nac.csv' 

# Se realiza la descarga y se guarda el archivo de manera local
request.urlretrieve(remote_url, local_file)
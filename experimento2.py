from zeep import Client
from math import gcd

# URL do serviço web
wsdl_url = "http://localhost:3000/mdc?wsdl"

# Criar um cliente para o serviço web
client = Client(wsdl=wsdl_url)

# Definir as dimensões da imagem (x e y)
x = 800
y = 600

# Fazer a chamada ao método CalculateMDC do serviço web
response = client.service.CalculateMDC(x=x, y=y)

# Extrair o MDC da resposta
mdc = response.MDC

# Calcular o Aspect Ratio da imagem
aspect_ratio_x = x / mdc
aspect_ratio_y = y / mdc

print("MDC da imagem:", mdc)
print("Aspect Ratio da imagem:", aspect_ratio_x, ":", aspect_ratio_y)

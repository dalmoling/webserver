from zeep import Client

# URL do serviço web
wsdl_url = "http://www.dneonline.com/calculator.asmx?WSDL"

# Criar um cliente para o serviço web
client = Client(wsdl=wsdl_url)

# Exemplo de chamada de método (por exemplo, Add)
result = client.service.Add(intA=5, intB=3)
print("Resultado da adição:", result)

# Exemplo de chamada de outro método (por exemplo, Subtract)
result = client.service.Subtract(intA=5, intB=3)
print("Resultado da subtração:", result)

# Exemplo de chamada de outro método (por exemplo, Multiply)
result = client.service.Multiply(intA=5, intB=3)
print("Resultado da multiplicação:", result)

# Exemplo de chamada de outro método (por exemplo, Divide)
result = client.service.Divide(intA=10, intB=2)
print("Resultado da divisão:", result)

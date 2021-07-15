def saida():
    print("Necessidade de Transferência Armazém para CO\nProduto	QtCO	QtMin	QtVendas	Estq.após	Necess.	Transf. de\n\nVendas			Arm p/ CO")
    

def toArray(arquivo):
    lista=[]
    for linha in arquivo:
        valor=linha.split(";")
        x=len(valor)-1
        if "\n" in valor[x]:
            valor[x]=valor[x].replace("\n","")
        lista.append(valor)
    return lista
def vendasCanais(sales):
    canal={1:0,2:0,3:0,4:0}
    for dado in sales:
        if dado[2]=="100" or dado[2]=="102":
            num=int(dado[3])
            canal[num]=canal.get(num)+int(dado[1])
    return canal
def mostrarCanais(canal):
    print("Quantidades de Vendas por canal\n")
    print("1 - Representantes		{}".format(canal.get(1)))
    print("2 - Website			{}".format(canal.get(2)))
    print("3 - App móvel Android		{}".format(canal.get(3)))
    print("4 - App móvel iPhone		{}".format(canal.get(4)))
def main():
    produtos=open("c1_produtos.txt","r")
    produtos1=open("")
    vendas=open("c1_vendas.txt","r")
    sales=toArray(vendas)
    products=toArray(produtos)
    produtos.close()
    vendas.close()
    canal=vendasCanais(sales)
    mostrarCanais(canal)
main()
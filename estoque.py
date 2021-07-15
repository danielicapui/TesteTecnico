import sys,os,glob,shutil
def saida():
    print("Necessidade de Transferência Armazém para CO\nProduto	QtCO	QtMin	QtVendas	Estq.após	Necess.	Transf. de\n\nVendas			Arm p/ CO")
def handle_args(args):
    return args.replace("..",".")
def handle_file(file):
    return os.path.dirname(file)
def handle_path(txt):
    return os.path.abspath(txt)
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
def salvarCanais(canal,file):
    filename=handle_file(file)+"/TOTCANAIS.txt"
    arquivo=open(filename,"w")
    arquivo.write("Quantidades de Vendas por canal\n\n")
    arquivo.write("1 - Representantes		{}\n".format(canal.get(1)))
    arquivo.write("2 - Website			{}\n".format(canal.get(2)))
    arquivo.write("3 - App móvel Android		{}\n".format(canal.get(3)))
    arquivo.write("4 - App móvel iPhone		{}\n".format(canal.get(4)))
    arquivo.close()
    return True
def loadData(file):
    arquivo=open(file,"r")
    data=toArray(arquivo)
    arquivo.close()
    return data
def main(file,file1):
    products=loadData(file1)
    sales=loadData(file)
    canal=vendasCanais(sales)
    mostrarCanais(canal)
    salvarCanais(canal,file)
    return 0
if __name__=="__main__":
    txt=handle_args(sys.argv[1])
    txt1=handle_args(sys.argv[2])
    file=handle_path(txt)
    file1=handle_path(txt1)
    main(file,file1)
from PyQt5 import uic,QtWidgets

def funcao_principal():
    linha1 = formulario.lineEdit.text()
    linha2 = formulario.lineEdit_2.text()
    linha3 = formulario.lineEdit_3.text()

    categoria =""


    if formulario.radioButton.isChecked(): 
        print("Categoria Fruta foi selecionado")
        categoria = "Fruta"
    elif formulario.radioButton_2.isChecked(): 
        print("Categoria Bebidas foi selecionado")
        categoria = "Bebidas"
    else :
        print("Categoria Lanches foi selecionado")
        categoria = "Lanche"
        
    print("Codigo",linha1) 
    print("Descricao",linha2)
    print("Preco",linha3)

app=QtWidgets.QApplication([])
formulario=uic.loadUi("formulario.ui")
formulario.pushButton.clicked.connect(funcao_principal)

formulario.show()
app.exec()



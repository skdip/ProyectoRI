class HTMLReader:
    def __init__(self, docName):
        self.fileName = './Coleccion/' + docName

        # Se tiene que cambiar el tipo de encoding del archivo y
        # se tiene que ignorar ciertos errores de caracteres que dice que no existen.
        self.file = open(self.fileName, encoding='utf-8-sig', errors='ignore')



    def printHtml(self):
        print(self.file.read())
class Save():
    def __init__(self,gulag,tensao,content):
        self.gulag = gulag
        self.tensao = tensao
        self.content = content
        
    def __repr__(self):
        print(self.gulag)
        print("Tensão: ", self.tensao)
        print("Contentamento: ", self.content)
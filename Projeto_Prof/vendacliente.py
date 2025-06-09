import json

class VandaCliente:
    compras = []     # atributo de classe / estático - Não tem instância
    @classmethod
    def inserir(cls,email, carinho):
        for i in carinho:
            a = email
            a = a + carinho[i]
            cls.compras.append(a)
            cls.salvar() 
    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.compras
    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for obj in cls.carinho:
            if obj.id == id: return obj
        return None
    @classmethod
    def excluir(cls, obj):
        x = cls.listar_id(obj.email)
        if x != None: 
            cls.compras.remove(x)
            cls.salvar()
    @classmethod
    def abrir(cls):
        cls.compras = [] 
        try:   
            with open("vendacliente.json", mode="r") as arquivo:
                s = json.load(arquivo)
                for dic in s: 
                    obj = Cliente(dic["email"]
                    obj = VendaItem(dic[]
                    cls.compras.append(obj)
        except FileNotFoundError:
            pass            
    @classmethod
    def salvar(cls):
        with open("vendaitens.json", mode="w") as arquivo:
            json.dump(cls.compras, arquivo, default = vars)
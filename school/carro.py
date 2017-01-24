class Carro:
    
    #   Atributos de Classe
    #   ** Atributos de classe são variaveis declaradas em escopo global, Dizem respeito a informaçôes comum para todos objetos.
    #   ** Não precisa do objeto para existir, mas assim que o objeto é criado ele pode acessar esses atributos.
    pneus = 4
    farois = 2
    destino = "Revendedora"

    #   Métodos Contrutores
    #   ** métodos de construtores inicializam os paramêtros da classe e os constroi.
    #   ** na criação de um objeto é preciso passar como paramêtros as informações da classe.
    def __init__(self, marca, nome, ano):
        
        #   atributos de objetos
        self.marca = marca
        self.nome = nome
        self.ano = ano
    
    #   Métodos de Instancia
    #   ** métodos que tem acesso aos atributos da classe apenas com o #self#
    #   ## pode ser facilmente acessivel a qualquer atributo da classe.

    def drive(self):

        print(self.marca, self.nome + " Está andando")
        
    def stop(self):

        print(self.marca, self.nome + " Está parado")

    #   Métodos Estáticos
    #   ** métodos estáticos não tem acessos aos atributos da classe ou de outros métodos.
    #   ** esse acesso pode ser feito passando como paramêtro o atributo que quer ter acesso.

    #   **método estático sem paramêtro e sem acesso aos atributos da classe Carro().
    #   **mesmo sendo um método da classe Carro() não tem acesso a seus atributos.
    @staticmethod
    def mensagem():

        print("Sua mensagem é essa!")
    
    #   ** método estático com paramêtro e com acesso aos atributos da classe Carro().
    #   ** é um método da classe Carro() e só tem acesso a seus atributos por meio dos paramêtros passado.
    @staticmethod
    def situacao(pneus):

        print("Este veiculo está com ", pneus, "pneus novos!")

    #   Métodos da Classe
    #   ** métodos da classe tem acesso apenas a atributos da classe, ou seja aqueles atributos declarados de forma global
    #   ** assim como métodos estáticos precisa da notação @classmethod para identificar que é um metodo de classe.
    @classmethod
    def show(cls):

        print(cls.destino)

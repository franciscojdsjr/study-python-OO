class Celular:
    marca = 'Nokia'
    modelo = 'Tijolão'
    cor = 'Azul'
    tem_camera = False
    bateria = 'infinita'

    def fazer_ligacao(self):
        print('Fazendo ligação...')
    
    def jogar_cobrinha(self):
        print('Jogando cobrinha...')
    
    def despertador(self):
        print('Despertando...')
    
celular = Celular()

celular.despertador()
celular.fazer_ligacao()
celular.jogar_cobrinha()
print(celular.marca)
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
    
    def calcular(self,v1,v2):
        return f'Calculando...\nO Resultado é: {v1 + v2}'
    
celular = Celular()

celular.despertador()
celular.fazer_ligacao()
celular.jogar_cobrinha()
print(celular.marca)
print('-' * 100)

calculado = celular.calcular(15,5)
print(calculado)
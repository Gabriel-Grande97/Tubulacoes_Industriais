'''Perda de carga
A tubulação sofre ramificação, uma única vir 3, logo seus diâmetros são reduzidos em certo ponto
'''
import numpy as np 
import matplotlib.pyplot as plt

# Dados de geometria - SI [m]
altura_inicial  = 0.85
altura_final    = 13.7

#Estado do fluido - através da estipulação de bomba(SI)
#tem-se apenas um valor de vazão e pressão final pois deve ser igual nas 3 tubulações ramificadas e 3 reservatórios
vazao_inicial    = 0.056
#vazao_final      =

pressao_bomba  =   400000       #[Pa]
pressao_reservatorio    = 70300 #[Pa] 

#Características do fluido
peso_especifico = 9500                  #[N/m³]
viscosidade_cinematica = 1.003*10^(-6)  #[]

#Características do meio [m/s²]
gravidade = 9.8 

# 1º passo - Variáveis arbitrárias iniciais
diametro_estimado = 0.218           # SI [m] 
comprimento_estimado = 2000 # SI [m]
velocidade_inicial = 1.47

# 2º passo - Determinação do comprimento equivalente dos componetes de perda localizada [m]
comprimento_equivalente_1 = 100
comprimento_equivalente_2 = 0
comprimento_equivalente_3 = 0

# 3º passo - Cálculo de energia disponível (multiplica por 3)
energia_disponivel = ((pressao_bomba/peso_especifico) +((velocidade_inicial^2)/(2*gravidade)) 
    + (altura_inicial))
    - 3*((pressao_reservatorio/peso_especifico) +((velocidade_final^2)/(2*gravidade)) 
    + (altura_final))
print("Energia disponível:"energia_disponivel)

# 4º passo - Cálculo da perda de carga (utiliza-se a velocidade média)
velocidade_media = velocidade_inicial-velocidade_final
numero_de_reynolds = (((velocidade_media)/2)*diametro_estimado)/viscosidade_cinematica

fator_de_atrito = 0
if numero_de_reynolds < 2000:
    fator_de_atrito = 64/numero_de_reynolds
    print("Regime laminar")
else:
    print("Regime indefinido ou turbulento")#    f(Re, e_r)

perda_de_carga = fator_de_atrito*(((comprimento estimado + comprimento_equivalente_1 +
    comprimento_equivalente_2 + 
        comprimento_equivalente_3)*(velocidade_media)^2)/2*gravidade*diametro_estimado)

# 5º passo - Balanço de energia
delta_energia = energia_disponivel - perda_de_carga 
print("Variação de energia:"delta_energia)

# 6º passo - Verificar vazão
vazao_nova = 0

vazao_nova = (np.pi*viscosidade_cinematica*(diametro_estimado^2))/4
print(vazao_nova)

if vazao_nova < vazao_inicial:
    print("Escolher novo diametro")
else:
    ("Valor da vazão após perda de carga")
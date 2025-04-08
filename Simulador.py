import numpy as np
import matplotlib.pyplot as plt

# Entradas do usuário
angulo_graus = float(input("Digite o ângulo de lançamento (em graus): "))
velocidade_inicial = float(input("Digite a velocidade inicial (em m/s): "))
coef_arrasto = float(input("Digite o coeficiente de arrasto (ex.: 0.1): "))
massa = float(input("Digite a massa do projétil (em kg): "))
diametro = float(input("Digite o diâmetro do objeto (em metros): "))
tempo_total = float(input("Digite o tempo total de simulação (em segundos): "))

# Constantes
g = 9.81  # aceleração gravitacional em m/s^2
rho_ar = 1.225  # densidade do ar ao nível do mar em kg/m³

# Conversão do ângulo para radianos
angulo = np.radians(angulo_graus)

# Componentes da velocidade inicial
velocidade_x = velocidade_inicial * np.cos(angulo)
velocidade_y = velocidade_inicial * np.sin(angulo)

# Parâmetros de simulação
dt = 0.01  # intervalo de tempo em segundos
area_seccional = np.pi * (diametro / 2)**2  # área de seção transversal em m²

# Condições iniciais
posicao_x = 0
posicao_y = 0

# Listas para armazenar dados
posicoes_x = [posicao_x]
posicoes_y = [posicao_y]
tempos = np.arange(0, tempo_total, dt)

# Função para calcular a força de arrasto com base na área de seção transversal
def forca_arrasto(velocidade_x, velocidade_y, coef_arrasto, area_seccional):
    velocidade = np.sqrt(velocidade_x*2 + velocidade_y*2)
    forca_arrasto_magnitude = 0.5 * coef_arrasto * area_seccional * rho_ar * velocidade**2
    forca_arrasto_x = -forca_arrasto_magnitude * (velocidade_x / velocidade)
    forca_arrasto_y = -forca_arrasto_magnitude * (velocidade_y / velocidade)
    return forca_arrasto_x, forca_arrasto_y

# Simulação do movimento do projétil
for t in tempos:
    # Calcular forças
    forca_arrasto_x, forca_arrasto_y = forca_arrasto(velocidade_x, velocidade_y, coef_arrasto, area_seccional)
    forca_gravidade_y = -massa * g

    # Acelerações
    aceleracao_x = forca_arrasto_x / massa
    aceleracao_y = (forca_gravidade_y + forca_arrasto_y) / massa

    # Atualizar velocidades
    velocidade_x += aceleracao_x * dt
    velocidade_y += aceleracao_y * dt

    # Atualizar posições
    posicao_x += velocidade_x * dt
    posicao_y += velocidade_y * dt

    # Armazenar as novas posições
    posicoes_x.append(posicao_x)
    posicoes_y.append(posicao_y)

    # Parar quando y=0
    if posicao_y < 0:
        break

# Plotar a trajetória do projétil
plt.figure(figsize=(10, 5))
plt.plot(posicoes_x, posicoes_y, label="Trajetória do Projétil")
plt.xlabel("Posição X (m)")
plt.ylabel("Posição Y (m)")
plt.title("Simulação de Lançamento de Projétil com Resistência do Ar e Diâmetro do Objeto")
plt.legend()
plt.grid()
plt.show()

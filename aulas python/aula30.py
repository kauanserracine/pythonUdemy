velocidade = 61
local_carro = 99


RADAR_1 = 60
LOCAL_1 = 100
RANGE = 1

vel_car_pass_r1 = velocidade > RADAR_1
multa = local_carro >= (LOCAL_1 - RANGE) and \
        local_carro <= (LOCAL_1 + RANGE)

if vel_car_pass_r1:
    print("Velocidade do carro passou do radar 1")

if   multa and vel_car_pass_r1:
    print("carro multado em radar 1")
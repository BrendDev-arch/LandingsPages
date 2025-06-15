import random

def calcular_dano(ataques, forca_atacante, toughness_inimigo, salvar, armour_penetration):
    danos = 0

    for i in range(ataques):
        # Rolando um dado para acertar o ataque (simulando 1D6)
        rolagem_acerto = random.randint(1, 6)
        print(f"Ataque {i + 1}: Rolagem de ataque: {rolagem_acerto}")

        # Verifique se o ataque atinge o inimigo (pode adicionar um valor de dificuldade aqui)
        if rolagem_acerto >= 3:  # Exemplo: precisa rolar 3 ou mais para acertar
            # Rolando um dado para determinar se o ataque causa wound
            rolagem_wound = random.randint(1, 6)
            print(f"Ataque {i + 1}: Rolagem de wound: {rolagem_wound}")

            if (forca_atacante >= toughness_inimigo and rolagem_wound >= 2) or (forca_atacante < toughness_inimigo and rolagem_wound >= (5 - toughness_inimigo + forca_atacante)):
                print(f"Ataque {i + 1} causa dano!")
                danos += 1
            if (rolagem_wound < salvar):
                print(f"O ataque do inimigo foi {toughness_inimigo}")
            if (armour_penetration >= rolagem_wound):
                toughness_inimigo-=1
                save = toughness_inimigo
                print(f"O Armour penetration diminui para {save}")
            else:
                print(f"Ataque {i + 1} não causa dano.")
        else:
            print(f"Ataque {i + 1} falha em acertar.")

    print(f"Dano total causado: {danos}")
    return danos

# Exemplo de uso
ataques = 5
forca_atacante = 4
toughness_inimigo = 3
salvar = 4
armour_penetration = 5

calcular_dano(ataques, forca_atacante, toughness_inimigo, salvar, armour_penetration)
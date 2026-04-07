import pygame
import os

pygame.mixer.init()

print("Arquivos detectados no projeto:", os.listdir())

arquivo = "sua_musica.mp3"

if os.path.exists(arquivo):
    pygame.mixer.music.load(arquivo)
    pygame.mixer.music.play()

    print(f"\n--- REPRODUZINDO: {arquivo} ---")

    status = True
    while status:
        print("\n[P] Pausar | [R] Retomar | [S] Sair")
        opcao = input("Escolha uma opção: ").lower()

        if opcao == 'p':
            pygame.mixer.music.pause()
        elif opcao == 'r':
            pygame.mixer.music.unpause()
        elif opcao == 's':
            pygame.mixer.music.stop()
            status = False
        else:
            print("Opção inválida, tenta de novo.")
else:
    print(f"\nERRO: O arquivo '{arquivo}' não foi encontrado.")
    print("Dica: Verifique se o nome está idêntico e se o arquivo está na mesma pasta do script.")
from collections import Counter
import wget
import os
import matplotlib.pyplot as plt


# Verifica se o arquivo existe, se não existir vai até o local desejado e faz o download dele
if os.path.exists("livro.txt"):
    print("Arquivo já existe, e não será baixado.")
else:
    print("Arquivo não existe, baixando...")
    wget.download(
        "https://www.gutenberg.org/files/16429/16429-0.txt", "livro.txt")


# Abre e fecha o arquivo e adiciona todo o livro a variavel texto em letra minuscula
with open("livro.txt", encoding="UTF-8") as arquivo:
    texto = arquivo.read().lower()


filtered_text = "".join(
    [letra for letra in texto if letra.isalpha() or letra == " "])


"""filtered_text = ''
for letra in texto:
    if letra.isalpha() or letra == ' ':
        filtered_text += letra
print(filtered_text)"""


letras = [l for l in filtered_text if l.isalpha()]
frequencia_letras = Counter(letras)


rotulos, valores = zip(*frequencia_letras.most_common(5))
plt.title("Letras que mais aparecem")
plt.bar(rotulos, valores, color="black")
plt.xlabel("letras")
plt.ylabel("Sua frequência")


for i, v in enumerate(valores):
    plt.text(
        i,
        v,
        str(v),
        color="orange",
        fontweight="bold",
        horizontalalignment="center",
        verticalalignment="bottom",
    )

plt.show()

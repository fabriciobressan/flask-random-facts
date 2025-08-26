from deep_translator import GoogleTranslator

print("Digite o arquivo de origem: ")
input_file = input()
print("Digite o arquivo de destino: ")
output_file = input()
translator = GoogleTranslator(source='en', target='pt')

def deve_traduzir(linha):
    return not (linha.strip() == "" or linha.strip().isdigit() or "-->" in linha)

with open(input_file, "r", encoding="utf-8") as entrada, open(output_file, "w", encoding="utf-8") as saida:
    for linha in entrada:
        if deve_traduzir(linha):
            try:
                traduzida = translator.translate(linha.strip())
                saida.write(traduzida + "\n")
            except Exception as e:
                print(f"Erro ao traduzir: {linha.strip()} -> {e}")
                saida.write(linha)
        else:
            saida.write(linha)

# Cidade se começa ou não com "SANTO"

cid = str(input("Em que cidade você nasceu? ")).strip()
print(cid[:5].upper() == 'Santos')

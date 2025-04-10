import json

dados_python = {
    "nome": "Ana",
    "idade": 30,
    "cursos": ["Python", "JSON"],
    "ativo": True,
    "endereco": None
}

# Converter para JSON
json_string = json.dumps(dados_python, ensure_ascii=False, indent=4)
print(json_string)
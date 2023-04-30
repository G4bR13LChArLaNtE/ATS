# Nome: Julio Gabriel Charlante Barbosa Moreira da Silva RA: 2101478

import requests


class Blog:
    def posts():
        endereco = "https://jsonplaceholder.typicode.com/posts"
        response = requests.get(endereco)
        return response.json()

    def post_by_user_id(userId):
        e = f"https://jsonplaceholder.typicode.com/posts/{userId}"
        response = requests.get(e)
        return response.json()


resultado = Blog.post_by_user_id(1)

print(resultado['userId'])
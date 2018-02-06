# projeto_todo_list
Projeto desenvolvido com Python/Django para criar listas de atividades.


## Instalação

1. Faça o clone do projeto:

```bash
$ git clone https://github.com/alisonamerico/projeto_todo_list.git
```

2. Crie um ambiente virtualizado com [virtualenv]() e ative-o:

```bash
$ cd projeto_todo_list
$ python3 -m venv .venv
$ source .venv/bin/activate
```

3. Executando o último comando, deve aparecer dessa forma:

```bash
(.venv)$
```

4. Isso significa que o ambiente foi ativado com sucesso. Agora vamos instalar as dependências:

```bash
(.venv)$ pip install -r requirements.txt
```

5. Configure a instância com o .env:

```bash
(.venv)$ cp contrib/env-sample .env
```

6. Antes executar a aplicação, precisa criar o banco de dados localmente:

```bash
(.venv)$ ./manage.py migrate
```

7. Execute o servidor web local:

```bash
(.venv)$ ./manage.py runserver
```

8. Execute os testes:

```bash
(.venv)$ ./manage.py test

## Dúvidas ou problemas

Em caso de dúvidas ou problemas para configurar e rodar o projeto, crie uma [Issue](https://github.com/alisonamerico/projeto_todo_list/issues) nesse repositório.

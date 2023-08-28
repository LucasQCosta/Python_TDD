# Curso Alura: Python e TDD

## Descrição

Este repositório contém os exercícios e projetos que foram desenvolvidos durante o curso de Python e TDD oferecido pela Alura. O curso aborda os fundamentos da programação em Python, direciona a POO, bem como as melhores práticas de desenvolvimento orientado a testes (TDD).

Utilizado principalmente Pytest para verificar a cobertura do código.

Requisitos
- colorama==0.4.6
- coverage==7.3.0
- exceptiongroup==1.1.3
- iniconfig==2.0.0
- packaging==23.1
- pluggy==1.2.0
- pytest==7.4.0
- pytest-cov==4.1.0
- tomli==2.0.1
- IDE de sua escolha (recomendamos o VSCode ou PyCharm)
- Git (para clonar o repositório)


## Como Usar

Clone o repositório para o seu computador local.

```git clone https://github.com/LucasQCosta/Python_TDD.git```

Crie um ambiente virtual:

```python -m venv python_test```

Ative o ambiente virtual:

```python_teste/bin/activate```

E instale as dependências:

```pip install -r requirements.txt```

Após esse processo, pode-se verificar o funcionamento do pytest e sua cobertura utilizando os comandos abaixo:
```
# Para usar verificar os teste existentes estão funcionado:
    pytest -v
```


```
# Para que seja mostrado a cobertura do código no terminal
    pytest --cov=codigo tests/ --cov-report term-missing

# Para gerar um arquivo html em que possa ser verificado o mesmo que o comando anterior, porém no navegador.
    pytest --cov=codigo tests/ --cov-report html

# Para gerar um arquivo xml que facilite a visualização no terminal
    pytest --junitxml report.xml 
```


### Contribuições
Sinta-se à vontade para contribuir com o projeto, seja corrigindo bugs, adicionando novas funcionalidades ou melhorando a documentação.






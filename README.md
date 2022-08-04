# Aplicativo validador/gerador de CPF

O projeto consiste em um aplicativo que valida e gera CPF's de acordo com as regras de CPF.

## Como usar

Pode ser executado de duas maneiras: direto por um ambiente virtual de Python ou pelo Docker.

## Docker

**Essas instruções presumem que você já tenha o Docker instalado no seu Sistema Operacional.**

Execute os comandos abaixo:

1. Gere a imagem de dentro da raiz do projeto usando o comando: `docker build -t nome-da-image .`
2. Execute a imagem com o comando: `docker r^C --rm -it -v /tmp/.X11-unix:/tmp/.X11-unix -v /home:/qtuser -e DISPLAY=$DISPLAY -u qtuser pyqt-cpf-app python3 /tmp/main.py`

### Ambiente virtual

**Essas instruções presumem que você já tenha as instalações básicas do Python3 no seu Sistema Operacional.**

**Ignore os passos 1 e 2 caso esteja utilizando uma IDE como o PyCharm.**

Para executar o ambiente virtual execute os seguintes comandos:

1. Crie um ambiente virtual com: `python3 -m venv venv`
2. Inicie o ambiente virtual com: `source venv/bin/activate`
3. Instale as dependências: `pip install -y pyqt5 pyqt5-qt pyqt5-sip opencv-python`
4. Execute o aplicativo com: `python3 main.py`

## Referências

- [Regras de validação CPF](https://dicasdeprogramacao.com.br/algoritmo-para-validar-cpf/)

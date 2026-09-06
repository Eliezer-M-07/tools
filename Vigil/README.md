<div align="center">

<img width="401" height="187" alt="Vigil" src="https://github.com/user-attachments/assets/cc2ff0eb-2f0d-4ae3-80e9-1bd852b6ca41" />

Ferramenta de linha de comando desenvolvida em Python para verificação de disponibilidade de websites e portas de rede.

![Version](https://img.shields.io/badge/version-1.0.0-000000?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.x-000000?style=for-the-badge\&logo=python\&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-HTTP%2FHTTPS-000000?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-000000?style=for-the-badge)

</div>

🇧🇷 Português | [🇺🇸 English](README.en.md)

---

## Descrição

O Vigil é uma ferramenta de linha de comando destinada à verificação de disponibilidade e conectividade de hosts e serviços.

A aplicação permite realizar verificações individuais de websites e portas TCP, além de fornecer uma opção de análise completa de um host.

As informações apresentadas incluem status HTTP, endereço IPv4, latência da requisição e estado das portas analisadas.

---

## Funcionalidades

### Verificação de website

A verificação de website utiliza requisições HTTP ou HTTPS para determinar se o endereço informado está acessível.

A funcionalidade realiza:

* Verificação de disponibilidade do website.
* Identificação do código de status HTTP.
* Medição da latência da requisição.
* Adição automática de `https://` quando o protocolo não é informado.
* Tratamento de erros relacionados à requisição.

### Verificação de porta

A verificação de porta utiliza conexões TCP para determinar se uma porta específica está acessível no host informado.

O resultado da verificação é classificado de acordo com o comportamento da conexão:

| Estado     | Descrição                                          |
| ---------- | -------------------------------------------------- |
| `OPEN`     | A conexão TCP foi estabelecida com sucesso.        |
| `CLOSED`   | A conexão foi recusada pelo host.                  |
| `FILTERED` | A tentativa de conexão excedeu o tempo limite.     |
| `ERROR`    | Ocorreu outro erro durante a tentativa de conexão. |

### Full Check

A opção `Full Check` executa uma análise completa do host informado.

A verificação apresenta:

* Host analisado.
* Endereço IPv4 resolvido.
* Status de disponibilidade do website.
* Código de status HTTP.
* Latência da requisição.
* Estado das portas `443`, `80` e `8080`.

As portas verificadas são:

* `443` — HTTPS
* `80` — HTTP
* `8080` — HTTP alternativo

---

## Requisitos

Para executar o projeto, é necessário possuir:

* Python 3
* pip
* Conexão com a internet para verificações HTTP/HTTPS

A única dependência externa utilizada atualmente é a biblioteca `requests`.

---

## Instalação

Clone o repositório:

```bash
git clone <repository-url>
```

Acesse o diretório do projeto:

```bash
cd vigil
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## Execução

Execute o arquivo principal:

```bash
python main.py
```

Após a inicialização, o programa apresenta o seguinte menu:

```text
[1] Check if the website is online.
[2] Check if the port is open.
[3] Full Check
[0] Exit
```

Cada opção direciona a execução para o serviço correspondente.

---

## Estrutura do projeto

```text
vigil/
├── functions/
│   ├── clear_terminal.py
│   ├── colors.py
│   └── validate_url.py
│
├── services/
│   ├── full_check.py
│   ├── port_up.py
│   └── website_up.py
│
├── main.py
├── requirements.txt
├── README.md
└── README.en.md
```

### `functions/`

Contém funções auxiliares utilizadas pela aplicação.

| Arquivo             | Descrição                                                       |
| ------------------- | --------------------------------------------------------------- |
| `clear_terminal.py` | Responsável pela limpeza do terminal.                           |
| `colors.py`         | Define recursos relacionados à formatação de cores do terminal. |
| `validate_url.py`   | Realiza a validação e o tratamento das URLs informadas.         |


### `services/`

Contém os módulos responsáveis pelas verificações realizadas pelo Vigil.

| Arquivo         | Descrição                                             |
| --------------- | ----------------------------------------------------- |
| `website_up.py` | Realiza a verificação de disponibilidade de websites. |
| `port_up.py`    | Realiza a verificação de portas TCP.                  |
| `full_check.py` | Combina as verificações de website, IPv4 e portas.    |

---

## Tecnologias

O projeto utiliza os seguintes recursos:

* Python 3
* Requests
* Socket
* urllib.parse

### Requests

Utilizado para realizar requisições HTTP e HTTPS durante as verificações de websites.

### Socket

Utilizado para estabelecer conexões TCP e realizar a resolução de endereços de hosts.

### urllib.parse

Utilizado para análise e manipulação das URLs informadas pelo usuário.

---

## Funcionamento

O arquivo `main.py` é responsável por apresentar o menu principal e direcionar a execução para os serviços disponíveis.

### Verificação de website

O endereço informado é processado e validado antes da realização da requisição.

Quando o protocolo não é informado, o Vigil utiliza `https://` como padrão.

Após a requisição, são obtidos o status da conexão, o código HTTP retornado e o tempo necessário para concluir a operação.

### Verificação de porta

A verificação de portas utiliza conexões TCP através do módulo `socket`.

O resultado é determinado com base no comportamento da tentativa de conexão:

```text
Conexão estabelecida  -> OPEN
Conexão recusada      -> CLOSED
Tempo limite excedido -> FILTERED
Outro erro            -> ERROR
```

### Full Check

O `Full Check` combina as funcionalidades disponíveis em uma única execução.

O fluxo de verificação consiste em:

```text
Host informado
    |
    +-- Resolução IPv4
    |
    +-- Verificação do website
    |     |
    |     +-- Status
    |     +-- Código HTTP
    |     +-- Latência
    |
    +-- Verificação de portas
          |
          +-- 443
          +-- 80
          +-- 8080
```

---

## Objetivo

O objetivo do Vigil é fornecer uma interface simples para realização de verificações básicas de disponibilidade e conectividade diretamente pelo terminal.

A ferramenta pode ser utilizada para diagnóstico de conectividade, verificação de websites e análise do estado de portas TCP em hosts autorizados.

---

## Limitações

O Vigil realiza verificações básicas de disponibilidade e conectividade. Os resultados obtidos representam o comportamento do host no momento da execução e podem variar de acordo com fatores como firewall, configuração de rede, disponibilidade do serviço e tempo de resposta.

A classificação `FILTERED`, por exemplo, indica que a conexão não foi concluída dentro do tempo limite configurado, não necessariamente que a porta esteja definitivamente bloqueada.

---

## Contribuição

Contribuições para o projeto são bem-vindas.

Para contribuir:

1. Faça um fork do repositório.
2. Crie uma branch para sua alteração.
3. Implemente e teste as modificações.
4. Faça um commit das alterações.
5. Abra um Pull Request descrevendo as modificações realizadas.

---

## Licença

Consulte o arquivo de licença do projeto para obter informações sobre os termos de uso e distribuição.
### TRABALHO DE Topicos Especiais em Software


# Guia de Configuração do Projeto

Este documento fornece instruções para configurar um ambiente de desenvolvimento para este projeto. Siga os passos abaixo para criar um ambiente virtual e instalar as dependências necessárias.

## Criando um Ambiente Virtual

Para criar um ambiente virtual, siga as instruções abaixo dependendo do seu sistema operacional:

1. Abra o terminal ou o Prompt de Comando.
2. Navegue até o diretório do projeto.
3. Execute o seguinte comando para criar o ambiente virtual:

   python -m venv .venv

### Ativando o Ambiente Virtual
Depois de criar o ambiente virtual, você precisa ativá-lo:

No terminal ou Prompt de Comando, execute:
  
  .\.venv\Scripts\activate

### Instalando as Dependências
Com o ambiente virtual ativado, você pode instalar as dependências listadas no arquivo requirements.txt:

Execute o seguinte comando para instalar as dependências:

  pip install -r requirements.txt

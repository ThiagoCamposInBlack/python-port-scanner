# Python Port Scanner 🐍

![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

Um scanner de portas rápido e multi-threaded, desenvolvido em Python, projetado para identificar portas TCP abertas em um host de destino. Este projeto foi criado como uma ferramenta prática para estudos em segurança da informação e desenvolvimento de redes.

## 📋 Índice

-   [Visão Geral](#-visão-geral)
-   [Principais Funcionalidades](#-principais-funcionalidades)
-   [Demonstração](#-demonstração)
-   [Tecnologias Utilizadas](#-tecnologias-utilizadas)
-   [Pré-requisitos](#-pré-requisitos)
-   [Como Instalar e Executar](#-como-instalar-e-executar)
-   [Como Funciona](#-como-funciona)
-   [Licença](#-licença)

## 🔭 Visão Geral

Ferramentas de varredura de portas são essenciais para administradores de rede e profissionais de segurança para auditar a segurança de uma rede, identificando quais serviços estão expostos à internet. Este script oferece uma implementação leve e eficiente para realizar essa tarefa diretamente do terminal.

## ✨ Principais Funcionalidades

-   **Varredura Multi-threaded:** Utiliza threads para escanear múltiplas portas simultaneamente, garantindo alta velocidade e eficiência.
-   **Intervalo de Portas Customizável:** Permite que o usuário especifique exatamente qual intervalo de portas deseja verificar.
-   **Interface de Linha de Comando (CLI):** Interação simples e direta via terminal.
-   **Identificação de Serviços Comuns:** Reconhece e informa os serviços mais comuns associados a portas conhecidas (HTTP, SSH, FTP, etc.).

## 🚀 Demonstração

Abaixo, um exemplo de como o scanner é executado no terminal e a sua respectiva saída.

```bash
# Executando o scanner para um host local no intervalo de portas 20 a 81
$ python port_scanner.py 127.0.0.1 20 81

[+] Analisando host 127.0.0.1
------------------------------------
[✓] Porta 21 (FTP) está aberta.
[✓] Porta 22 (SSH) está aberta.
[✓] Porta 80 (HTTP) está aberta.
------------------------------------
Varredura concluída.
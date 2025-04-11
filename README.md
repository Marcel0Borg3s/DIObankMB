# 💳 DIObankMB – Desafio Bancário DIO

Este projeto foi desenvolvido como parte do desafio proposto no bootcamp da [DIO](https://www.dio.me/), com o objetivo de simular um sistema bancário simples, capaz de realizar operações básicas como depósitos, saques e emissão de extrato.

## 🔍 Funcionalidades

- ✅ Cadastro de usuários com CPF único
- ✅ Criação de contas bancárias vinculadas a usuários
- ✅ Realização de depósitos e saques
- ✅ Emissão de extrato bancário com saldo e histórico de movimentações
- ✅ Listagem de contas existentes

## 📋 Regras de Negócio

- 💵 **Limite de saque**: R$500,00 por operação  
- 🔁 **Número máximo de saques diários**: 3  
- 🕐 **Limite de transações por dia**: 10 (a ser implementado)  
- 📄 **Extrato com data e hora das operações** (em versão futura)

---

## 🧱 Versão Atual – `versao2`

Nesta versão, foi realizada uma **refatoração significativa** do código para tornar o projeto mais estruturado e escalável:

### 🔁 Refatorações:

- Migração do uso de **dicionários** para **objetos e classes**
- Modelagem de classes como `Usuário` e `ContaBancária`
- Métodos mais organizados, orientados a objetos
- Melhor separação entre **lógica de negócio** e **interface de menu**

---

## 🏁 Como executar

# Clona o repositório
git clone https://github.com/Marcel0Borg3s/DIObankMB.git

# Entra na pasta do projeto
cd DIObankMB

# Troca para a branch da versão refatorada
git checkout versao2


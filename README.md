# Desafio DIO - Automação com AWS Lambda e Amazon S3

## Descrição

Este repositório foi desenvolvido como parte do laboratório da DIO com foco em automação de tarefas utilizando AWS Lambda e Amazon S3.

O objetivo foi compreender como criar fluxos automatizados baseados em eventos, utilizando serviços serverless da AWS para processar ações sem a necessidade de gerenciamento de servidores.

---

# Objetivos do Laboratório

* Compreender o conceito de Serverless Computing.
* Criar funções Lambda.
* Configurar buckets S3.
* Integrar Lambda e S3 através de eventos.
* Monitorar execuções utilizando logs.
* Documentar os conhecimentos adquiridos.

---

# Arquitetura Utilizada

Fluxo implementado:

Usuário → Upload Arquivo → S3 → Evento → Lambda → Processamento

Sempre que um novo arquivo é enviado para o bucket, o Amazon S3 dispara automaticamente uma execução da função Lambda.

---

# Conceitos Utilizados

## AWS Lambda

Serviço de computação serverless que executa código sob demanda sem necessidade de provisionar servidores.

Principais benefícios:

* Escalabilidade automática
* Pagamento por uso
* Baixa manutenção
* Integração nativa com diversos serviços AWS

---

## Amazon S3

Serviço de armazenamento de objetos da AWS.

Principais características:

* Alta durabilidade
* Escalabilidade
* Segurança
* Integração com eventos

---

## Event-Driven Architecture

Modelo em que eventos disparam ações automaticamente.

Exemplo utilizado:

Upload de arquivo → Execução da Lambda

---

# Etapas Realizadas

## 1. Criação do Bucket S3

Foi criado um bucket para armazenamento dos arquivos enviados durante o laboratório.

---

## 2. Criação da Função Lambda

Foi criada uma função Lambda responsável por processar eventos gerados pelo bucket.

---

## 3. Configuração do Trigger

Foi configurado um gatilho (Trigger) no S3 para disparar automaticamente a Lambda após o upload de arquivos.

---

## 4. Teste da Solução

Foi realizado o upload de arquivos para validar o acionamento automático da função.

---

## 5. Monitoramento

Foram analisados:

* Logs da execução
* Eventos recebidos
* Resultados do processamento

---

# Exemplo de Função Lambda

```python
import json

def lambda_handler(event, context):

    print("Evento recebido:")
    print(json.dumps(event))

    return {
        "statusCode": 200,
        "body": "Processamento realizado com sucesso"
    }
```

---

# Benefícios Observados

* Automação de tarefas
* Redução de infraestrutura
* Escalabilidade automática
* Processamento orientado a eventos
* Baixo custo operacional

---

# Insights Pessoais

O laboratório demonstrou como arquiteturas serverless simplificam a criação de soluções escaláveis.

A integração entre Amazon S3 e AWS Lambda mostrou-se uma forma eficiente de automatizar processos baseados em eventos, eliminando a necessidade de servidores dedicados para monitoramento contínuo.

Também foi possível compreender melhor como os serviços AWS podem trabalhar de forma integrada para construir aplicações modernas e resilientes.

---

# Conclusão

A prática permitiu compreender o funcionamento da computação serverless utilizando AWS Lambda e Amazon S3, reforçando conceitos de automação, integração entre serviços e processamento orientado a eventos na nuvem.

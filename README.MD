# TestesQualidadeSoftware
Código para realização de testes



# 🧮 Projeto de Testes - Calculadora em Python

Este repositório foi criado para a disciplina **Testes e Qualidade de Software**.  
O objetivo é que os alunos pratiquem a escrita de **testes unitários** e a **análise de cobertura de código** utilizando **PyTest**.



## 📂 Estrutura do Projeto

```
calculadora-tests/
│
├── src/
│   ├── calculadora.py
│   └── api_client.py
│
├── tests/
│   ├── test_calculadora.py
│   └── test_api_client.py
│
├── requirements.txt
├── README.md
└── .gitignore
```


## 🚀 Como começar

1. **Clonar o repositório**
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd calculadora-tests
   ```

2. **Instalar dependências**
   ```bash
   pip install -r requirements.txt
   ```

3. **Executar os testes**
   ```bash
   pytest
   ```


## 🧪 Atividade Prática: Laboratório Hands-On

**Parte 1: Implementação (35 min)**

Em duplas, vocês irão:
1. Clonar o repositório da aula via GitHub Classroom  
2. Implementar testes unitários para o módulo `calculadora.py`  
3. Aplicar mocks para isolar dependências externas no módulo `api_client.py`  
4. Executar os testes e verificar se passam  

💡 **Dica:** Consultem a documentação do PyTest (https://docs.pytest.org/en/stable/) e os exemplos fornecidos no repositório. Não hesitem em chamar a professora!



## 📊 Atividade Prática: Análise de Cobertura

**Parte 2: Medição e Análise (35 min)**

1. **Executar Cobertura**  
   Rode no terminal:  
   ```bash
   pytest --cov=src --cov-report=html
   ```

2. **Abrir Relatório**  
   Navegue até `htmlcov/index.html` e explore visualmente.

3. **Identificar Lacunas**  
   Liste no `README.md`: quais linhas não foram cobertas e por quê?

4. **Propor Melhorias**  
   Escreva 2-3 novos testes para aumentar a cobertura significativamente.



## 🎯 Objetivo

Ao final da atividade, os alunos deverão:
- Ter escrito testes unitários para funções da calculadora.  
- Ter utilizado mocks para simular dependências externas.  
- Ter gerado e analisado relatórios de cobertura.  
- Ter proposto melhorias para aumentar a qualidade dos testes.  



## 📌 Observações

- O projeto é apenas um **exemplo didático**.  
- O foco está em **boas práticas de testes** e **qualidade de software**.  
- A cobertura não precisa ser 100%, mas deve ser **significativa e justificada**.
```

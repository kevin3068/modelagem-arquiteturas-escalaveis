# Tarefa 07 — Submissão ao Congresso e Modalidade de Apresentação

## 1. Dados do Evento e Submissão
- **Evento:** III Congresso UniSENAI-SP de Educação, Tecnologia e Inovação
- **Tipo de Trabalho:** Resumo Expandido (Pesquisa em Desenvolvimento)
- **Modalidade Escolhida:** **Apresentação Presencial**
- **Página oficial do evento:** https://www.even3.com.br/iiicongressounisenai-sp-721261/

---

## 2. Justificativa da Escolha da Modalidade Presencial
A opção pela apresentação presencial foi definida para maximizar o retorno acadêmico e profissional proporcionado pelo evento:
- **Interação com a Banca Avaliadora:** Possibilidade de debate direto e aprofundado sobre a metodologia experimental e o comportamento da *baseline* sob estresse.
- **Divulgação Científica e Networking:** Troca de experiências com outros pesquisadores da área de Engenharia de Software e Sistemas de Informação.
- **Coleta de Feedback:** Obtenção de contribuições imediatas da comunidade acadêmica para direcionar a continuidade do projeto de pesquisa.

---

## 3. Memorial do Processo Realizado
Durante esta etapa da Iniciação Científica, as seguintes atividades foram concluídas e documentadas no repositório:

### A. Conteinerização e Reprodutibilidade
- Estruturação do ambiente de desenvolvimento via [`docker-compose.yml`](../src/prototipo/api-app/docker-compose.yml), separando a API Laravel e o banco de dados MySQL em contêineres isolados.
- Parametrização de variáveis de ambiente seguras via [`.env.example`](../src/prototipo/api-app/.env.example), garantindo a sanitização e proteção de credenciais antes do versionamento.

### B. Execução dos Experimentos de Carga
- Elaboração do [script de testes com K6](../src/experimento/teste-carga.js), simulando múltiplos estágios de tráfego com injeção de até 100 Usuários Virtuais (VUs) simultâneos autenticados por JWT.
- Definição de critérios estritos de aceitação (SLA de tempo de resposta inferior a 500 ms).
- Identificação do ponto de saturação da máquina local: enquanto a taxa de respostas HTTP 200 permaneceu em 100%, a latência média extrapolou os limites aceitáveis (conforme log armazenado em [`/data/bruto/baseline-local-v1.json`](../data/bruto/baseline-local-v1.json)).

### C. Tratamento de Dados e Visualização
- Processamento do log bruto de métricas através do script [`gerar_grafico.py`](../src/experimento/gerar_grafico_k6_v1.py).
- Geração da síntese visual com eixos duplos (correlacionando VUs e tempo de resposta), cujo resultado final pode ser visualizado em [`/data/tratado/grafico_k6_resultados.png`](../data/tratado/grafico_k6_resultados_v1.png).

### D. Redação Acadêmica e Normalização
- Escrita completa do resumo expandido de acordo com o template oficial disponibilizado, sintetizando os dados gerados nos experimentos.
- O manuscrito final em PDF encontra-se disponível no diretório [`docs/artigos/resumo-expandido.pdf`](../docs/artigos/resumo-expandido.pdf).

---

## 4. Próximos Passos
1. Acompanhamento da avaliação e do parecer do comitê científico do congresso.
2. Preparação do material audiovisual (slides / pôster técnico) para a sessão presencial de apresentação.
3. Continuidade da pesquisa, com foco na implantação da arquitetura e nova coleta de dados na nuvem AWS.
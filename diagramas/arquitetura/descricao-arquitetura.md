# Consolidação da Arquitetura da Solução

Esta documentação detalha a arquitetura proposta para a avaliação de desempenho de sistemas web escaláveis em ambiente de nuvem, substituindo o modelo monolítico tradicional por uma abordagem *cloud-native*.

### 1. Organização dos Componentes
A solução adota a separação estrita de responsabilidades:
* **Front-end:** Aplicação estática de página única (SPA), isolada do processamento lógico.
* **Back-end:** API RESTful desenvolvida em PHP (Laravel), totalmente conteinerizada (Docker).
* **Banco de Dados:** Instância relacional gerenciada, dedicada à persistência de dados.

### 2. Comunicação entre Serviços
A comunicação entre o cliente (Front-end) e o servidor (Back-end) ocorre exclusivamente via protocolo HTTP/HTTPS utilizando o padrão REST. O intercâmbio de dados é feito no formato JSON, e as rotas protegidas exigem o envio de um token JWT (JSON Web Token) no cabeçalho (*header*) de autorização.

### 3. Infraestrutura em Nuvem (AWS)
* **Amazon S3:** Hospedagem de baixo custo e alta disponibilidade para os arquivos estáticos do Front-end (HTML, CSS, JS).
* **Amazon ECS com AWS Fargate:** Orquestração *serverless* dos contêineres Docker do Back-end.
* **Application Load Balancer (ALB):** Ponto de entrada do Back-end, responsável por distribuir o tráfego de rede.
* **Amazon RDS (MySQL):** Serviço de banco de dados relacional gerenciado.

### 4. Fluxo de Dados
1. O usuário acessa a interface carregada diretamente do **Amazon S3**.
2. O navegador dispara requisições assíncronas (`fetch`) para o **ALB**.
3. O ALB roteia a requisição para um dos contêineres **Laravel** ociosos no **ECS**.
4. A API Laravel processa a regra de negócio, consulta/modifica os dados no **Amazon RDS** e devolve a resposta em JSON para a interface.
5. Em paralelo, a ferramenta **K6/JMeter** injeta requisições massivas diretamente no ALB para simular estresse.

### 5. Escalabilidade
A escalabilidade horizontal é o núcleo desta proposta. O Application Load Balancer monitora a carga de tráfego. Quando os limites de CPU/Memória definidos no ECS Fargate são atingidos devido ao estresse gerado pelos testes, o orquestrador provisiona novos contêineres idênticos da API automaticamente (Auto-scaling), destruindo-os quando o tráfego normaliza.

### 6. Segurança
* **Autenticação Stateless:** O uso do JWT elimina a necessidade de armazenar sessões no servidor, protegendo as rotas da API e viabilizando a escalabilidade de múltiplos contêineres independentes.
* **Isolamento de Rede:** O Amazon RDS é protegido por *Security Groups* da AWS, bloqueando qualquer acesso externo à internet e permitindo requisições apenas originadas pelos contêineres internos do ECS.

### 7. Definição Tecnológica
* **Linguagens e Frameworks:** HTML, CSS, JavaScript (Vanilla), PHP, Laravel.
* **Infraestrutura e DevOps:** Docker, AWS (S3, ECS Fargate, ALB, RDS).
* **Qualidade e Avaliação:** K6 ou Apache JMeter (Testes de carga).

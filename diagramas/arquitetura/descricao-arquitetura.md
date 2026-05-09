# Arquitetura da Solução: Avaliação de API REST Escalável

Esta solução propõe uma arquitetura conteinerizada na nuvem, desenhada de forma objetiva para avaliar a escalabilidade e o desempenho de uma API REST sob cenários de alta demanda. 

### Componentes da Arquitetura
* **Front-end:** Interface estática simples, desenvolvida puramente em HTML, CSS e JavaScript (Vanilla), responsável apenas por consumir a API.
* **Back-end (API REST):** Desenvolvido em PHP com o framework Laravel. A aplicação será isolada em contêineres Docker, garantindo que o mesmo ambiente testado localmente seja executado na nuvem.
* **Banco de Dados:** Utilização de MySQL como banco relacional para persistência de dados.
* **Autenticação:** Baseada em tokens JWT (JSON Web Tokens) gerenciados pelo próprio Laravel, garantindo uma autenticação *stateless* (sem estado), o que é fundamental para permitir a escalabilidade horizontal dos contêineres.
* **Ferramenta de Teste de Carga (Escalabilidade):** Uso da ferramenta **K6** (ou Apache JMeter) para injetar tráfego massivo e simular milhares de usuários simultâneos acessando os endpoints da API.

### Infraestrutura na Nuvem (AWS)
A infraestrutura focará na distribuição de carga e escalabilidade horizontal:
1. **Front-end:** Hospedado estaticamente no **Amazon S3** (armazenamento de arquivos de baixo custo).
2. **Back-end:** Contêineres Docker da API Laravel orquestrados pelo **Amazon ECS** operando no modelo **AWS Fargate** (Serverless). Isso permite aumentar ou diminuir a quantidade de instâncias do Laravel automaticamente sem precisar gerenciar servidores.
3. **Distribuição de Tráfego:** Um **Application Load Balancer (ALB)** da AWS receberá as requisições web e as distribuirá de forma equilibrada entre os diversos contêineres do Laravel disponíveis.
4. **Banco de Dados:** Instância gerenciada pelo **Amazon RDS (Relational Database Service) para MySQL**, facilitando backups, monitoramento de conexões e escalabilidade da camada de dados.

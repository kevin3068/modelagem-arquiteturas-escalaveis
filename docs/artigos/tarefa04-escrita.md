# ☁️ Modelagem e Avaliação de Arquitetura de Software para Sistemas Web Escaláveis

## Capítulo 1 — Introdução

A transformação digital contemporânea alterou de maneira substancial os paradigmas de desenvolvimento e implantação de sistemas computacionais. Serviços digitais se popularizaram em escala global, aumentando a demanda por plataformas capazes de suportar tráfego intenso para a sobrevivência de organizações nos mais diversos setores. Nesse contexto, a arquitetura de software é fundamental para garantir a estabilidade, a segurança e a evolução contínua de aplicações web modernas.

É de suma importância estabelecer uma base arquitetural sólida e bem projetada para mitigar riscos operacionais, como indisponibilidades prolongadas e gargalos de desempenho que afetam a experiência do usuário final. Sistemas escaláveis precisam prever o crescimento exponencial e imprevisível de acessos, exigindo a adoção de padrões que permitam a alocação dinâmica e inteligente de recursos computacionais, garantindo que o software consuma apenas os recursos necessários em momentos de ociosidade e expanda sua capacidade durante picos de utilização.

Sistemas legados têm uma chance muito maior de enfrentarem desafios de manutenção e evolução. A abordagem tradicional, frequentemente baseada em aplicações monolíticas fortemente acopladas, impõe barreiras significativas à agilidade corporativa e práticas de entrega contínua de software. A transição para modelos distribuídos, como microsserviços e computação em nuvem nativa, é impulsionada pela busca por maior modularidade, resiliência e independência entre as equipes de desenvolvimento.

Atualmente, a adoção acelerada de plataformas cloud-native, que potencializam o uso de contêineres eficientes e orquestradores avançados para otimizar o ciclo de vida da aplicação, consolida metodologias como DevOps e ferramentas de infraestrutura como código (IaC). Aplicações altamente escaláveis democratizam o acesso à informação, garantindo que milhares de usuários, independentemente de sua origem, possam interagir com serviços digitais de alta performance simultaneamente.

## Capítulo 2 — Problema e Objetivos

A concepção arquitetural de sistemas web escaláveis ainda esbarra em desafios relacionados ao acoplamento de componentes sistêmicos e à rápida degradação de desempenho sob alta carga computacional. O problema central desta pesquisa se concentra na dificuldade operacional de dimensionar aplicações sem custos de infraestrutura exorbitantes ou falhas de arquitetura. Sistemas projetados sem a previsibilidade de escala tendem a apresentar gargalos na camada de banco de dados e latência no tempo de resposta de requisições web.

Existe uma falta de comparação empírica e quantitativa de diferentes modelos arquiteturais submetidos a condições de estresse virtualmente idênticas. Embora o uso da arquitetura de microsserviços seja amplamente recomendado pelo mercado, carecem estudos direcionados que comparem sistematicamente o custo-benefício e a sobrecarga de rede (network overhead) gerada pela comunicação interna entre múltiplos serviços em contêineres.

O objetivo geral do presente trabalho é modelar, implementar e avaliar uma proposta de arquitetura de software orientada a microsserviços, hospedada integralmente em ambiente de computação em nuvem. O intuito é fornecer uma base empírica, robusta e analítica que auxilie na tomada de decisão arquitetural de engenheiros e pesquisadores. O estudo demonstrará, por meio de simulações práticas, como a separação de responsabilidades e a conteinerização melhoram o comportamento da aplicação sob tráfego intenso.

Para alcançar esse propósito, definem-se os seguintes objetivos específicos: mapear padrões de projeto para sistemas web distribuídos; desenhar a arquitetura de referência com front-end isolado e back-end conteinerizado; desenvolver uma prova de conceito (PoC) utilizando infraestrutura como código; e executar testes de carga com injeção massiva de tráfego. A hipótese central é que uma arquitetura de microsserviços provisionada dinamicamente na nuvem reduzirá o tempo médio de resposta durante picos de acesso, superando o desempenho de um servidor monolítico.

## Capítulo 3 — Fundamentação Inicial

A fundamentação teórica apoia-se nos conceitos de escalabilidade, alta disponibilidade e elasticidade aplicados a sistemas distribuídos. A escalabilidade divide-se em vertical (aumento de capacidade em uma única máquina) e horizontal (adição de novas instâncias à rede). A literatura aponta a escalabilidade horizontal como o padrão atual, visto que plataformas em nuvem permitem o provisionamento elástico e imediato de recursos, eliminando pontos únicos de falha.

As soluções no estado da arte consolidam o paradigma Cloud-Native, focado no desenvolvimento de aplicações que exploram o potencial dos ambientes em nuvem. Nesse modelo, tecnologias como Docker padronizam o empacotamento da aplicação em contêineres isolados, reduzindo divergências entre os ambientes de desenvolvimento e produção. Paralelamente, orquestradores assumem o gerenciamento do roteamento de tráfego, a verificação de integridade e a auto-recuperação do sistema.

A transição do modelo monolítico para um ecossistema de microsserviços é a evolução estrutural mais debatida na literatura da área. Enquanto o monólito acopla regras de negócios, interfaces e persistência em um único pacote, a arquitetura de microsserviços divide o sistema em componentes independentes e especializados. Esses módulos interagem via APIs RESTful, viabilizando implantações ágeis e garantindo isolamento contra falhas em cascata.

Embora tendências arquiteturais apontem para o uso crescente de sistemas assíncronos orientados a eventos, o foco primário na avaliação de desempenho sob estresse recai sobre a capacidade do orquestrador de alocar recursos sob demanda.

A partir do cenário tecnológico avaliado, constata-se a necessidade de produzir metodologias documentadas que mensurem o balanço entre consumo de nuvem, custos operacionais e entrega de desempenho. Este projeto ambiciona suprir essa demanda técnica, servindo como referência prática e agregando dados empíricos à literatura sobre dimensionamento de arquiteturas escaláveis.

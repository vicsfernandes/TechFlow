# TechFlow #

#TechFlow Solutions - Verificador de Estoque (SKU Checker)
Este projeto é uma simulação de desenvolvimento de software ágil, parte do desafio de Engenharia de Software. O objetivo é criar uma ferramenta interna para a equipe de logística e gerenciamento de armazém da TechFlow Solutions.

A aplicação consiste em um micro-serviço web que permite aos funcionários consultar rapidamente a disponibilidade de produtos no inventário.

1. Escopo Inicial (MVP)
O escopo inicial do projeto (Produto Mínimo Viável) está focado em entregar a funcionalidade de consulta mais crítica e direta. O sistema permitirá que um usuário:

Acesse uma interface web simples.

Insira um código SKU (Stock Keeping Unit) de um produto em um formulário.

Receba um feedback imediato informando a quantidade exata daquele item em estoque.

Se o SKU não for encontrado, o sistema informará ao usuário que o item não existe no inventário. A lógica do back-end utilizará um conjunto de dados mock (um dicionário Python) para simular o banco de dados do inventário.


### 🔄 Gestão de Mudança: Alteração de Escopo

Seguindo os princípios ágeis, o projeto foi adaptado para uma nova demanda do cliente (gerente do armazém).

**A Mudança:**
O escopo inicial permitia a consulta de estoque apenas pelo **SKU** (código do produto). O cliente solicitou que a ferramenta também permitisse a busca por um **Número de Série (Serial Number)** específico, para que a equipe pudesse rastrear um item individual e ver a qual grupo de SKU ele pertencia.

**Ação de Gerenciamento:**
A mudança foi documentada aqui, um novo card foi criado no Kanban, e a aplicação (front-end, back-end e testes) foi atualizada. A lógica de back-end agora prioriza a busca por Número de Série e, se não encontrar, tenta a busca por SKU. A mudança foi registrada em um commit específico.
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

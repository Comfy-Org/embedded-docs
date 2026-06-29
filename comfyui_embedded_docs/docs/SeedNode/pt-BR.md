# Seed

O nó Seed gera um valor inteiro fixo ou aleatório. Ele é comumente usado para controlar a reprodutibilidade de operações aleatórias em outros nós, fornecendo um ponto de partida consistente para a geração de números aleatórios.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `semente` | O valor da semente a ser usado. A opção de controle após a geração determina se o valor permanece fixo ou muda após cada geração. | INT | Sim | 0 a 9223372036854775807 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|-------------|-------------|-----------|
| `semente` | O valor da semente gerado. | INT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `19f9b22945bb152ff5066195067f1b6b4c006589f26c7533fad905044ac3b7fa`

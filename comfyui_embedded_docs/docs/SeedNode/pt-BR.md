# Seed

O nó Seed fornece um valor inteiro que pode ser usado como semente para controlar a reprodutibilidade de operações aleatórias em outros nós. Ao fornecer um valor inicial consistente, ele ajuda a manter os resultados gerados repetíveis quando necessário.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `seed` | O valor de semente a ser usado. A opção control after generate determina se o valor permanece fixo ou muda após cada geração; neste nó, ela está definida como fixed. | INT | Sim | 0 a 9223372036854775807 |

## Saídas

| Nome de Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `seed` | O valor de semente gerado. | INT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `19f9b22945bb152ff5066195067f1b6b4c006589f26c7533fad905044ac3b7fa`

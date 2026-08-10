# Seed

O nó Seed fornece um valor inteiro que pode ser usado como semente para controlar a reprodutibilidade de operações aleatórias em outros nós. Ao fornecer um valor inicial consistente, ajuda a manter resultados repetíveis quando necessário.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `semente` | O valor de semente a ser usado. A opção de controle após gerar determina se o valor permanece fixo ou muda após cada geração; neste nó, ele é definido como fixo. | INT | Sim | 0 a 9223372036854775807 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|-------------|-------------|-----------|
| `semente` | O valor da semente gerado. | INT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `19f9b22945bb152ff5066195067f1b6b4c006589f26c7533fad905044ac3b7fa`

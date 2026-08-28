# Latents em Lote

O nó Batch Latents combina múltiplas entradas latentes em um único lote. Ele aceita um número variável de amostras latentes e as mescla ao longo da dimensão do lote para que possam ser processadas em conjunto por nós subsequentes. O nó também mescla os metadados de índice de lote de todas as entradas na saída combinada.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `latents` | Um conjunto de amostras latentes a serem combinadas em um único lote. Você deve fornecer pelo menos um latente e pode adicionar até 50. O nó cria automaticamente slots de entrada conforme você conecta mais latentes. | LATENT | Sim | 1 a 50 entradas |

**Observação:** Você deve fornecer pelo menos uma entrada latente para que o nó funcione. O nó cria automaticamente slots de entrada conforme você conecta mais latentes, até um máximo de 50. Cada entrada latente é redimensionada para corresponder ao formato da amostra do primeiro latente antes de ser combinada, e qualquer latente sem metadados de índice de lote recebe um índice de lote sequencial.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `output` | Uma única saída latente contendo todas as entradas latentes combinadas em um lote, juntamente com seus metadados de índice de lote mesclados. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BatchLatentsNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `38df5e6cfa391e054c663af1cc55728d115cebfbb804e1c2c51dfc2aab37df47`

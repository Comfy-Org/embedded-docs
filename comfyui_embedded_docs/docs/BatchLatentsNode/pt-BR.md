# Latents em Lote

O nó Batch Latents combina múltiplas entradas latentes em um único lote. Ele recebe um número variável de amostras latentes e as mescla ao longo da dimensão de lote, para que possam ser processadas em conjunto pelos nós subsequentes. O nó também mescla os metadados de índice de lote de todas as entradas na saída combinada.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `latents` | Um conjunto de amostras latentes a serem combinadas em um único lote. Você deve fornecer pelo menos uma amostra latente, e pode adicionar até 50. O nó cria automaticamente slots de entrada (`latent_1`, `latent_2`, e assim por diante) à medida que você conecta mais latentes. | LATENT | Sim | 1 a 50 entradas |

**Nota:** Você deve fornecer pelo menos uma entrada latente para que o nó funcione. O nó cria automaticamente slots de entrada à medida que você conecta mais latentes, até um máximo de 50. Cada amostra latente de entrada é remodelada para corresponder ao formato de amostra da primeira latente antes de ser combinada, e qualquer amostra latente sem metadados de índice de lote recebe um índice de lote sequencial. As amostras latentes de entrada são unidas ao longo da dimensão de lote para produzir o resultado combinado.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `output` | Uma única saída latente contendo todas as amostras latentes de entrada combinadas em um lote, juntamente com seus metadados de índice de lote mesclados. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BatchLatentsNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `38df5e6cfa391e054c663af1cc55728d115cebfbb804e1c2c51dfc2aab37df47`

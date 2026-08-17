# Latents em Lote

O nó **Batch Latents** combina múltiplas entradas latentes em um único lote. Ele recebe um número variável de amostras latentes e as mescla ao longo da dimensão do lote, permitindo que sejam processadas juntas em nós subsequentes. Isso é útil para gerar ou processar múltiplas imagens em uma única operação.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `latents` | Um conjunto de amostras latentes a serem combinadas em um único lote. Você deve fornecer pelo menos uma entrada latente e pode adicionar até 50. O nó cria automaticamente slots de entrada conforme você conecta mais entradas latentes. | LATENT | Sim | 1 a 50 entradas |

**Nota:** Você deve fornecer pelo menos uma entrada latente para que o nó funcione. O nó criará automaticamente slots de entrada conforme você conecta mais entradas latentes, até o máximo de 50.

Todas as entradas latentes são remodeladas para corresponder às dimensões espaciais da primeira entrada latente antes de serem combinadas. Os metadados `batch_index` de cada entrada latente são transferidos para a saída; uma entrada sem `batch_index` recebe uma sequência padrão começando em 0.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `output` | Uma única saída latente contendo todas as entradas latentes combinadas em um lote. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BatchLatentsNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `38df5e6cfa391e054c663af1cc55728d115cebfbb804e1c2c51dfc2aab37df47`

# EmptyChromaRadianceLatentImage

O nó `EmptyChromaRadianceLatentImage` cria uma imagem latente em branco com dimensões especificadas para uso em fluxos de trabalho de radiância cromática. Ele gera um tensor preenchido com zeros (contendo 3 canais de cor) que serve como ponto de partida para operações no espaço latente. O nó permite definir a largura, a altura e o tamanho do lote da imagem latente vazia.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `width` | A largura da imagem latente em pixels (padrão: 1024, deve ser divisível por 16) | INT | Sim | 16 to MAX_RESOLUTION |
| `height` | A altura da imagem latente em pixels (padrão: 1024, deve ser divisível por 16) | INT | Sim | 16 to MAX_RESOLUTION |
| `batch_size` | O número de imagens latentes a serem geradas em um lote (padrão: 1) | INT | Não | 1 to 4096 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `samples` | O tensor de imagem latente vazio gerado, com as dimensões especificadas, preenchido com zeros | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyChromaRadianceLatentImage/pt-BR.md)

---
**Source fingerprint (SHA-256):** `870cc89fb021c258c214db153cda0a32a63da1b6bf92f09cbd3b8498c363096b`

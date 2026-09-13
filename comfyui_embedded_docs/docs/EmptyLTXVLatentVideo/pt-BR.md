# EmptyLTXVLatentVideo

O nó EmptyLTXVLatentVideo cria um tensor de vídeo latente vazio (preenchido com zeros) usando `width`, `height`, `length` e `batch_size` que você especifica. Ele fornece um ponto de partida em branco para fluxos de trabalho de geração de vídeo LTXV, com as dimensões latentes automaticamente comprimidas em relação ao tamanho de vídeo solicitado.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `width` | A largura do tensor de vídeo latente (padrão: 768, passo: 32) | INT | Sim | 64 a MAX_RESOLUTION |
| `height` | A altura do tensor de vídeo latente (padrão: 512, passo: 32) | INT | Sim | 64 a MAX_RESOLUTION |
| `length` | O número de quadros no vídeo latente (padrão: 97, passo: 8) | INT | Sim | 1 a MAX_RESOLUTION |
| `batch_size` | O número de vídeos latentes a gerar em um lote (padrão: 1) | INT | Sim | 1 a 4096 |

Observação: O vídeo latente é comprimido em comparação com as dimensões solicitadas: as dimensões espaciais (`width` e `height`) são divididas por 32, e a contagem de quadros (`length`) é dividida por 8 e arredondada para cima até o número inteiro mais próximo. Os valores de passo para `width`, `height` e `length` ajudam a manter essas divisões exatas.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `samples` | O tensor latente vazio gerado com valores zero nas dimensões especificadas, juntamente com uma taxa de redução espacial de 32 | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLTXVLatentVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `0b1e57baf9730d852b03b6bccbb8a033e2be9b9cd2420a0aa3638c31f6d3cd26`

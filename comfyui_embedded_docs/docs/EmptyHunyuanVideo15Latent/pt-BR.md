# Empty HunyuanVideo 1.5 Latent

This node creates an empty latent tensor specifically formatted for use with the HunyuanVideo 1.5 model. It generates a blank starting point for video generation by allocating a tensor of zeros with the correct channel count and spatial dimensions for the model's latent space.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `largura` | A largura do quadro de vídeo em pixels. | INT | Sim | - |
| `altura` | A altura do quadro de vídeo em pixels. | INT | Sim | - |
| `duração` | O número de quadros na sequência de vídeo. | INT | Sim | - |
| `tamanho_do_lote` | O número de amostras de vídeo a serem geradas em um lote (padrão: 1). | INT | Não | - |

**Nota:** As dimensões espaciais do tensor latente gerado são calculadas dividindo-se os valores de entrada `width` e `height` por 16 (este nó usa um fator de escala espacial de 16 em vez de 8). A dimensão temporal (quadros) é calculada como `((length - 1) // 4) + 1`. Esses cálculos usam divisão inteira, portanto `width` e `height` devem ser múltiplos de 16 para evitar truncamento.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `samples` | Um tensor latente vazio com dimensões adequadas para o modelo HunyuanVideo 1.5. O tensor tem formato `[batch_size, 32, ((length - 1) // 4) + 1, height // 16, width // 16]`. A saída também inclui um valor `downscale_ratio_spacial` de 16. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHunyuanVideo15Latent/pt-BR.md)

---
**Source fingerprint (SHA-256):** `ce7ec75e8433c778d175a3e2ea260a4397aa5507428908b9a32f50fbe9e184c6`

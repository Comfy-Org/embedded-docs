# Empty HunyuanVideo 1.5 Latent

Este nó cria um tensor latente vazio especificamente formatado para uso com o modelo HunyuanVideo 1.5. Ele gera um ponto de partida em branco para a geração de vídeo alocando um tensor de zeros com a quantidade correta de canais e dimensões espaciais para o espaço latente do modelo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `width` | A largura do quadro de vídeo em pixels. | INT | Sim | - |
| `height` | A altura do quadro de vídeo em pixels. | INT | Sim | - |
| `length` | O número de quadros na sequência de vídeo. | INT | Sim | - |
| `batch_size` | O número de amostras de vídeo a serem geradas em um lote (padrão: 1). | INT | Não | - |

**Nota:** As dimensões espaciais do tensor latente gerado são calculadas dividindo a `width` e a `height` de entrada por 16. A dimensão temporal (quadros) é calculada como `((length - 1) // 4) + 1`.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `samples` | Um tensor latente vazio com dimensões adequadas para o modelo HunyuanVideo 1.5. O tensor tem uma forma de `[batch_size, 32, frames, height//16, width//16]`. A saída também inclui um valor `downscale_ratio_spacial` de 16. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHunyuanVideo15Latent/pt-BR.md)

---
**Source fingerprint (SHA-256):** `ce7ec75e8433c778d175a3e2ea260a4397aa5507428908b9a32f50fbe9e184c6`

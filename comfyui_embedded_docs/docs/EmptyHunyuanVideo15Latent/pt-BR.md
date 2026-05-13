> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHunyuanVideo15Latent/pt-BR.md)

Esta documentação foi gerada por IA. Se encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHunyuanVideo15Latent/en.md)

Este nó cria um tensor latente vazio especificamente formatado para uso com o modelo HunyuanVideo 1.5. Ele gera um ponto de partida em branco para a geração de vídeo, alocando um tensor de zeros com a contagem correta de canais e dimensões espaciais para o espaço latente do modelo.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|-----------|----------|-------|-------------|
| `width` | INT | Sim | - | A largura do quadro de vídeo em pixels. |
| `height` | INT | Sim | - | A altura do quadro de vídeo em pixels. |
| `length` | INT | Sim | - | O número de quadros na sequência de vídeo. |
| `batch_size` | INT | Não | - | O número de amostras de vídeo a serem geradas em um lote (padrão: 1). |

**Nota:** As dimensões espaciais do tensor latente gerado são calculadas dividindo a `width` e `height` de entrada por 16. A dimensão temporal (quadros) é calculada como `((length - 1) // 4) + 1`.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `samples` | LATENT | Um tensor latente vazio com dimensões adequadas para o modelo HunyuanVideo 1.5. O tensor tem a forma `[batch_size, 32, frames, height//16, width//16]`. A saída também inclui um valor `downscale_ratio_spacial` de 16. |

---
**Source fingerprint (SHA-256):** `eebc131adfe63f6bc8367f2a96b3ac7f3f3223c5b1fb308eda3ec09c94fff2ee`

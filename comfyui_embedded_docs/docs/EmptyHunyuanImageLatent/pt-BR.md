# EmptyHunyuanImageLatent

O nó `EmptyHunyuanImageLatent` cria um tensor latente vazio com dimensões específicas para uso com modelos de geração de imagem Hunyuan. Ele gera um ponto de partida em branco que pode ser processado por nós subsequentes no fluxo de trabalho. O nó permite especificar a largura, a altura e o tamanho do lote do espaço latente.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `width` | A largura da imagem latente gerada em pixels (padrão: 2048, passo: 32) | INT | Sim | 64 a MAX_RESOLUTION |
| `height` | A altura da imagem latente gerada em pixels (padrão: 2048, passo: 32) | INT | Sim | 64 a MAX_RESOLUTION |
| `batch_size` | O número de amostras latentes a gerar em um lote (padrão: 1) | INT | Sim | 1 a 4096 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `LATENT` | Um tensor latente vazio com as dimensões especificadas para processamento de imagem Hunyuan. O tensor tem 64 canais e suas dimensões espaciais são um trinta e dois avos (1/32) da largura e altura solicitadas. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHunyuanImageLatent/pt-BR.md)

---
**Source fingerprint (SHA-256):** `31fc10d43c224810709870cf40256b6fccd4743445ea9d98d148d443bc591d7a`

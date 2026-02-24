> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHunyuanImageLatent/pt-BR.md)

O nó EmptyHunyuanImageLatent cria um tensor latente vazio com dimensões específicas para uso com modelos de geração de imagem Hunyuan. Ele gera um ponto de partida em branco que pode ser processado por nós subsequentes no fluxo de trabalho. O nó permite especificar a largura, altura e tamanho do lote do espaço latente.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `width` | INT | Sim | 64 a MAX_RESOLUTION | A largura da imagem latente gerada em pixels (padrão: 2048, incremento: 32) |
| `height` | INT | Sim | 64 a MAX_RESOLUTION | A altura da imagem latente gerada em pixels (padrão: 2048, incremento: 32) |
| `batch_size` | INT | Sim | 1 a 4096 | O número de amostras latentes a serem geradas em um lote (padrão: 1) |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `LATENT` | LATENT | Um tensor latente vazio com as dimensões especificadas para processamento de imagem Hunyuan |

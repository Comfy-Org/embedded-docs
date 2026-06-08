O nó **EmptyHunyuanImageLatent** cria um tensor latente vazio com dimensões específicas para uso com modelos de geração de imagem Hunyuan. Ele gera um ponto de partida em branco que pode ser processado por nós subsequentes no fluxo de trabalho. O nó permite especificar a largura, altura e tamanho do lote do espaço latente.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `largura` | A largura da imagem latente gerada em pixels (padrão: 2048, incremento: 32) | INT | Sim | 64 a MAX_RESOLUTION |
| `altura` | A altura da imagem latente gerada em pixels (padrão: 2048, incremento: 32) | INT | Sim | 64 a MAX_RESOLUTION |
| `tamanho_do_lote` | O número de amostras latentes a serem geradas em um lote (padrão: 1) | INT | Sim | 1 a 4096 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `LATENT` | Um tensor latente vazio com as dimensões especificadas para processamento de imagem Hunyuan | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHunyuanImageLatent/pt-BR.md)

---
**Source fingerprint (SHA-256):** `18e920527c88be2648d8cbe4255f693123be4e70a9e21dd379310088a1470834`

# EmptyHunyuanImageLatent

O nó EmptyHunyuanImageLatent cria um espaço latente vazio (preenchido com zeros) para modelos de geração de imagem Hunyuan. Ele gera um latente inicial em branco com a largura, altura e tamanho do lote especificados, que pode ser passado para nós subsequentes no fluxo de trabalho. O tensor latente tem 64 canais, e suas dimensões espaciais são a largura e a altura, cada uma dividida por 32.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `largura` | A largura da imagem latente gerada em pixels (padrão: 2048, passo: 32) | INT | Sim | 64 to MAX_RESOLUTION |
| `altura` | A altura da imagem latente gerada em pixels (padrão: 2048, passo: 32) | INT | Sim | 64 to MAX_RESOLUTION |
| `tamanho_do_lote` | O número de amostras latentes a serem geradas em um lote (padrão: 1) | INT | Sim | 1 a 4096 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `LATENT` | Um tensor latente vazio com 64 canais e dimensões de altura ÷ 32 por largura ÷ 32, pronto para o processamento de imagens Hunyuan | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHunyuanImageLatent/pt-BR.md)

---
**Source fingerprint (SHA-256):** `31fc10d43c224810709870cf40256b6fccd4743445ea9d98d148d443bc591d7a`

# EmptyMochiLatentVideo

EmptyMochiLatentVideo cria um tensor de vídeo latente vazio com as dimensões que você especifica. Ele gera uma representação latente preenchida com zeros que pode ser usada como ponto de partida para fluxos de trabalho de geração de vídeo. O nó permite definir a largura, a altura, o comprimento e o tamanho do lote do tensor de vídeo latente.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `largura` | A largura do vídeo latente em pixels (padrão: 848, os valores aumentam em incrementos de 16) | INT | Sim | 16 a MAX_RESOLUTION |
| `altura` | A altura do vídeo latente em pixels (padrão: 480, os valores aumentam em incrementos de 16) | INT | Sim | 16 a MAX_RESOLUTION |
| `comprimento` | O número de quadros no vídeo latente (padrão: 25, os valores aumentam em incrementos de 6, começando em 7) | INT | Sim | 7 a MAX_RESOLUTION |
| `tamanho_do_lote` | O número de vídeos latentes a gerar em um lote (padrão: 1) | INT | Não | 1 a 4096 |

**Observação:** As dimensões latentes reais são calculadas como width/8 e height/8, a dimensão temporal é calculada como `((length - 1) // 6) + 1`, e o tensor tem 12 canais. Como `length` avança em incrementos de 6 começando em 7, os valores válidos são 7, 13, 19, 25 e assim por diante.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `samples` | Um tensor de vídeo latente vazio com as dimensões especificadas, contendo apenas zeros | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyMochiLatentVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `1774e1b54b429a946172ba9f609b433d99c0ca2ced2d9e0e3b0b85c82e5141b2`

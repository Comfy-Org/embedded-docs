O nó EmptyMochiLatentVideo cria um tensor de vídeo latente vazio com dimensões especificadas. Ele gera uma representação latente preenchida com zeros que pode ser usada como ponto de partida para fluxos de trabalho de geração de vídeo. O nó permite definir largura, altura, comprimento e tamanho do lote para o tensor de vídeo latente.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `largura` | A largura do vídeo latente em pixels (padrão: 848, deve ser divisível por 16) | INT | Sim | 16 a MAX_RESOLUTION |
| `altura` | A altura do vídeo latente em pixels (padrão: 480, deve ser divisível por 16) | INT | Sim | 16 a MAX_RESOLUTION |
| `comprimento` | O número de quadros no vídeo latente (padrão: 25, deve ser divisível por 6 após subtrair 1) | INT | Sim | 7 a MAX_RESOLUTION |
| `tamanho_do_lote` | O número de vídeos latentes a serem gerados em um lote (padrão: 1) | INT | Não | 1 a 4096 |

**Observação:** As dimensões latentes reais são calculadas como largura/8 e altura/8, e a dimensão temporal é calculada como ((comprimento - 1) // 6) + 1. O parâmetro `length` deve satisfazer que `(length - 1)` seja divisível por 6, o que significa que os valores válidos são 7, 13, 19, 25, etc.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `samples` | Um tensor de vídeo latente vazio com as dimensões especificadas, contendo todos os zeros | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyMochiLatentVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `6876a739355b2dcde42f8c02eb67405678798b818865ec1a73e19076b738554b`

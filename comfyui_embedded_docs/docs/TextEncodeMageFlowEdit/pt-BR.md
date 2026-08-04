# TextEncodeMageFlowEdit

## Visão Geral

Este nó codifica uma instrução de edição (prompt) juntamente com uma ou mais imagens de referência para o modelo Mage-Flow-Edit. Ele redimensiona todas as imagens de referência para a resolução de saída desejada, codifica-as no espaço latente se um VAE for fornecido e anexa os latentes de referência à saída de conditioning. Um tensor latente vazio com as dimensões corretas para amostragem também é gerado, garantindo que o tamanho sempre corresponda à largura e altura de saída.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `clip` | O modelo CLIP usado para tokenizar e codificar os prompts de texto. | CLIP | Sim | |
| `prompt` | A instrução de edição (prompt positivo) a ser aplicada. | STRING | Sim | multiline, dynamic prompts enabled |
| `negative_prompt` | O prompt negativo para evitar. Padrão: string vazia (usa um espaço internamente quando em branco). Exibido na seção avançada da interface. | STRING | Não | multilinha, prompts dinâmicos habilitados |
| `vae` | Modelo VAE para codificar as imagens de referência no espaço latente. Se não for fornecido, nenhum latente de referência é adicionado ao conditioning. | VAE | Não | |
| `images` | Imagem(ns) de referência para editar. Todas as referências são redimensionadas para a resolução de saída antes da codificação. | IMAGE (autogrow) | Não | Até 16 imagens (nomeadas `image_1`…`image_16`), pelo menos 0 |
| `width` | Largura de saída em pixels. Se definido como 0, a largura da primeira imagem de referência é usada. Sempre arredondado para baixo até um múltiplo de 16. Padrão: 0. | INT | Sim | 0 a 8192 (passo 16) |
| `height` | Altura de saída em pixels. Mesmo comportamento de fallback que a largura. Padrão: 0. | INT | Sim | 0 a 8192 (passo 16) |
| `batch_size` | Número de amostras latentes a serem geradas. Padrão: 1. | INT | Sim | 1 a 4096 |

**Observações sobre dependências de parâmetros:**
- Se `width` e/ou `height` forem 0 e nenhuma imagem de referência for fornecida, eles recaem para 1024 cada.
- Se apenas um de `width` ou `height` for 0, a dimensão ausente é obtida da primeira imagem de referência enquanto a dimensão definida explicitamente é mantida.
- O parâmetro `vae` é opcional; latentes de referência só são gerados e anexados ao conditioning quando um VAE está conectado.
- O campo `negative_prompt` é opcional – se deixado vazio, um único espaço é usado internamente como o texto negativo.
- Para o condicionamento de texto, cada imagem de referência é redimensionada para que sua borda mais longa tenha no máximo 384 pixels, correspondendo ao pré-processamento de treinamento. O ramo de codificação VAE, por outro lado, redimensiona todas as referências para a resolução de saída completa.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `positive` | Saída de conditioning contendo os tokens do prompt positivo, além dos latentes de referência codificados (se um VAE foi fornecido). | CONDITIONING |
| `negative` | Saída de conditioning contendo os tokens do prompt negativo, além dos mesmos latentes de referência (se VAE fornecido). | CONDITIONING |
| `latent` | Um tensor latente vazio com formato `[batch_size, 128, height÷16, width÷16]` para uso como ruído inicial durante a amostragem. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeMageFlowEdit/pt-BR.md)

---
**Source fingerprint (SHA-256):** `880d8856b7f6e656bc68ca953fbf892898d05bc5d65290ae3bf7a4405ee09be3`

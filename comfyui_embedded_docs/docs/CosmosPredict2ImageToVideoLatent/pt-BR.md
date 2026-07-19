# CosmosPredict2ImageToVideoLatent

Esta documentação foi gerada por IA. Se encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CosmosPredict2ImageToVideoLatent/en.md)

O nó CosmosPredict2ImageToVideoLatent cria representações latentes de vídeo a partir de imagens para geração de vídeos. Ele pode gerar um latente de vídeo em branco ou incorporar imagens de início e fim para criar sequências de vídeo com dimensões e duração especificadas. O nó gerencia a codificação das imagens no formato de espaço latente apropriado para processamento de vídeo.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `vae` | O modelo VAE usado para codificar imagens no espaço latente | VAE | Sim | - |
| `largura` | A largura do vídeo de saída em pixels (padrão: 848, deve ser divisível por 16) | INT | Não | 16 a MAX_RESOLUTION |
| `altura` | A altura do vídeo de saída em pixels (padrão: 480, deve ser divisível por 16) | INT | Não | 16 a MAX_RESOLUTION |
| `comprimento` | O número de quadros na sequência de vídeo (padrão: 93, passo: 4) | INT | Não | 1 a MAX_RESOLUTION |
| `tamanho_do_lote` | O número de sequências de vídeo a serem geradas (padrão: 1) | INT | Não | 1 a 4096 |
| `imagem_inicial` | Imagem inicial opcional para a sequência de vídeo | IMAGE | Não | - |
| `imagem_final` | Imagem final opcional para a sequência de vídeo | IMAGE | Não | - |

**Observação:** Quando nem `start_image` nem `end_image` são fornecidos, o nó gera um latente de vídeo em branco. Quando as imagens são fornecidas, elas são codificadas e posicionadas no início e/ou no final da sequência de vídeo com mascaramento apropriado.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `samples` | A representação latente do vídeo gerado contendo a sequência de vídeo codificada | LATENT |
| `noise_mask` | Uma máscara indicando quais partes do latente devem ser preservadas durante a geração | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CosmosPredict2ImageToVideoLatent/pt-BR.md)

---
**Source fingerprint (SHA-256):** `55fab16180c0e3fa254bcc77694dbc666810b28522e61b9c613f720fae66bd0c`

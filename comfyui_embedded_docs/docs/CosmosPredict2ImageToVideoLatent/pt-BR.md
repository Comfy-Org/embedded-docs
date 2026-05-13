> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CosmosPredict2ImageToVideoLatent/pt-BR.md)

Esta documentação foi gerada por IA. Se encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CosmosPredict2ImageToVideoLatent/en.md)

O nó CosmosPredict2ImageToVideoLatent cria representações latentes de vídeo a partir de imagens para geração de vídeos. Ele pode gerar um latente de vídeo em branco ou incorporar imagens de início e fim para criar sequências de vídeo com dimensões e duração especificadas. O nó gerencia a codificação das imagens no formato de espaço latente apropriado para processamento de vídeo.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|--------------|-------------|-----------|-----------|
| `vae` | VAE | Sim | - | O modelo VAE usado para codificar imagens no espaço latente |
| `largura` | INT | Não | 16 a MAX_RESOLUTION | A largura do vídeo de saída em pixels (padrão: 848, deve ser divisível por 16) |
| `altura` | INT | Não | 16 a MAX_RESOLUTION | A altura do vídeo de saída em pixels (padrão: 480, deve ser divisível por 16) |
| `comprimento` | INT | Não | 1 a MAX_RESOLUTION | O número de quadros na sequência de vídeo (padrão: 93, passo: 4) |
| `tamanho_do_lote` | INT | Não | 1 a 4096 | O número de sequências de vídeo a serem geradas (padrão: 1) |
| `imagem_inicial` | IMAGE | Não | - | Imagem inicial opcional para a sequência de vídeo |
| `imagem_final` | IMAGE | Não | - | Imagem final opcional para a sequência de vídeo |

**Observação:** Quando nem `start_image` nem `end_image` são fornecidos, o nó gera um latente de vídeo em branco. Quando as imagens são fornecidas, elas são codificadas e posicionadas no início e/ou no final da sequência de vídeo com mascaramento apropriado.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `samples` | LATENT | A representação latente do vídeo gerado contendo a sequência de vídeo codificada |
| `noise_mask` | LATENT | Uma máscara indicando quais partes do latente devem ser preservadas durante a geração |

---
**Source fingerprint (SHA-256):** `55fab16180c0e3fa254bcc77694dbc666810b28522e61b9c613f720fae66bd0c`

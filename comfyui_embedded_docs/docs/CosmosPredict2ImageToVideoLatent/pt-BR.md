# CosmosPredict2ImageToVideoLatent

O nó CosmosPredict2ImageToVideoLatent cria representações latentes de vídeo a partir de imagens para a geração de vídeos. Ele pode gerar um latente de vídeo em branco ou incorporar imagens inicial e final para criar sequências de vídeo com dimensões e duração especificadas. O nó processa a codificação das imagens no formato apropriado de espaço latente para o processamento de vídeo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `vae` | O modelo VAE usado para codificar imagens no espaço latente | VAE | Sim | - |
| `width` | A largura do vídeo de saída em pixels (padrão: 848, deve ser divisível por 16) | INT | Sim | 16 to MAX_RESOLUTION (step 16) |
| `height` | A altura do vídeo de saída em pixels (padrão: 480, deve ser divisível por 16) | INT | Sim | 16 to MAX_RESOLUTION (step 16) |
| `length` | O número de quadros na sequência de vídeo (padrão: 93) | INT | Sim | 1 to MAX_RESOLUTION (step 4) |
| `batch_size` | O número de sequências de vídeo a gerar (padrão: 1) | INT | Sim | 1 to 4096 |
| `start_image` | Imagem inicial opcional para a sequência de vídeo | IMAGE | Não | - |
| `end_image` | Imagem final opcional para a sequência de vídeo | IMAGE | Não | - |

**Nota:** Quando nem `start_image` nem `end_image` são fornecidos, o nó gera um latente de vídeo em branco. Quando imagens são fornecidas, elas são codificadas e posicionadas no início e/ou no final da sequência de vídeo com mascaramento adequado.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `samples` | A representação latente de vídeo gerada contendo a sequência de vídeo codificada | LATENT |
| `noise_mask` | Uma máscara que indica quais partes do latente devem ser preservadas durante a geração | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CosmosPredict2ImageToVideoLatent/pt-BR.md)

---
**Source fingerprint (SHA-256):** `842bd2b8cda438e7b938439d4eba280478939e3302dc1846d52595d40082ff05`

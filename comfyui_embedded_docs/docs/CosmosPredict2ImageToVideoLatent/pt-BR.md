# CosmosPredict2ImageToVideoLatent

CosmosPredict2ImageToVideoLatent cria representações latentes de vídeo a partir de imagens para a geração de vídeos. Ele pode gerar um latente de vídeo em branco ou incorporar imagens de início e fim para criar sequências de vídeo com dimensões e duração específicas. O nó codifica as imagens no formato de espaço latente apropriado para o processamento de vídeo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `vae` | O modelo VAE usado para codificar imagens no espaço latente | VAE | Sim | - |
| `largura` | A largura do vídeo de saída em pixels (padrão: 848, deve ser divisível por 16) | INT | Sim | 16 a MAX_RESOLUTION |
| `altura` | A altura do vídeo de saída em pixels (padrão: 480, deve ser divisível por 16) | INT | Sim | 16 a MAX_RESOLUTION |
| `comprimento` | O número de quadros na sequência de vídeo (padrão: 93, passo: 4) | INT | Sim | 1 a MAX_RESOLUTION |
| `tamanho_do_lote` | O número de sequências de vídeo a serem geradas (padrão: 1) | INT | Sim | 1 a 4096 |
| `imagem_inicial` | Imagem inicial opcional para a sequência de vídeo | IMAGE | Não | - |
| `imagem_final` | Imagem final opcional para a sequência de vídeo | IMAGE | Não | - |

**Nota:** Quando nem `start_image` nem `end_image` são fornecidos, o nó gera um latente de vídeo em branco. Quando uma ou ambas as imagens são fornecidas, elas são redimensionadas para `width` e `height`, codificadas no espaço latente e posicionadas no início e/ou no final da sequência de vídeo, com as regiões correspondentes marcadas na máscara de ruído para que sejam preservadas durante a geração. O latente e a máscara resultantes são repetidos `batch_size` vezes.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `samples` | A representação latente de vídeo gerada contendo a sequência de vídeo codificada | LATENT |
| `noise_mask` | Uma máscara que indica quais partes do latente devem ser preservadas durante a geração. Presente apenas quando pelo menos uma das imagens `start_image` ou `end_image` for fornecida. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CosmosPredict2ImageToVideoLatent/pt-BR.md)

---
**Source fingerprint (SHA-256):** `842bd2b8cda438e7b938439d4eba280478939e3302dc1846d52595d40082ff05`

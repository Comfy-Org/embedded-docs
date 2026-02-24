> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CosmosPredict2ImageToVideoLatent/pt-BR.md)

O nó CosmosPredict2ImageToVideoLatent cria representações latentes de vídeo a partir de imagens para geração de vídeo. Ele pode gerar um latente de vídeo em branco ou incorporar imagens de início e fim para criar sequências de vídeo com dimensões e duração especificadas. O nó gerencia a codificação das imagens no formato apropriado do espaço latente para processamento de vídeo.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `vae` | VAE | Sim | - | O modelo VAE usado para codificar imagens no espaço latente |
| `width` | INT | Não | 16 a MAX_RESOLUTION | A largura do vídeo de saída em pixels (padrão: 848, deve ser divisível por 16) |
| `height` | INT | Não | 16 a MAX_RESOLUTION | A altura do vídeo de saída em pixels (padrão: 480, deve ser divisível por 16) |
| `length` | INT | Não | 1 a MAX_RESOLUTION | O número de quadros na sequência de vídeo (padrão: 93, passo: 4) |
| `batch_size` | INT | Não | 1 a 4096 | O número de sequências de vídeo a serem geradas (padrão: 1) |
| `start_image` | IMAGE | Não | - | Imagem inicial opcional para a sequência de vídeo |
| `end_image` | IMAGE | Não | - | Imagem final opcional para a sequência de vídeo |

**Observação:** Quando nem `start_image` nem `end_image` são fornecidos, o nó gera um latente de vídeo em branco. Quando imagens são fornecidas, elas são codificadas e posicionadas no início e/ou no fim da sequência de vídeo com uma máscara apropriada.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `samples` | LATENT | A representação latente de vídeo gerada, contendo a sequência de vídeo codificada |
| `noise_mask` | LATENT | Uma máscara que indica quais partes do latente devem ser preservadas durante a geração |

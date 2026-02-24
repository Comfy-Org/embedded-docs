> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVImgToVideo/pt-BR.md)

O nó LTXVImgToVideo converte uma imagem de entrada em uma representação latente de vídeo para modelos de geração de vídeo. Ele recebe uma única imagem e a estende em uma sequência de quadros usando o codificador VAE, em seguida, aplica condicionamento com controle de intensidade para determinar quanto do conteúdo original da imagem é preservado versus modificado durante a geração do vídeo.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Sim | - | Prompts de condicionamento positivo para orientar a geração do vídeo |
| `negative` | CONDITIONING | Sim | - | Prompts de condicionamento negativo para evitar certos elementos no vídeo |
| `vae` | VAE | Sim | - | Modelo VAE usado para codificar a imagem de entrada no espaço latente |
| `image` | IMAGE | Sim | - | Imagem de entrada a ser convertida em quadros de vídeo |
| `width` | INT | Não | 64 a MAX_RESOLUTION | Largura do vídeo de saída em pixels (padrão: 768, passo: 32) |
| `height` | INT | Não | 64 a MAX_RESOLUTION | Altura do vídeo de saída em pixels (padrão: 512, passo: 32) |
| `length` | INT | Não | 9 a MAX_RESOLUTION | Número de quadros no vídeo gerado (padrão: 97, passo: 8) |
| `batch_size` | INT | Não | 1 a 4096 | Número de vídeos a serem gerados simultaneamente (padrão: 1) |
| `strength` | FLOAT | Não | 0.0 a 1.0 | Controle sobre quanto a imagem original é modificada durante a geração do vídeo, onde 1.0 preserva a maior parte do conteúdo original e 0.0 permite a modificação máxima (padrão: 1.0) |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Condicionamento positivo processado com máscara de quadro de vídeo aplicada |
| `negative` | CONDITIONING | Condicionamento negativo processado com máscara de quadro de vídeo aplicada |
| `latent` | LATENT | Representação latente de vídeo contendo os quadros codificados e a máscara de ruído para geração de vídeo |

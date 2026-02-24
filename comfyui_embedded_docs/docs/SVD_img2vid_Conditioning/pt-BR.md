> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SVD_img2vid_Conditioning/pt-BR.md)

O nó SVD_img2vid_Conditioning prepara os dados de condicionamento para geração de vídeo usando o Stable Video Diffusion. Ele recebe uma imagem inicial e a processa através dos codificadores CLIP vision e VAE para criar pares de condicionamento positivo e negativo, juntamente com um espaço latente vazio para a geração do vídeo. Este nó configura os parâmetros necessários para controlar o movimento, a taxa de quadros e os níveis de aumento no vídeo gerado.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `clip_vision` | CLIP_VISION | Sim | - | Modelo CLIP vision para codificar a imagem de entrada |
| `init_image` | IMAGE | Sim | - | Imagem inicial a ser usada como ponto de partida para a geração do vídeo |
| `vae` | VAE | Sim | - | Modelo VAE para codificar a imagem no espaço latente |
| `width` | INT | Sim | 16 a MAX_RESOLUTION | Largura do vídeo de saída (padrão: 1024, incremento: 8) |
| `height` | INT | Sim | 16 a MAX_RESOLUTION | Altura do vídeo de saída (padrão: 576, incremento: 8) |
| `video_frames` | INT | Sim | 1 a 4096 | Número de quadros a serem gerados no vídeo (padrão: 14) |
| `motion_bucket_id` | INT | Sim | 1 a 1023 | Controla a quantidade de movimento no vídeo gerado (padrão: 127) |
| `fps` | INT | Sim | 1 a 1024 | Quadros por segundo para o vídeo gerado (padrão: 6) |
| `augmentation_level` | FLOAT | Sim | 0.0 a 10.0 | Nível de aumento de ruído a ser aplicado à imagem de entrada (padrão: 0.0, incremento: 0.01) |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Dados de condicionamento positivo contendo incorporações de imagem e parâmetros de vídeo |
| `negative` | CONDITIONING | Dados de condicionamento negativo com incorporações zeradas e parâmetros de vídeo |
| `latent` | LATENT | Tensor de espaço latente vazio pronto para a geração de vídeo |

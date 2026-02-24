> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SV3D_Conditioning/pt-BR.md)

O nó SV3D_Conditioning prepara dados de condicionamento para geração de vídeo 3D usando o modelo SV3D. Ele recebe uma imagem inicial e a processa por meio dos codificadores CLIP vision e VAE para criar condicionamentos positivo e negativo, juntamente com uma representação latente. O nó gera sequências de elevação e azimute da câmera para geração de vídeo multiframe com base no número especificado de quadros de vídeo.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `clip_vision` | CLIP_VISION | Sim | - | O modelo CLIP vision usado para codificar a imagem de entrada |
| `init_image` | IMAGE | Sim | - | A imagem inicial que serve como ponto de partida para a geração do vídeo 3D |
| `vae` | VAE | Sim | - | O modelo VAE usado para codificar a imagem no espaço latente |
| `width` | INT | Não | 16 a MAX_RESOLUTION | A largura de saída para os quadros de vídeo gerados (padrão: 576, deve ser divisível por 8) |
| `height` | INT | Não | 16 a MAX_RESOLUTION | A altura de saída para os quadros de vídeo gerados (padrão: 576, deve ser divisível por 8) |
| `video_frames` | INT | Não | 1 a 4096 | O número de quadros a serem gerados para a sequência de vídeo (padrão: 21) |
| `elevation` | FLOAT | Não | -90.0 a 90.0 | O ângulo de elevação da câmera em graus para a visão 3D (padrão: 0.0) |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Os dados de condicionamento positivo contendo incorporações de imagem e parâmetros de câmera para geração |
| `negative` | CONDITIONING | Os dados de condicionamento negativo com incorporações zeradas para geração contrastiva |
| `latent` | LATENT | Um tensor latente vazio com dimensões correspondentes aos quadros de vídeo e resolução especificados |

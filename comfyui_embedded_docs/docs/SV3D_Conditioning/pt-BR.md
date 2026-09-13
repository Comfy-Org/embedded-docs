# SV3D_Conditioning

SV3D_Conditioning prepara dados de condicionamento para geração de vídeo 3D usando o modelo SV3D. Ele recebe uma imagem inicial e a processa por meio de codificadores de visão CLIP e VAE para criar condicionamento positivo e negativo, juntamente com uma representação latente. O nó gera sequências de elevação e azimute da câmera para geração de vídeo com vários quadros com base no número especificado de quadros de vídeo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `clip_vision` | O modelo de visão CLIP usado para codificar a imagem de entrada | CLIP_VISION | Sim | - |
| `init_image` | A imagem inicial que serve como ponto de partida para a geração de vídeo 3D | IMAGE | Sim | - |
| `vae` | O modelo VAE usado para codificar a imagem no espaço latente | VAE | Sim | - |
| `width` | A largura de saída para os quadros de vídeo gerados (padrão: 576, passo de 8) | INT | Sim | 16 a MAX_RESOLUTION |
| `height` | A altura de saída para os quadros de vídeo gerados (padrão: 576, passo de 8) | INT | Sim | 16 a MAX_RESOLUTION |
| `video_frames` | O número de quadros a gerar para a sequência de vídeo (padrão: 21) | INT | Sim | 1 a 4096 |
| `elevation` | O ângulo de elevação da câmera em graus para a visualização 3D (padrão: 0.0, passo de 0.1) | FLOAT | Sim | -90.0 a 90.0 |

Observação: O azimute da câmera começa em 0 graus e aumenta em uma quantidade constante a cada quadro, de modo que a câmera complete uma órbita completa de 360 graus ao redor do objeto ao longo dos quadros gerados. O incremento por quadro é calculado como 360 dividido por (`video_frames` - 1), usando um divisor mínimo de 2 quando apenas um quadro é solicitado. O valor de `elevation` permanece constante para todos os quadros.

A `init_image` é redimensionada para a `width` e a `height` especificadas antes da codificação VAE, e o latente retornado usa dimensões de `video_frames` x 4 x (`height` // 8) x (`width` // 8).

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `positive` | Os dados de condicionamento positivo contendo embeddings de imagem e parâmetros de câmera para geração | CONDITIONING |
| `negative` | Os dados de condicionamento negativo com embeddings e latentes zerados para geração contrastiva | CONDITIONING |
| `latent` | Um tensor latente vazio com dimensões correspondentes aos quadros de vídeo e à resolução especificados | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SV3D_Conditioning/pt-BR.md)

---
**Source fingerprint (SHA-256):** `e28173cfa560290e66b032687088cf0b981256ca5c21f6aa608e0fdaec886665`

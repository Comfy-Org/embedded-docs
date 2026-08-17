# SV3D_Conditioning

O nó SV3D_Conditioning prepara dados de condicionamento para geração de vídeo 3D usando o modelo SV3D. Ele recebe uma imagem inicial e a processa por meio dos codificadores CLIP vision e VAE para criar condicionamentos positivo e negativo, juntamente com uma representação latente. O nó gera sequências de elevação e azimute da câmera para a geração de vídeo com múltiplos quadros, com base no número de quadros de vídeo especificado.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-------------|--------------|-------------|-------|
| `clip_vision` | O modelo de visão CLIP usado para codificar a imagem de entrada | CLIP_VISION | Sim | - |
| `init_image` | A imagem inicial que serve como ponto de partida para a geração de vídeo 3D | IMAGE | Sim | - |
| `vae` | O modelo VAE usado para codificar a imagem no espaço latente | VAE | Sim | - |
| `width` | A largura de saída para os quadros de vídeo gerados (padrão: 576, deve ser divisível por 8) | INT | Sim | 16 a MAX_RESOLUTION (passo de 8) |
| `height` | A altura de saída para os quadros de vídeo gerados (padrão: 576, deve ser divisível por 8) | INT | Sim | 16 a MAX_RESOLUTION (passo de 8) |
| `video_frames` | O número de quadros a serem gerados para a sequência de vídeo (padrão: 21) | INT | Sim | 1 a 4096 |
| `elevation` | O ângulo de elevação da câmera em graus para a visualização 3D, aplicado a cada quadro (padrão: 0.0) | FLOAT | Sim | -90.0 a 90.0 (passo de 0.1) |

Observação: O azimute da câmera começa em 0 graus e aumenta em 360 / (video_frames - 1) graus por quadro, de modo que a câmera completa uma órbita completa ao redor do objeto ao longo da sequência. O mesmo valor de `elevation` é aplicado a todos os quadros.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|---------------|-------------|--------------|
| `positive` | Os dados de condicionamento positivos contendo embeddings de imagem e parâmetros de câmera para geração | CONDITIONING |
| `negative` | Os dados de condicionamento negativos com embeddings zerados para geração contrastiva | CONDITIONING |
| `latent` | Um tensor latente vazio com dimensões correspondentes aos quadros de vídeo e à resolução especificados | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SV3D_Conditioning/pt-BR.md)

---
**Source fingerprint (SHA-256):** `e28173cfa560290e66b032687088cf0b981256ca5c21f6aa608e0fdaec886665`

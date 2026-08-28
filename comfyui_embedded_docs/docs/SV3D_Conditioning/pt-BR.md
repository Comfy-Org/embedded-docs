# SV3D_Conditioning

O SV3D_Conditioning prepara dados de condicionamento para a geração de vídeo 3D usando o modelo SV3D. Ele recebe uma imagem inicial e a processa por meio dos codificadores CLIP vision e VAE para criar condicionamento positivo e negativo, juntamente com uma representação latente. O nó gera sequências de elevação e azimute da câmera para a geração de vídeo com múltiplos quadros com base no número especificado de quadros de vídeo.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `clip_vision` | O modelo CLIP vision usado para codificar a imagem de entrada | CLIP_VISION | Sim | - |
| `imagem_inicial` | A imagem inicial que serve como ponto de partida para a geração de vídeo 3D | IMAGE | Sim | - |
| `vae` | O modelo VAE usado para codificar a imagem no espaço latente | VAE | Sim | - |
| `largura` | A largura de saída para os quadros de vídeo gerados (padrão: 576, deve ser divisível por 8) | INT | Sim | 16 a MAX_RESOLUTION |
| `altura` | A altura de saída para os quadros de vídeo gerados (padrão: 576, deve ser divisível por 8) | INT | Sim | 16 a MAX_RESOLUTION |
| `quadros_de_vídeo` | O número de quadros a serem gerados para a sequência de vídeo (padrão: 21) | INT | Sim | 1 a 4096 |
| `elevação` | O ângulo de elevação da câmera em graus para a visão 3D (padrão: 0.0) | FLOAT | Sim | -90.0 a 90.0 |

Nota: O azimute da câmera começa em 0 graus e aumenta em uma quantidade constante a cada quadro, de modo que a câmera complete uma órbita completa de 360 graus ao redor do objeto ao longo dos quadros gerados. O valor de `elevation` permanece constante para cada quadro.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `positivo` | Os dados de condicionamento positivo, contendo embeddings de imagem e parâmetros de câmera para a geração | CONDITIONING |
| `negativo` | Os dados de condicionamento negativo, com embeddings e latentes zerados para geração contrastiva | CONDITIONING |
| `latent` | Um tensor latente vazio com dimensões correspondentes aos quadros de vídeo e à resolução especificados | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SV3D_Conditioning/pt-BR.md)

---
**Source fingerprint (SHA-256):** `e28173cfa560290e66b032687088cf0b981256ca5c21f6aa608e0fdaec886665`

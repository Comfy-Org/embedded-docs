# MiniMax H3 Max Camera Control

Este nó gera um vídeo que parte de uma imagem estática e move a câmera para um novo ângulo e distância ao redor do sujeito. Azimute, elevação e distância descrevem onde a câmera termina; o primeiro quadro permanece exatamente como fornecido. Quando nenhum prompt é fornecido, a cena fica congelada e apenas a câmera se move.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model` | Modelo a usar para a geração de vídeo. | DYNAMIC_COMBO | Sim | "MiniMax H3 Max" |

### Entradas do MiniMax H3 Max

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `image` | Primeiro quadro do vídeo, com pelo menos 256x256 pixels. A proporção deve estar entre 0,4 e 2,5. | IMAGE | Sim | Imagem única |
| `camera_info` | Câmera final opcional, por exemplo, de Create Camera Info ou Compose Camera Angle Prompt, com a imagem como vista frontal. Quando conectada, define o azimute e a elevação. | LOAD3D_CAMERA | Não | Informações de câmera |
| `prompt` | Opcional. Quando vazio, a cena fica congelada e apenas a câmera se move. | STRING | Sim | 0 a 50000 caracteres |
| `azimuth` | Órbita horizontal ao redor do sujeito ao final do vídeo, em graus a partir da imagem (padrão: 90). Valores positivos movem a câmera para a direita, de modo que o sujeito gira em direção à esquerda do quadro. É um alvo: uma órbita de 90 graus frequentemente termina entre 30 e 90 graus. Ignorado quando `camera_info` está conectado. | INT | Sim | -360 a 360 |
| `elevation` | Ângulo vertical da câmera ao final do vídeo, em graus (padrão: 0). Valores positivos olham de cima para baixo, valores negativos olham de baixo para cima. Ignorado quando `camera_info` está conectado. | INT | Sim | -90 a 90 |
| `distance` | Distância da câmera ao final do vídeo em relação à imagem: 1 mantém, abaixo de 1 aproxima, acima de 1 afasta (padrão: 1,0). | FLOAT | Sim | 0,1 a 10,0 |
| `duration` | Duração do vídeo de saída em segundos (padrão: 5). | INT | Sim | 1 a 15 |
| `resolution` | Resolução do vídeo de saída (padrão: "768P"). | COMBO | Sim | "480P"<br>"768P"<br>"1080P" |
| `prompt_expansion_mode` | Quanto esforço é dedicado à reescrita do prompt antes da geração (padrão: "balanced"). | COMBO | Sim | "disabled"<br>"balanced"<br>"quality" |
| `seed` | Semente aleatória. A mesma requisição com a mesma seed gera resultados semelhantes, mas não necessariamente idênticos (padrão: 42). | INT | Sim | 0 a 4294967295 |

## Saídas

| Nome da saída | Descrição | Tipo de dados |
| --- | --- | --- |
| `video` | O vídeo gerado com o movimento de câmera aplicado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03MaxCameraControlNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `d9eed1a3ae91891b974bea39ea00101c0577cf5b204d4c701b13b232e0604153`

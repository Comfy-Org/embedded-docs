> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanCameraEmbedding/pt-BR.md)

O nó WanCameraEmbedding gera embeddings de trajetória de câmera usando embeddings de Plücker com base em parâmetros de movimento da câmera. Ele cria uma sequência de poses de câmera que simulam diferentes movimentos da câmera e os converte em tensores de embedding adequados para pipelines de geração de vídeo.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `camera_pose` | COMBO | Sim | "Static"<br>"Pan Up"<br>"Pan Down"<br>"Pan Left"<br>"Pan Right"<br>"Zoom In"<br>"Zoom Out"<br>"Anti Clockwise (ACW)"<br>"ClockWise (CW)" | O tipo de movimento da câmera a ser simulado (padrão: "Static") |
| `width` | INT | Sim | 16 a MAX_RESOLUTION | A largura da saída em pixels (padrão: 832, passo: 16) |
| `height` | INT | Sim | 16 a MAX_RESOLUTION | A altura da saída em pixels (padrão: 480, passo: 16) |
| `length` | INT | Sim | 1 a MAX_RESOLUTION | O comprimento da sequência de trajetória da câmera (padrão: 81, passo: 4) |
| `speed` | FLOAT | Não | 0.0 a 10.0 | A velocidade do movimento da câmera (padrão: 1.0, passo: 0.1) |
| `fx` | FLOAT | Não | 0.0 a 1.0 | O parâmetro de distância focal x (padrão: 0.5, passo: 0.000000001) |
| `fy` | FLOAT | Não | 0.0 a 1.0 | O parâmetro de distância focal y (padrão: 0.5, passo: 0.000000001) |
| `cx` | FLOAT | Não | 0.0 a 1.0 | A coordenada x do ponto principal (padrão: 0.5, passo: 0.01) |
| `cy` | FLOAT | Não | 0.0 a 1.0 | A coordenada y do ponto principal (padrão: 0.5, passo: 0.01) |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `camera_embedding` | TENSOR | O tensor de embedding da câmera gerado, contendo a sequência de trajetória |
| `width` | INT | O valor de largura que foi usado para o processamento |
| `height` | INT | O valor de altura que foi usado para o processamento |
| `length` | INT | O valor de comprimento que foi usado para o processamento |

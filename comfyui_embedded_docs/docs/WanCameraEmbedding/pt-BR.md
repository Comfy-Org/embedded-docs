# WanCameraEmbedding

O nó WanCameraEmbedding gera embeddings de trajetória de câmera usando embeddings de Plücker com base em parâmetros de movimento de câmera. Ele cria uma sequência de poses de câmera que simulam diferentes movimentos de câmera e as converte em tensores de embedding adequados para pipelines de geração de vídeo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `camera_pose` | O tipo de movimento de câmera a simular (padrão: "Static") | COMBO | Sim | "Static"<br>"Pan Up"<br>"Pan Down"<br>"Pan Left"<br>"Pan Right"<br>"Zoom In"<br>"Zoom Out"<br>"Anti Clockwise (ACW)"<br>"ClockWise (CW)" |
| `width` | A largura da saída em pixels (padrão: 832, passo: 16) | INT | Sim | 16 a MAX_RESOLUTION |
| `height` | A altura da saída em pixels (padrão: 480, passo: 16) | INT | Sim | 16 a MAX_RESOLUTION |
| `length` | O comprimento da sequência de trajetória de câmera (padrão: 81, passo: 4) | INT | Sim | 1 a MAX_RESOLUTION |
| `speed` | A velocidade do movimento da câmera (padrão: 1.0, passo: 0.1) | FLOAT | Não | 0.0 a 10.0 |
| `fx` | O parâmetro de distância focal x (padrão: 0.5, passo: 0.000000001) | FLOAT | Não | 0.0 a 1.0 |
| `fy` | O parâmetro de distância focal y (padrão: 0.5, passo: 0.000000001) | FLOAT | Não | 0.0 a 1.0 |
| `cx` | A coordenada x do ponto principal (padrão: 0.5, passo: 0.01) | FLOAT | Não | 0.0 a 1.0 |
| `cy` | A coordenada y do ponto principal (padrão: 0.5, passo: 0.01) | FLOAT | Não | 0.0 a 1.0 |

Nota: `fx`, `fy`, `cx` e `cy` são parâmetros avançados. O parâmetro `length` usa um passo de 4 porque o primeiro quadro da câmera é repetido internamente; portanto, o comprimento efetivo da sequência processada se torna `length + 3`.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `camera_embedding` | O tensor de embedding de câmera gerado contendo a sequência de trajetória | TENSOR |
| `width` | O valor de largura usado para o processamento | INT |
| `height` | O valor de altura usado para o processamento | INT |
| `length` | O valor de comprimento usado para o processamento | INT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanCameraEmbedding/pt-BR.md)

---
**Source fingerprint (SHA-256):** `1a2f98d83d18033581823dee61b5a3686d560c749c55223f81febca89654a29f`

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanCameraEmbedding/pt-BR.md)

O nó WanCameraEmbedding gera embeddings de trajetória de câmera utilizando embeddings de Plücker com base em parâmetros de movimento de câmera. Ele cria uma sequência de poses de câmera que simulam diferentes movimentos e as converte em tensores de embedding adequados para pipelines de geração de vídeo.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `camera_pose` | COMBO | Sim | "Estática"<br>"Panorâmica para Cima"<br>"Panorâmica para Baixo"<br>"Panorâmica para Esquerda"<br>"Panorâmica para Direita"<br>"Aproximar"<br>"Afastar"<br>"Anti-Horário (AH)"<br>"Horário (H)" | O tipo de movimento de câmera a ser simulado (padrão: "Estática") |
| `width` | INT | Sim | 16 a RESOLUÇÃO_MÁXIMA | A largura da saída em pixels (padrão: 832, passo: 16) |
| `height` | INT | Sim | 16 a RESOLUÇÃO_MÁXIMA | A altura da saída em pixels (padrão: 480, passo: 16) |
| `length` | INT | Sim | 1 a RESOLUÇÃO_MÁXIMA | O comprimento da sequência de trajetória da câmera (padrão: 81, passo: 4) |
| `speed` | FLOAT | Não | 0.0 a 10.0 | A velocidade do movimento da câmera (padrão: 1.0, passo: 0.1) |
| `fx` | FLOAT | Não | 0.0 a 1.0 | O parâmetro de distância focal x (padrão: 0.5, passo: 0.000000001) |
| `fy` | FLOAT | Não | 0.0 a 1.0 | O parâmetro de distância focal y (padrão: 0.5, passo: 0.000000001) |
| `cx` | FLOAT | Não | 0.0 a 1.0 | A coordenada x do ponto principal (padrão: 0.5, passo: 0.01) |
| `cy` | FLOAT | Não | 0.0 a 1.0 | A coordenada y do ponto principal (padrão: 0.5, passo: 0.01) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `camera_embedding` | TENSOR | O tensor de embedding de câmera gerado contendo a sequência de trajetória |
| `width` | INT | O valor de largura utilizado para o processamento |
| `height` | INT | O valor de altura utilizado para o processamento |
| `length` | INT | O valor de comprimento utilizado para o processamento |

---
**Source fingerprint (SHA-256):** `422c4a1fdfb6fd403afac26a609f80cbdbaa87f2c115068de9d7a33c756e71fd`

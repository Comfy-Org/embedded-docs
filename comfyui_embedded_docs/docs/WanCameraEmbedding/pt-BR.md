O nó WanCameraEmbedding gera embeddings de trajetória de câmera utilizando embeddings de Plücker com base em parâmetros de movimento de câmera. Ele cria uma sequência de poses de câmera que simulam diferentes movimentos e as converte em tensores de embedding adequados para pipelines de geração de vídeo.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `pose_da_câmera` | O tipo de movimento de câmera a ser simulado (padrão: "Estática") | COMBO | Sim | "Estática"<br>"Panorâmica para Cima"<br>"Panorâmica para Baixo"<br>"Panorâmica para Esquerda"<br>"Panorâmica para Direita"<br>"Aproximar"<br>"Afastar"<br>"Anti-Horário (AH)"<br>"Horário (H)" |
| `largura` | A largura da saída em pixels (padrão: 832, passo: 16) | INT | Sim | 16 a RESOLUÇÃO_MÁXIMA |
| `altura` | A altura da saída em pixels (padrão: 480, passo: 16) | INT | Sim | 16 a RESOLUÇÃO_MÁXIMA |
| `duração` | O comprimento da sequência de trajetória da câmera (padrão: 81, passo: 4) | INT | Sim | 1 a RESOLUÇÃO_MÁXIMA |
| `velocidade` | A velocidade do movimento da câmera (padrão: 1.0, passo: 0.1) | FLOAT | Não | 0.0 a 10.0 |
| `fx` | O parâmetro de distância focal x (padrão: 0.5, passo: 0.000000001) | FLOAT | Não | 0.0 a 1.0 |
| `fy` | O parâmetro de distância focal y (padrão: 0.5, passo: 0.000000001) | FLOAT | Não | 0.0 a 1.0 |
| `cx` | A coordenada x do ponto principal (padrão: 0.5, passo: 0.01) | FLOAT | Não | 0.0 a 1.0 |
| `cy` | A coordenada y do ponto principal (padrão: 0.5, passo: 0.01) | FLOAT | Não | 0.0 a 1.0 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `camera_embedding` | O tensor de embedding de câmera gerado contendo a sequência de trajetória | TENSOR |
| `largura` | O valor de largura utilizado para o processamento | INT |
| `altura` | O valor de altura utilizado para o processamento | INT |
| `duração` | O valor de comprimento utilizado para o processamento | INT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanCameraEmbedding/pt-BR.md)

---
**Source fingerprint (SHA-256):** `422c4a1fdfb6fd403afac26a609f80cbdbaa87f2c115068de9d7a33c756e71fd`

# StableZero123_Conditioning

O nó StableZero123_Conditioning processa uma imagem de entrada e ângulos de câmera para gerar dados de condicionamento e representações latentes para a geração de modelos 3D. Ele usa um modelo de visão CLIP para codificar as características da imagem, combina-as com informações de embedding da câmera baseadas em ângulos de elevação e azimute, e produz condicionamento positivo e negativo juntamente com uma representação latente para tarefas downstream de geração 3D.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `clip_vision` | O modelo de visão CLIP usado para codificar características da imagem | CLIP_VISION | Sim | - |
| `init_image` | A imagem de entrada a ser processada e codificada | IMAGE | Sim | - |
| `vae` | O modelo VAE usado para codificar pixels no espaço latente | VAE | Sim | - |
| `width` | Largura de saída para a representação latente (padrão: 256, deve ser divisível por 8) | INT | Sim | 16 to MAX_RESOLUTION |
| `height` | Altura de saída para a representação latente (padrão: 256, deve ser divisível por 8) | INT | Sim | 16 to MAX_RESOLUTION |
| `batch_size` | Número de amostras a serem geradas no lote (padrão: 1) | INT | Sim | 1 to 4096 |
| `elevation` | Ângulo de elevação da câmera em graus (padrão: 0.0) | FLOAT | Sim | -180.0 to 180.0 |
| `azimuth` | Ângulo de azimute da câmera em graus (padrão: 0.0) | FLOAT | Sim | -180.0 to 180.0 |

**Nota:** Os parâmetros `width` e `height` devem ser divisíveis por 8, pois o nó os divide automaticamente por 8 para criar as dimensões da representação latente.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `positive` | Dados de condicionamento positivo que combinam características da imagem e embeddings da câmera | CONDITIONING |
| `negative` | Dados de condicionamento negativo com características inicializadas em zero | CONDITIONING |
| `latent` | Representação latente com dimensões [batch_size, 4, height//8, width//8] | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableZero123_Conditioning/pt-BR.md)

---
**Source fingerprint (SHA-256):** `a694610c9f22fe0dab3ae02f4aabb33e3de8e5031c82dff5e8ba232c098f4a1d`

# StableZero123_Conditioning_Batched

O nó StableZero123_Conditioning_Batched prepara os dados de condicionamento necessários para gerar visualizações 3D de um objeto com o modelo Stable Zero123. Ele codifica uma imagem de entrada com um modelo de visão CLIP e um VAE, combina os recursos da imagem com os ângulos de elevação e azimute da câmera para cada item de um lote e gera o condicionamento positivo e negativo juntamente com um latente vazio. Os incrementos do lote aumentam ou diminuem o ângulo da câmera para cada item consecutivo no lote.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `clip_vision` | O modelo de visão CLIP usado para codificar a imagem de entrada em embeddings de imagem | CLIP_VISION | Sim | - |
| `init_image` | A imagem inicial de entrada a ser processada e codificada | IMAGE | Sim | - |
| `vae` | O modelo VAE usado para codificar os pixels da imagem no espaço latente | VAE | Sim | - |
| `width` | Largura alvo da imagem processada (padrão: 256) | INT | Sim | 16 a MAX_RESOLUTION (passo 8) |
| `height` | Altura alvo da imagem processada (padrão: 256) | INT | Sim | 16 a MAX_RESOLUTION (passo 8) |
| `batch_size` | Número de amostras de condicionamento a serem geradas no lote (padrão: 1) | INT | Sim | 1 a 4096 |
| `elevation` | Ângulo inicial de elevação da câmera em graus (padrão: 0.0) | FLOAT | Sim | -180.0 a 180.0 (passo 0.1) |
| `azimuth` | Ângulo inicial de azimute da câmera em graus (padrão: 0.0) | FLOAT | Sim | -180.0 a 180.0 (passo 0.1) |
| `elevation_batch_increment` | Valor adicionado ao ângulo de elevação para cada item consecutivo no lote (padrão: 0.0, parâmetro avançado) | FLOAT | Sim | -180.0 a 180.0 (passo 0.1) |
| `azimuth_batch_increment` | Valor adicionado ao ângulo de azimute para cada item consecutivo no lote (padrão: 0.0, parâmetro avançado) | FLOAT | Sim | -180.0 a 180.0 (passo 0.1) |

**Observação:** Os valores de `width` e `height` devem ser múltiplos de 8 (o passo de seleção de 8 garante isso) porque o nó os divide por 8 para construir as dimensões latentes. Para cada item no lote, os valores de `elevation` e `azimuth` são aumentados por `elevation_batch_increment` e `azimuth_batch_increment`, de modo que itens consecutivos do lote recebem ângulos de câmera incrementalmente.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `positive` | Condicionamento positivo que combina os embeddings da imagem, os embeddings da câmera e a imagem de entrada codificada usada para concatenação durante a geração | CONDITIONING |
| `negative` | Condicionamento negativo que usa embeddings de imagem inicializados em zero e um latente zero para concatenação | CONDITIONING |
| `latent` | Tensor latente vazio com dimensões (batch_size, 4, height/8, width/8) e informações de índice do lote | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableZero123_Conditioning_Batched/pt-BR.md)

---
**Source fingerprint (SHA-256):** `94fc53dace8f294a746c47f8aa0da145f3e7beeb77a95912a38f0037ac094292`

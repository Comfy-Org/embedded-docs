# StableZero123_Conditioning

O nó StableZero123_Conditioning processa uma imagem de entrada e ângulos de câmera para gerar dados de condicionamento e representações latentes para geração de modelos 3D. Ele usa um modelo de visão CLIP para codificar as características da imagem, combina-as com informações de embedding de câmera com base nos ângulos de elevação e azimute e produz condicionamento positivo e negativo, juntamente com uma representação latente para tarefas posteriores de geração 3D.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `clip_vision` | O modelo de visão CLIP usado para codificar as características da imagem | CLIP_VISION | Sim | - |
| `imagem_inicial` | A imagem de entrada a ser processada e codificada | IMAGE | Sim | - |
| `vae` | O modelo VAE usado para codificar pixels no espaço latente | VAE | Sim | - |
| `largura` | Largura de saída para a representação latente (padrão: 256, passo: 8) | INT | Sim | 16 a MAX_RESOLUTION |
| `altura` | Altura de saída para a representação latente (padrão: 256, passo: 8) | INT | Sim | 16 a MAX_RESOLUTION |
| `tamanho_do_lote` | Número de amostras a gerar no lote (padrão: 1) | INT | Sim | 1 a 4096 |
| `elevação` | Ângulo de elevação da câmera em graus (padrão: 0.0, passo: 0.1) | FLOAT | Sim | -180.0 a 180.0 |
| `azimute` | Ângulo de azimute da câmera em graus (padrão: 0.0, passo: 0.1) | FLOAT | Sim | -180.0 a 180.0 |

**Nota:** Os parâmetros `width` e `height` usam um passo de 8, então os valores são definidos em incrementos de 8. O nó os divide por 8 para determinar as dimensões da representação latente. A imagem é redimensionada para a `width` e a `height` fornecidas usando ampliação bilinear com recorte central antes da codificação pelo VAE.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `positive` | Dados de condicionamento positivo que combinam características da imagem e embeddings de câmera, incluindo a imagem de entrada codificada pelo VAE como um latente para concatenar | CONDITIONING |
| `negative` | Dados de condicionamento negativo com características inicializadas com zero e um latente inicializado com zero | CONDITIONING |
| `latent` | Representação latente inicializada com zero com dimensões [batch_size, 4, height//8, width//8] | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableZero123_Conditioning/pt-BR.md)

---
**Source fingerprint (SHA-256):** `a694610c9f22fe0dab3ae02f4aabb33e3de8e5031c82dff5e8ba232c098f4a1d`

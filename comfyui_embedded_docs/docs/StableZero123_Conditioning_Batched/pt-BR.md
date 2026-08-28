# StableZero123_Conditioning_Batched

O nó `StableZero123_Conditioning_Batched` prepara dados de condicionamento para a geração de um modelo 3D a partir de uma única imagem de entrada. Ele codifica a imagem com um modelo de visão CLIP e um VAE, combina as características visuais com embeddings de câmera construídos a partir dos ângulos de elevação e azimute, e produz condicionamento positivo, negativo e um tensor latente para um lote de amostras. Quando `batch_size` é maior que 1, os ângulos de elevação e azimute são aumentados pelos respectivos valores de incremento do lote para cada item do lote.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|---------------|-------------|-----------|
| `clip_vision` | O modelo de visão CLIP usado para codificar a imagem de entrada | CLIP_VISION | Sim | - |
| `imagem_inicial` | A imagem inicial de entrada a ser processada e codificada | IMAGE | Sim | - |
| `vae` | O modelo VAE usado para codificar os pixels da imagem no espaço latente | VAE | Sim | - |
| `largura` | A largura de saída da imagem processada (padrão: 256) | INT | Sim | 16 a MAX_RESOLUTION (passo de 8) |
| `altura` | A altura de saída da imagem processada (padrão: 256) | INT | Sim | 16 a MAX_RESOLUTION (passo de 8) |
| `tamanho_do_lote` | O número de amostras de condicionamento a serem geradas no lote (padrão: 1) | INT | Sim | 1 a 4096 |
| `elevação` | O ângulo inicial de elevação da câmera em graus (padrão: 0.0) | FLOAT | Sim | -180.0 a 180.0 |
| `azimute` | O ângulo inicial de azimute da câmera em graus (padrão: 0.0) | FLOAT | Sim | -180.0 a 180.0 |
| `incremento_de_lote_de_elevacao` | O valor de incremento da elevação para cada item do lote (padrão: 0.0) | FLOAT | Sim | -180.0 a 180.0 |
| `incremento_de_lote_de_azimute` | O valor de incremento do azimute para cada item do lote (padrão: 0.0) | FLOAT | Sim | -180.0 a 180.0 |

**Nota:** Os valores de `width` e `height` devem ser múltiplos de 8, pois o nó divide essas dimensões por 8 internamente ao construir o tensor latente.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|---------------|-------------|---------------|
| `positivo` | Os dados de condicionamento positivo contendo os embeddings da imagem e os embeddings de câmera para cada item do lote | CONDITIONING |
| `negativo` | Os dados de condicionamento negativo com embeddings inicializados em zero | CONDITIONING |
| `latente` | Um tensor latente inicializado em zero com dimensões batch_size x 4 x height/8 x width/8, juntamente com informações de indexação do lote | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableZero123_Conditioning_Batched/pt-BR.md)

---
**Source fingerprint (SHA-256):** `94fc53dace8f294a746c47f8aa0da145f3e7beeb77a95912a38f0037ac094292`

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableZero123_Conditioning_Batched/pt-BR.md)

O nó **StableZero123_Conditioning_Batched** processa uma imagem de entrada e gera dados de condicionamento para a geração de modelos 3D. Ele codifica a imagem usando modelos CLIP vision e VAE, em seguida, cria embeddings de câmera com base nos ângulos de elevação e azimute para produzir condicionamentos positivo e negativo, juntamente com representações latentes para processamento em lote.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `clip_vision` | CLIP_VISION | Sim | - | O modelo de visão CLIP usado para codificar a imagem de entrada |
| `imagem_inicial` | IMAGE | Sim | - | A imagem de entrada inicial a ser processada e codificada |
| `vae` | VAE | Sim | - | O modelo VAE usado para codificar pixels da imagem no espaço latente |
| `largura` | INT | Não | 16 a MAX_RESOLUTION | A largura de saída para a imagem processada (padrão: 256, deve ser divisível por 8) |
| `altura` | INT | Não | 16 a MAX_RESOLUTION | A altura de saída para a imagem processada (padrão: 256, deve ser divisível por 8) |
| `tamanho_do_lote` | INT | Não | 1 a 4096 | O número de amostras de condicionamento a serem geradas no lote (padrão: 1) |
| `elevação` | FLOAT | Não | -180.0 a 180.0 | O ângulo inicial de elevação da câmera em graus (padrão: 0.0) |
| `azimute` | FLOAT | Não | -180.0 a 180.0 | O ângulo inicial de azimute da câmera em graus (padrão: 0.0) |
| `incremento_de_lote_de_elevacao` | FLOAT | Não | -180.0 a 180.0 | O incremento de elevação para cada item do lote (padrão: 0.0) |
| `incremento_de_lote_de_azimute` | FLOAT | Não | -180.0 a 180.0 | O incremento de azimute para cada item do lote (padrão: 0.0) |

**Nota:** Os parâmetros `width` e `height` devem ser divisíveis por 8, pois o nó divide internamente essas dimensões por 8 para a geração do espaço latente.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `positive` | CONDITIONING | Os dados de condicionamento positivo contendo embeddings de imagem e parâmetros de câmera |
| `negative` | CONDITIONING | Os dados de condicionamento negativo com embeddings inicializados em zero |
| `latent` | LATENT | A representação latente da imagem processada com informações de indexação do lote |

---
**Source fingerprint (SHA-256):** `2b770f7a168a0d3e33da8bfa63383080709fa5d53846dbf6a4374bd1ef1746aa`

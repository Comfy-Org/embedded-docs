O nó **StableZero123_Conditioning_Batched** processa uma imagem de entrada e gera dados de condicionamento para a geração de modelos 3D. Ele codifica a imagem usando modelos CLIP vision e VAE, em seguida, cria embeddings de câmera com base nos ângulos de elevação e azimute para produzir condicionamentos positivo e negativo, juntamente com representações latentes para processamento em lote.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `clip_vision` | O modelo de visão CLIP usado para codificar a imagem de entrada | CLIP_VISION | Sim | - |
| `imagem_inicial` | A imagem de entrada inicial a ser processada e codificada | IMAGE | Sim | - |
| `vae` | O modelo VAE usado para codificar pixels da imagem no espaço latente | VAE | Sim | - |
| `largura` | A largura de saída para a imagem processada (padrão: 256, deve ser divisível por 8) | INT | Não | 16 a MAX_RESOLUTION |
| `altura` | A altura de saída para a imagem processada (padrão: 256, deve ser divisível por 8) | INT | Não | 16 a MAX_RESOLUTION |
| `tamanho_do_lote` | O número de amostras de condicionamento a serem geradas no lote (padrão: 1) | INT | Não | 1 a 4096 |
| `elevação` | O ângulo inicial de elevação da câmera em graus (padrão: 0.0) | FLOAT | Não | -180.0 a 180.0 |
| `azimute` | O ângulo inicial de azimute da câmera em graus (padrão: 0.0) | FLOAT | Não | -180.0 a 180.0 |
| `incremento_de_lote_de_elevacao` | O incremento de elevação para cada item do lote (padrão: 0.0) | FLOAT | Não | -180.0 a 180.0 |
| `incremento_de_lote_de_azimute` | O incremento de azimute para cada item do lote (padrão: 0.0) | FLOAT | Não | -180.0 a 180.0 |

**Nota:** Os parâmetros `width` e `height` devem ser divisíveis por 8, pois o nó divide internamente essas dimensões por 8 para a geração do espaço latente.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `positive` | Os dados de condicionamento positivo contendo embeddings de imagem e parâmetros de câmera | CONDITIONING |
| `negative` | Os dados de condicionamento negativo com embeddings inicializados em zero | CONDITIONING |
| `latent` | A representação latente da imagem processada com informações de indexação do lote | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableZero123_Conditioning_Batched/pt-BR.md)

---
**Source fingerprint (SHA-256):** `2b770f7a168a0d3e33da8bfa63383080709fa5d53846dbf6a4374bd1ef1746aa`

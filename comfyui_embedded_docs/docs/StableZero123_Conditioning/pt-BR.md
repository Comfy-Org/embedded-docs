> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableZero123_Conditioning/pt-BR.md)

O nó StableZero123_Conditioning processa uma imagem de entrada e ângulos de câmera para gerar dados de condicionamento e representações latentes para geração de modelos 3D. Ele utiliza um modelo de visão CLIP para codificar as características da imagem, combina-as com informações de incorporação da câmera baseadas nos ângulos de elevação e azimute, e produz condicionamentos positivo e negativo juntamente com uma representação latente para tarefas subsequentes de geração 3D.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `clip_vision` | CLIP_VISION | Sim | - | O modelo de visão CLIP usado para codificar as características da imagem |
| `init_image` | IMAGE | Sim | - | A imagem de entrada a ser processada e codificada |
| `vae` | VAE | Sim | - | O modelo VAE usado para codificar pixels no espaço latente |
| `width` | INT | Não | 16 a MAX_RESOLUTION | Largura de saída para a representação latente (padrão: 256, deve ser divisível por 8) |
| `height` | INT | Não | 16 a MAX_RESOLUTION | Altura de saída para a representação latente (padrão: 256, deve ser divisível por 8) |
| `batch_size` | INT | Não | 1 a 4096 | Número de amostras a serem geradas no lote (padrão: 1) |
| `elevation` | FLOAT | Não | -180.0 a 180.0 | Ângulo de elevação da câmera em graus (padrão: 0.0) |
| `azimuth` | FLOAT | Não | -180.0 a 180.0 | Ângulo de azimute da câmera em graus (padrão: 0.0) |

**Observação:** Os parâmetros `width` e `height` devem ser divisíveis por 8, pois o nó os divide automaticamente por 8 para criar as dimensões da representação latente.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Dados de condicionamento positivo que combinam características da imagem e incorporações da câmera |
| `negative` | CONDITIONING | Dados de condicionamento negativo com características inicializadas como zero |
| `latent` | LATENT | Representação latente com dimensões [batch_size, 4, height//8, width//8] |

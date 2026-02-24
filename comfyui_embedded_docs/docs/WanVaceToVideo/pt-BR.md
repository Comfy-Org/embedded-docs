> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanVaceToVideo/pt-BR.md)

O nó WanVaceToVideo processa dados de condicionamento de vídeo para modelos de geração de vídeo. Ele recebe entradas de condicionamento positivo e negativo juntamente com dados de controle de vídeo e prepara representações latentes para a geração de vídeo. O nó lida com upscaling de vídeo, máscaras e codificação VAE para criar a estrutura de condicionamento apropriada para modelos de vídeo.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Sim | - | Entrada de condicionamento positivo para guiar a geração |
| `negative` | CONDITIONING | Sim | - | Entrada de condicionamento negativo para guiar a geração |
| `vae` | VAE | Sim | - | Modelo VAE usado para codificar imagens e quadros de vídeo |
| `width` | INT | Sim | 16 a MAX_RESOLUTION | Largura do vídeo de saída em pixels (padrão: 832, passo: 16) |
| `height` | INT | Sim | 16 a MAX_RESOLUTION | Altura do vídeo de saída em pixels (padrão: 480, passo: 16) |
| `length` | INT | Sim | 1 a MAX_RESOLUTION | Número de quadros no vídeo (padrão: 81, passo: 4) |
| `batch_size` | INT | Sim | 1 a 4096 | Número de vídeos a serem gerados simultaneamente (padrão: 1) |
| `strength` | FLOAT | Sim | 0.0 a 1000.0 | Força de controle para o condicionamento de vídeo (padrão: 1.0, passo: 0.01) |
| `control_video` | IMAGE | Não | - | Vídeo de entrada opcional para condicionamento de controle |
| `control_masks` | MASK | Não | - | Máscaras opcionais para controlar quais partes do vídeo modificar |
| `reference_image` | IMAGE | Não | - | Imagem de referência opcional para condicionamento adicional |

**Observação:** Quando `control_video` é fornecido, ele será ampliado (upscaled) para corresponder à largura e altura especificadas. Se `control_masks` for fornecido, elas devem corresponder às dimensões do vídeo de controle. A `reference_image` é codificada através do VAE e pré-anexada à sequência latente quando fornecida.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Condicionamento positivo com dados de controle de vídeo aplicados |
| `negative` | CONDITIONING | Condicionamento negativo com dados de controle de vídeo aplicados |
| `latent` | LATENT | Tensor latente vazio pronto para geração de vídeo |
| `trim_latent` | INT | Número de quadros latentes a serem cortados quando a imagem de referência é usada |

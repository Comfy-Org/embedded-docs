> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan22FunControlToVideo/pt-BR.md)

O nó Wan22FunControlToVideo prepara os condicionamentos e representações latentes para geração de vídeo usando a arquitetura do modelo de vídeo Wan. Ele processa entradas de condicionamento positivo e negativo, juntamente com imagens de referência e vídeos de controle opcionais, para criar as representações necessárias no espaço latente para a síntese de vídeo. O nó gerencia o dimensionamento espacial e as dimensões temporais para gerar dados de condicionamento apropriados para modelos de vídeo.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Sim | - | Entrada de condicionamento positivo para orientar a geração do vídeo |
| `negative` | CONDITIONING | Sim | - | Entrada de condicionamento negativo para orientar a geração do vídeo |
| `vae` | VAE | Sim | - | Modelo VAE usado para codificar imagens no espaço latente |
| `width` | INT | Não | 16 a MAX_RESOLUTION | Largura do vídeo de saída em pixels (padrão: 832, passo: 16) |
| `height` | INT | Não | 16 a MAX_RESOLUTION | Altura do vídeo de saída em pixels (padrão: 480, passo: 16) |
| `length` | INT | Não | 1 a MAX_RESOLUTION | Número de quadros na sequência de vídeo (padrão: 81, passo: 4) |
| `batch_size` | INT | Não | 1 a 4096 | Número de sequências de vídeo a serem geradas (padrão: 1) |
| `ref_image` | IMAGE | Não | - | Imagem de referência opcional para fornecer orientação visual |
| `control_video` | IMAGE | Não | - | Vídeo de controle opcional para orientar o processo de geração |

**Observação:** O parâmetro `length` é processado em blocos de 4 quadros, e o nó gerencia automaticamente o dimensionamento temporal para o espaço latente. Quando `ref_image` é fornecido, ele influencia o condicionamento através de latentes de referência. Quando `control_video` é fornecido, ele afeta diretamente a representação latente concatenada usada no condicionamento.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Condicionamento positivo modificado com dados latentes específicos para vídeo |
| `negative` | CONDITIONING | Condicionamento negativo modificado com dados latentes específicos para vídeo |
| `latent` | LATENT | Tensor latente vazio com dimensões apropriadas para geração de vídeo |

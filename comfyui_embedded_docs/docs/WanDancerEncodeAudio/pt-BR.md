> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanDancerEncodeAudio/pt-BR.md)

## Visão Geral

Este nó processa uma entrada de áudio para extrair características que podem ser usadas para orientar um modelo de geração de vídeo. Ele analisa o áudio para detectar tempo, batidas e outras características musicais, então empacota essas informações em um formato adequado para condicionar um modelo de vídeo, permitindo que o vídeo gerado seja sincronizado com o áudio.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|---------------|-------------|-----------|-----------|
| `audio` | AUDIO | Sim | - | A entrada de áudio a ser analisada e codificada. |
| `video_frames` | INT | Sim | Mín: 1, Máx: 268435456 (MAX_RESOLUTION), Passo: 4 | O número de quadros no vídeo de destino. Usado para calcular a taxa de quadros para sincronização (padrão: 149). |
| `audio_inject_scale` | FLOAT | Sim | Mín: 0.0, Máx: 10.0, Passo: 0.01 | A escala para as características de áudio quando injetadas no modelo de vídeo (padrão: 1.0). |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|---------------|---------------|-----------|
| `audio_encoder_output` | AUDIO_ENCODER_OUTPUT | Um dicionário contendo as características de áudio processadas, a taxa de quadros calculada (fps) e a escala de injeção de áudio. Esta saída é usada para condicionar o modelo de geração de vídeo. |
| `fps_string` | STRING | Uma string de texto descrevendo a taxa de quadros calculada (fps) com base na duração do áudio e no número de quadros de vídeo. Esta string é destinada a ser usada no prompt para o modelo de vídeo. |
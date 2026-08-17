# WanDancerEncodeAudio

Este nó processa uma entrada de áudio para extrair características que podem ser usadas para guiar um modelo de geração de vídeo. Ele analisa o áudio para detectar tempo, batidas e outras características musicais e, em seguida, empacota essas informações em um formato adequado para condicionar um modelo de vídeo, permitindo que o vídeo gerado seja sincronizado com o áudio.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `audio` | A entrada de áudio a ser analisada e codificada. | AUDIO | Sim | - |
| `video_frames` | O número de quadros no vídeo de destino. Usado para calcular a taxa de quadros para sincronização (padrão: 149). | INT | Sim | Min: 1, Max: 268435456 (MAX_RESOLUTION), Step: 4 |
| `audio_inject_scale` | A escala das características de áudio ao serem injetadas no modelo de vídeo (padrão: 1.0). | FLOAT | Sim | Min: 0.0, Max: 10.0, Step: 0.01 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `audio_encoder_output` | Um dicionário contendo as características de áudio processadas, a taxa de quadros calculada (fps) e a escala de injeção de áudio. Esta saída é usada para condicionar o modelo de geração de vídeo. | AUDIO_ENCODER_OUTPUT |
| `fps_string` | Uma string de texto que descreve a taxa de quadros calculada (fps) com base na duração do áudio e no número de quadros de vídeo. Esta string deve ser usada no prompt para o modelo de vídeo. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanDancerEncodeAudio/pt-BR.md)

---
**Source fingerprint (SHA-256):** `ce27a3bdea2d9e3cf8875c24236a2a0a1429e9bc13a58581e372fb669d2c0018`

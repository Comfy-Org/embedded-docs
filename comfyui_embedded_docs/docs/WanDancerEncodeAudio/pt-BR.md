# WanDancerEncodeAudio

Este nó analisa um clipe de áudio e o transforma em um conjunto de características que podem orientar um modelo de geração de vídeo. Ele estima tempo e batidas, extrai mel-espectrograma, MFCC, chroma e características de onset, depois os empacota juntamente com uma taxa de quadros calculada para sincronização.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `audio` | A entrada de áudio a ser analisada e codificada. Se o áudio tiver vários canais, os canais são combinados em mono pela média antes da extração de características. | AUDIO | Sim | - |
| `video_frames` | O número de quadros no vídeo de destino. Usado para calcular a taxa de quadros para sincronização (padrão: 149). | INT | Sim | Mín.: 1, Máx.: 16384 (MAX_RESOLUTION), Passo: 4 |
| `audio_inject_scale` | A escala das características de áudio quando injetadas no modelo de vídeo (padrão: 1.0). | FLOAT | Sim | Mín.: 0.0, Máx.: 10.0, Passo: 0.01 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `audio_encoder_output` | Um dicionário contendo as características de áudio processadas, a taxa de quadros calculada (fps) e a escala de injeção de áudio. Esta saída é usada para condicionar o modelo de geração de vídeo. | AUDIO_ENCODER_OUTPUT |
| `fps_string` | Uma string de texto que descreve a taxa de quadros calculada (fps) com base na duração do áudio e no número de quadros do vídeo. Esta string destina-se a ser usada no prompt do modelo de vídeo. Ela é formatada em chinês para corresponder ao pipeline de referência. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanDancerEncodeAudio/pt-BR.md)

---
**Source fingerprint (SHA-256):** `ce27a3bdea2d9e3cf8875c24236a2a0a1429e9bc13a58581e372fb669d2c0018`

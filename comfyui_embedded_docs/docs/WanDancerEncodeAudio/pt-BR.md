# WanDancerEncodeAudio

## Visão Geral

Este nó processa uma entrada de áudio para extrair características que podem ser usadas para guiar um modelo de geração de vídeo. Ele analisa o áudio para detectar tempo, batidas e outras características musicais, depois empacota essas informações em um formato adequado para condicionar um modelo de vídeo, permitindo que o vídeo gerado seja sincronizado com o áudio.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `áudio` | A entrada de áudio a ser analisada e codificada. | AUDIO | Sim | - |
| `quadros_de_vídeo` | O número de quadros no vídeo de destino. Usado para calcular a taxa de quadros para sincronização (padrão: 149). | INT | Sim | Mín: 1, Máx: 268435456 (MAX_RESOLUTION), Passo: 4 |
| `escala_de_injeção_de_áudio` | A escala para as características de áudio quando injetadas no modelo de vídeo (padrão: 1.0). | FLOAT | Sim | Mín: 0.0, Máx: 10.0, Passo: 0.01 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `audio_encoder_output` | Um dicionário contendo as características de áudio processadas, a taxa de quadros calculada (fps) e a escala de injeção de áudio. Esta saída é usada para condicionar o modelo de geração de vídeo. | AUDIO_ENCODER_OUTPUT |
| `fps_string` | Uma string de texto descrevendo a taxa de quadros calculada (fps) com base na duração do áudio e no número de quadros de vídeo. Esta string deve ser usada no prompt para o modelo de vídeo. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanDancerEncodeAudio/pt-BR.md)

---
**Source fingerprint (SHA-256):** `ef230c92b23a04369708041b2e5d03c1b2928edf746dc43020bae777f9f0b589`

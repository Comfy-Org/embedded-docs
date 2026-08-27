# WanDancerEncodeAudio

Este nó processa uma entrada de áudio para extrair características que podem ser usadas para guiar um modelo de geração de vídeo. Ele analisa o áudio para detectar andamento, batidas e outras características musicais e, em seguida, empacota essas informações em um formato adequado para condicionar um modelo de vídeo, permitindo que o vídeo gerado seja sincronizado com o áudio.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `áudio` | A entrada de áudio a ser analisada e codificada. Se o áudio tiver vários canais, os canais são transformados em mono por média antes da extração de características. | AUDIO | Sim | - |
| `quadros_de_vídeo` | O número de quadros no vídeo de destino. Usado para calcular a taxa de quadros para sincronização (padrão: 149). | INT | Sim | Mín: 1, Máx: 268435456 (MAX_RESOLUTION), Passo: 4 |
| `escala_de_injeção_de_áudio` | A escala para as características de áudio quando injetadas no modelo de vídeo (padrão: 1.0). | FLOAT | Sim | Mín: 0.0, Máx: 10.0, Passo: 0.01 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `saída_do_codificador_de_áudio` | Um dicionário contendo as características de áudio processadas, a taxa de quadros calculada (fps) e a escala de injeção de áudio. Esta saída é usada para condicionar o modelo de geração de vídeo. | AUDIO_ENCODER_OUTPUT |
| `string_fps` | Uma string de texto descrevendo a taxa de quadros calculada (fps) com base no comprimento do áudio e no número de quadros do vídeo. Esta string é destinada a ser usada no prompt para o modelo de vídeo. Ela está formatada em chinês para corresponder ao pipeline de referência. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanDancerEncodeAudio/pt-BR.md)

---
**Source fingerprint (SHA-256):** `ce27a3bdea2d9e3cf8875c24236a2a0a1429e9bc13a58581e372fb669d2c0018`

O nó AudioEncoderEncode processa dados de áudio codificando-os usando um modelo de codificador de áudio. Ele recebe uma entrada de áudio e a converte em uma representação codificada que pode ser usada para processamento adicional no pipeline de condicionamento. Este nó transforma formas de onda de áudio brutas em um formato adequado para aplicações de aprendizado de máquina baseadas em áudio.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Tipo de Entrada | Padrão | Intervalo |
| --- | --- | --- | --- | --- | --- |
| `audio_encoder` | O modelo de codificador de áudio usado para processar a entrada de áudio | AUDIO_ENCODER | Obrigatório | - | - |
| `áudio` | Os dados de áudio contendo informações de forma de onda e taxa de amostragem | AUDIO | Obrigatório | - | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `output` | A representação de áudio codificada gerada pelo codificador de áudio | AUDIO_ENCODER_OUTPUT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioEncoderEncode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `8de45c157937ee95fbaef06aaefe478db7be8b16088d92720d977fe3d14eee39`

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioEncoderEncode/pt-BR.md)

O nó AudioEncoderEncode processa dados de áudio codificando-os usando um modelo de codificador de áudio. Ele recebe uma entrada de áudio e a converte em uma representação codificada que pode ser usada para processamento posterior no fluxo de condicionamento. Este nó transforma formas de onda de áudio bruto em um formato adequado para aplicações de aprendizado de máquina baseadas em áudio.

## Entradas

| Parâmetro | Tipo de Dado | Tipo de Entrada | Padrão | Intervalo | Descrição |
|-----------|-----------|------------|---------|-------|-------------|
| `audio_encoder` | AUDIO_ENCODER | Obrigatório | - | - | O modelo codificador de áudio usado para processar a entrada de áudio |
| `audio` | AUDIO | Obrigatório | - | - | Os dados de áudio contendo informações da forma de onda e da taxa de amostragem |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `output` | AUDIO_ENCODER_OUTPUT | A representação de áudio codificada gerada pelo codificador de áudio |

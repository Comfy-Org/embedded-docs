# Codificar com AudioEncoder

O nó AudioEncoderEncode processa dados de áudio codificando-os usando um modelo de codificador de áudio. Ele recebe entrada de áudio e a converte em uma representação codificada que pode ser usada para processamento posterior no pipeline de condicionamento. Este nó transforma formas de onda de áudio brutas em um formato adequado para aplicações de aprendizado de máquina baseadas em áudio.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `audio_encoder` | O modelo de codificador de áudio usado para processar a entrada de áudio | AUDIO_ENCODER | Sim | - |
| `audio` | Os dados de áudio contendo informações de forma de onda e taxa de amostragem | AUDIO | Sim | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `output` | A representação de áudio codificada gerada pelo codificador de áudio | AUDIO_ENCODER_OUTPUT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioEncoderEncode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `85f77152ccc1e3f4687e2b655283e69e03d90b862d6a676dcb89ea973dd70a63`

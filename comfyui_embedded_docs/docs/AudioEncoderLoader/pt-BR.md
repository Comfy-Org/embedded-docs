# Carregar AudioEncoder

O nó **AudioEncoderLoader** carrega um modelo de codificador de áudio a partir de um arquivo na sua pasta de codificadores de áudio. Ele recebe como entrada o nome do arquivo do modelo de codificador de áudio e retorna o modelo carregado, que pode então ser utilizado para tarefas de processamento de áudio no seu fluxo de trabalho.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `audio_encoder_name` | Seleciona qual arquivo de modelo de codificador de áudio será carregado | STRING | Sim | Lista de arquivos de codificador de áudio disponíveis na pasta audio_encoders |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `audio_encoder` | O modelo de codificador de áudio carregado, pronto para uso em fluxos de trabalho de processamento de áudio | AUDIO_ENCODER |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioEncoderLoader/pt-BR.md)

---
**Source fingerprint (SHA-256):** `24cbd45198db7d950633358c29de57f56c999bc33534fabe80404528d194163c`

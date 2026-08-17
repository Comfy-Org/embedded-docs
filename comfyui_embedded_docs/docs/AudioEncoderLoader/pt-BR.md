# Carregar AudioEncoder

O nó `AudioEncoderLoader` carrega um modelo de codificador de áudio de um arquivo na sua pasta de codificadores de áudio. Ele recebe o nome do arquivo de um modelo de codificador de áudio como entrada e retorna o modelo carregado, que pode então ser usado para tarefas de processamento de áudio no seu fluxo de trabalho.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `audio_encoder_name` | Seleciona qual arquivo de modelo de codificador de áudio carregar | COMBO | Sim | Lista de arquivos de codificador de áudio disponíveis na pasta `audio_encoders` |

Nota: O arquivo selecionado deve conter um modelo de codificador de áudio válido. Se o arquivo for inválido e não contiver um modelo válido, o nó gerará um erro.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `audio_encoder` | O modelo de codificador de áudio carregado, pronto para uso em fluxos de trabalho de processamento de áudio | AUDIO_ENCODER |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioEncoderLoader/pt-BR.md)

---
**Source fingerprint (SHA-256):** `780d0c7fcf571e5ef02d273791e5d2e894baa6d5900d845ed65e9ce669769f7e`

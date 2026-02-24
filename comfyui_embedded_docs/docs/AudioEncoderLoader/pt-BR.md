> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioEncoderLoader/pt-BR.md)

O nó AudioEncoderLoader carrega modelos de codificador de áudio a partir dos seus arquivos de codificador de áudio disponíveis. Ele recebe um nome de arquivo de codificador de áudio como entrada e retorna um modelo de codificador de áudio carregado que pode ser usado para tarefas de processamento de áudio no seu fluxo de trabalho.

## Entradas

| Parâmetro | Tipo de Dado | Tipo de Entrada | Padrão | Intervalo | Descrição |
|-----------|-----------|------------|---------|-------|-------------|
| `audio_encoder_name` | STRING | COMBO | - | Arquivos de codificador de áudio disponíveis | Seleciona qual arquivo de modelo de codificador de áudio carregar da sua pasta `audio_encoders` |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `audio_encoder` | AUDIO_ENCODER | Retorna o modelo de codificador de áudio carregado para uso em fluxos de trabalho de processamento de áudio |

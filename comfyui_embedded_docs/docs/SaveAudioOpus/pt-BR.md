> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudioOpus/pt-BR.md)

O nó SaveAudioOpus salva dados de áudio em um arquivo no formato Opus. Ele recebe uma entrada de áudio e a exporta como um arquivo Opus comprimido com configurações de qualidade ajustáveis. O nó gerencia automaticamente a nomeação do arquivo e salva a saída no diretório de saída designado.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `audio` | AUDIO | Sim | - | Os dados de áudio a serem salvos como um arquivo Opus |
| `filename_prefix` | STRING | Não | - | O prefixo para o nome do arquivo de saída (padrão: "audio/ComfyUI") |
| `quality` | COMBO | Não | "64k"<br>"96k"<br>"128k"<br>"192k"<br>"320k" | A configuração de qualidade de áudio para o arquivo Opus (padrão: "128k") |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| - | - | Este nó não retorna nenhum valor de saída. Sua função principal é salvar o arquivo de áudio no disco. |

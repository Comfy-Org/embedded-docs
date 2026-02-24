> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudioMP3/pt-BR.md)

O nó SaveAudioMP3 salva dados de áudio como um arquivo MP3. Ele recebe uma entrada de áudio e a exporta para o diretório de saída especificado, com configurações personalizáveis de nome de arquivo e qualidade. O nó gerencia automaticamente a nomeação do arquivo e a conversão de formato para criar um arquivo MP3 reproduzível.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `audio` | AUDIO | Sim | - | Os dados de áudio a serem salvos como um arquivo MP3 |
| `filename_prefix` | STRING | Não | - | O prefixo para o nome do arquivo de saída (padrão: "audio/ComfyUI") |
| `quality` | STRING | Não | "V0"<br>"128k"<br>"320k" | A configuração de qualidade de áudio para o arquivo MP3 (padrão: "V0") |
| `prompt` | PROMPT | Não | - | Dados internos do prompt (fornecidos automaticamente pelo sistema) |
| `extra_pnginfo` | EXTRA_PNGINFO | Não | - | Informações PNG adicionais (fornecidas automaticamente pelo sistema) |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| *Nenhuma* | - | Este nó não retorna nenhum dado de saída, mas salva o arquivo de áudio no diretório de saída |

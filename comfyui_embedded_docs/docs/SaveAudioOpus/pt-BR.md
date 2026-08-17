# Salvar Áudio (Opus)

O nó SaveAudioOpus salva dados de áudio em um arquivo no formato Opus. Ele recebe uma entrada de áudio e a exporta como um arquivo Opus compactado, com configurações de qualidade ajustáveis. Este nó está obsoleto e pode ser removido em versões futuras.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `audio` | Os dados de áudio a serem salvos como arquivo Opus. O nó gera um erro se nenhum áudio for fornecido (por exemplo, quando o vídeo de origem não possui trilha de áudio). | AUDIO | Sim | - |
| `filename_prefix` | O prefixo para o nome do arquivo de saída (padrão: "audio/ComfyUI") | STRING | Não | - |
| `quality` | A configuração de qualidade (bitrate) do áudio para o arquivo Opus (padrão: "128k") | COMBO | Não | "64k"<br>"96k"<br>"128k"<br>"192k"<br>"320k" |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `audio` | Os dados de áudio de entrada, retornados após o arquivo Opus ser salvo no disco. | AUDIO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudioOpus/pt-BR.md)

---
**Source fingerprint (SHA-256):** `a2f585f45299759738fa85f6b73f51680d4e86da57d3fc9c2236e66114fa3d6c`

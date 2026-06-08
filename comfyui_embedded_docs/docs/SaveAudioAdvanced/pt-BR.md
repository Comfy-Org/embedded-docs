# Salvar Áudio (Avançado)

Salva o áudio de entrada no diretório de saída do ComfyUI. Este nó permite exportar áudio em vários formatos, incluindo FLAC, MP3 e Opus, com configurações de qualidade ajustáveis.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `audio` | O áudio a ser salvo. | AUDIO | Sim | - |
| `filename_prefix` | O prefixo para o arquivo a ser salvo. Pode incluir tokens de formatação como %date:yyyy-MM-dd%. (padrão: "audio/ComfyUI") | STRING | Sim | - |
| `format` | O formato de arquivo no qual salvar o áudio. | COMBO | Sim | "flac"<br>"mp3"<br>"opus" |

Quando "mp3" é selecionado como formato, um subparâmetro `quality` fica disponível com as seguintes opções: "V0", "128k", "320k" (padrão: "V0").

Quando "opus" é selecionado como formato, um subparâmetro `quality` fica disponível com as seguintes opções: "64k", "96k", "128k", "192k", "320k" (padrão: "128k").

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|-------------|-------------|-----------|
| `ui` | Saída da interface contendo as informações do arquivo de áudio salvo. | UI |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudioAdvanced/pt-BR.md)

---
**Source fingerprint (SHA-256):** `98314263dd84c562e7c02ba89f3d10551fcb898ac784af2aa397ca8357e4aae8`

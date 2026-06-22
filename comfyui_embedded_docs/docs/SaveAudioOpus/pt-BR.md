# Salvar Áudio (Opus)

O nó SaveAudioOpus salva dados de áudio em um arquivo no formato Opus. Ele recebe entrada de áudio e a exporta como um arquivo Opus compactado com configurações de qualidade ajustáveis. O nó gerencia automaticamente a nomeação do arquivo e salva a saída no diretório de saída designado.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `áudio` | Os dados de áudio a serem salvos como um arquivo Opus | AUDIO | Sim | - |
| `prefixo_do_arquivo` | O prefixo para o nome do arquivo de saída (padrão: "audio/ComfyUI") | STRING | Não | - |
| `qualidade` | A configuração de qualidade de áudio para o arquivo Opus (padrão: "128k") | COMBO | Não | "64k"<br>"96k"<br>"128k"<br>"192k"<br>"320k" |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| - | Este nó não retorna nenhum valor de saída. Sua função principal é salvar o arquivo de áudio no disco. | - |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudioOpus/pt-BR.md)

---
**Source fingerprint (SHA-256):** `87c3b1b85ca51b79d43c8486eeb2de7b074faa11c4da2bff7b8931a3049560e2`

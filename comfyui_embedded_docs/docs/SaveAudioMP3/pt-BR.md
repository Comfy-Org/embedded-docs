# Salvar Áudio (MP3)

O nó SaveAudioMP3 salva dados de áudio como um arquivo MP3. Ele recebe uma entrada de áudio e a exporta para o diretório de saída especificado, com nome de arquivo e configurações de qualidade personalizáveis. O nó gerencia automaticamente a nomeação do arquivo e a conversão de formato para criar um arquivo MP3 reproduzível.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `áudio` | Os dados de áudio a serem salvos como um arquivo MP3 | AUDIO | Sim | - |
| `prefixo_do_arquivo` | O prefixo para o nome do arquivo de saída (padrão: "audio/ComfyUI") | STRING | Não | - |
| `qualidade` | A configuração de qualidade de áudio para o arquivo MP3 (padrão: "V0") | STRING | Não | "V0"<br>"128k"<br>"320k" |
| `prompt` | Dados internos do prompt (fornecidos automaticamente pelo sistema) | PROMPT | Não | - |
| `extra_pnginfo` | Informações adicionais de PNG (fornecidas automaticamente pelo sistema) | EXTRA_PNGINFO | Não | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| *Nenhum* | Este nó não retorna nenhum dado de saída, mas salva o arquivo de áudio no diretório de saída | - |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudioMP3/pt-BR.md)

---
**Source fingerprint (SHA-256):** `70b960cc9c86ad9a4c98e643f40e6caaafdeb9840ac72a5f8e59533fd6120e3e`

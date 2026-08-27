# Salvar Áudio (FLAC)

Este nó salva dados de áudio em um arquivo no formato FLAC. Ele recebe uma entrada de áudio e a grava no diretório de saída usando o prefixo de nome de arquivo especificado. Este nó está obsoleto e deve ser substituído pelo nó Save Audio atual.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `áudio` | Os dados de áudio a serem salvos | AUDIO | Sim | - |
| `prefixo_do_arquivo` | O prefixo para o nome do arquivo de saída (padrão: "audio/ComfyUI") | STRING | Não | - |

*Nota: Os parâmetros `prompt` e `extra_pnginfo` são ocultos e tratados automaticamente pelo sistema.*

Se a entrada `audio` não receber dados (por exemplo, quando o vídeo de origem não possui trilha de áudio), o nó gera um erro e nenhum arquivo é salvo.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `áudio` | Os dados de áudio fornecidos à entrada, repassados após o arquivo ser salvo | AUDIO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudio/pt-BR.md)

---
**Source fingerprint (SHA-256):** `6ac62d315f14213091cd179a05f0bbd51f1b1a5056bb5c06ca137d2b574d6017`

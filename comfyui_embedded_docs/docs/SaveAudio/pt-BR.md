# Salvar Áudio (FLAC)

O nó SaveAudio salva dados de áudio em um arquivo no formato FLAC. Ele recebe uma entrada de áudio, grava-a no diretório de saída usando o prefixo de nome de arquivo especificado e passa o mesmo áudio adiante como sua saída. Este nó está obsoleto e deve ser substituído pelo nó atual Save Audio.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `audio` | Os dados de áudio a serem salvos | AUDIO | Sim | - |
| `filename_prefix` | O prefixo para o nome do arquivo de saída (padrão: "audio/ComfyUI") | STRING | Não | - |

O nó gera um erro se `audio` for None, o que pode acontecer quando o vídeo de origem não possui trilha de áudio.

Os parâmetros `prompt` e `extra_pnginfo` são ocultos e manipulados automaticamente pelo sistema.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `audio` | Os mesmos dados de áudio que foram salvos no arquivo | AUDIO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudio/pt-BR.md)

---
**Source fingerprint (SHA-256):** `6ac62d315f14213091cd179a05f0bbd51f1b1a5056bb5c06ca137d2b574d6017`

# Salvar Áudio (Avançado)

Salva o áudio de entrada no seu diretório de saída do ComfyUI. Este nó permite exportar áudio em vários formatos, incluindo FLAC, MP3 e Opus, com configurações de qualidade ajustáveis.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `audio` | O áudio a ser salvo. | AUDIO | Sim | - |
| `filename_prefix` | O prefixo para o arquivo a ser salvo. Pode incluir tokens de formatação como %date:yyyy-MM-dd%. (padrão: "audio/ComfyUI") | STRING | Sim | - |
| `format` | O formato de arquivo no qual salvar o áudio. | DYNAMIC_COMBO | Sim | "flac"<br>"mp3"<br>"opus" |

### Entradas de MP3

Quando "mp3" é selecionado como formato, a seguinte configuração fica disponível.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `quality` | A qualidade de codificação do arquivo MP3 de saída. (padrão: "V0") | COMBO | Não | "V0"<br>"128k"<br>"320k" |

### Entradas do Opus

Quando "opus" é selecionado como formato, a seguinte configuração fica disponível.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `quality` | A qualidade de codificação do arquivo Opus de saída. (padrão: "128k") | COMBO | Não | "64k"<br>"96k"<br>"128k"<br>"192k"<br>"320k" |

Nota: A configuração `quality` está disponível somente quando o formato correspondente é selecionado. Quando "flac" é selecionado, nenhuma configuração adicional de qualidade está disponível.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `áudio` | O áudio de entrada, transmitido inalterado após ser salvo. | AUDIO |

O nó também retorna informações de interface contendo as informações do arquivo de áudio salvo.

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudioAdvanced/pt-BR.md)

---
**Source fingerprint (SHA-256):** `5f3af49670b485bbd31f0ed0c5667c12e9b9b23014cadcf64442a486255d0e6d`

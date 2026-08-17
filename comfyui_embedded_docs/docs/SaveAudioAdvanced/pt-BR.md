# Salvar Áudio (Avançado)

Salvar Áudio (Avançado)

Salva o áudio de entrada no seu diretório de saída do ComfyUI. Você pode exportar áudio nos formatos FLAC, MP3 ou Opus, com configurações de qualidade selecionáveis para arquivos MP3 e Opus.

## Entradas

### Entradas Comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `format` | O formato de arquivo no qual salvar o áudio. | DYNAMIC_COMBO | Sim | "flac"<br>"mp3"<br>"opus" |
| `audio` | O áudio a ser salvo. | AUDIO | Sim | - |
| `filename_prefix` | O prefixo para o arquivo a ser salvo. Pode incluir tokens de formatação como %date:yyyy-MM-dd%. (padrão: "audio/ComfyUI") | STRING | Sim | - |

### Entradas flac

O formato `flac` não requer nenhuma configuração adicional.

### Entradas mp3

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `quality` | A qualidade de codificação para arquivos MP3. (padrão: "V0") | COMBO | Sim | "V0"<br>"128k"<br>"320k" |

### Entradas opus

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `quality` | A qualidade de codificação para arquivos Opus. (padrão: "128k") | COMBO | Sim | "64k"<br>"96k"<br>"128k"<br>"192k"<br>"320k" |

**Nota:** A configuração `quality` é exibida somente quando `format` é `mp3` ou `opus`. Se nenhum valor de `quality` for fornecido, o áudio será salvo com a qualidade padrão do formato selecionado.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `audio` | O áudio de entrada, passado adiante após ser salvo. | AUDIO |
| `ui` | Saída de UI contendo as informações do arquivo de áudio salvo. | UI |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudioAdvanced/pt-BR.md)

---
**Source fingerprint (SHA-256):** `5f3af49670b485bbd31f0ed0c5667c12e9b9b23014cadcf64442a486255d0e6d`

# Salvar Vídeo

O nó SaveVideo salva um vídeo de entrada no diretório de saída do seu ComfyUI. Ele permite escolher o prefixo do nome do arquivo, o formato do vídeo e o codec, e cria automaticamente um nome de arquivo exclusivo adicionando um contador. Por padrão, o nó também armazena metadados do fluxo de trabalho no vídeo salvo.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `codec` | O codec a ser usado para o vídeo. Selecionar `h264` revela opções adicionais de codificação (padrão: "auto"). | DYNAMIC_COMBO | Sim | "auto"<br>"h264" |
| `video` | O vídeo a ser salvo. | VIDEO | Sim | - |
| `filename_prefix` | O prefixo do arquivo a ser salvo. Isso pode incluir informações de formatação como `%date:yyyy-MM-dd%` ou `%Empty Latent Image.width%` para incluir valores de nós (padrão: "video/ComfyUI"). | STRING | Sim | - |
| `format` | O formato no qual salvar o vídeo. Isso determina a extensão do arquivo do vídeo salvo (padrão: "auto"). | COMBO | Sim | "auto"<br>"mp4"<br>"webm"<br>"mkv"<br>"gif" |

### Entradas h264

Essas entradas aparecem quando `codec` está definido como `h264`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `encoding` | O modo de codificação para H.264. Automático preserva fluxos H.264 compatíveis. Re-encode aplica um CRF personalizado (padrão: "auto"). | DYNAMIC_COMBO | Não | "auto"<br>"re-encode" |
| `crf` | Valores menores produzem maior qualidade e arquivos maiores. Disponível apenas quando `encoding` está definido como `re-encode` (padrão: 23.0). | FLOAT | Sim (somente quando `encoding` estiver definido como `re-encode`) | 0.0 to 51.0 (step: 1.0) |

Nota: Se o `filename_prefix` incluir pastas, por exemplo `video/ComfyUI`, o vídeo é salvo dentro dessa subpasta do diretório de saída. O nome do arquivo é criado a partir do prefixo com um contador adicionado, por exemplo `ComfyUI_00001_.mp4`, para que arquivos existentes não sejam sobrescritos.

Nota: Quando os metadados estão ativados, o nó incorpora o prompt do fluxo de trabalho e metadados adicionais no vídeo salvo. Os metadados podem ser desativados iniciando o ComfyUI com o argumento `--disable-metadata`.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `video` | O vídeo que foi salvo, transmitido diretamente da entrada. | VIDEO |
| `ui` | Uma prévia do arquivo de vídeo salvo, incluindo o caminho do arquivo e informações da subpasta para exibição na interface do usuário. | PREVIEW_VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `c1fd5ac1043f0811951136b2d09cd59840b0c542079da9ed04c17cca7c02562b`

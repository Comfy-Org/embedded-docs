# Salvar Vídeo

O nó Save Video salva o vídeo de entrada no diretório de saída do seu ComfyUI. Você pode escolher o prefixo do nome do arquivo, o formato do contêiner, o codec de vídeo e opções de codificação, como qualidade. O nó gera automaticamente um nome de arquivo exclusivo usando um contador e pode incorporar metadados do fluxo de trabalho no arquivo salvo.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `vídeo` | O vídeo a ser salvo. | VIDEO | Sim | - |
| `prefixo_do_arquivo` | O prefixo para o arquivo a ser salvo. Pode incluir informações de formatação, como `%date:yyyy-MM-dd%` ou `%Empty Latent Image.width%`, para incluir valores de nós (padrão: `video/ComfyUI`). | STRING | Sim | - |
| `formato` | O contêiner de saída. Auto usa MP4 para Auto/H.264 e WebM para AV1. MP4, MKV e WebM selecionam um contêiner específico. Selecionar um formato também determina quais opções de codec estão disponíveis (padrão: `auto`). | DYNAMIC_COMBO | Sim | `"auto"`<br>`"mp4"`<br>`"mkv"`<br>`"webm"` |
| `codec` | O codec de vídeo de saída. Auto preserva um fluxo de origem compatível. A re-codificação H.264 e AV1 suporta SDR, HDR (HLG) e HDR PQ. Aparece depois que um formato é selecionado (padrão: `auto`). | DYNAMIC_COMBO | Não | `"auto"`<br>`"h264"`<br>`"av1"` |

### Entradas H.264

Estas entradas aparecem quando `codec` é `"h264"` e estão disponíveis com os formatos `auto`, `mp4` e `mkv`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `encoding` | Automático preserva fluxos H.264 compatíveis. Re-encode aplica opções de codificação personalizadas. | DYNAMIC_COMBO | Não | `"auto"`<br>`"re-encode"` |
| `crf` | Valores menores produzem maior qualidade e arquivos maiores. Aparece quando `encoding` é `"re-encode"` (padrão: 23.0). | FLOAT | Não | 0.0 a 51.0 |

### Entradas AV1

Estas entradas aparecem quando `codec` é `"av1"` e estão disponíveis com os formatos `auto`, `mp4`, `mkv` e `webm`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `encoding` | Automático preserva fluxos AV1 compatíveis. Re-encode aplica opções de codificação personalizadas. | DYNAMIC_COMBO | Não | `"auto"`<br>`"re-encode"` |
| `crf` | Valores menores produzem maior qualidade e arquivos maiores. Aparece quando `encoding` é `"re-encode"` (padrão: 30.0). | FLOAT | Não | 0.0 a 63.0 |

Nota: Quando `format` é `"auto"`, o contêiner salvo é escolhido automaticamente: `av1` produz WebM, enquanto `auto` e `h264` produzem MP4. O formato `webm` permite apenas os codecs `auto` e `av1`. Quando `codec` é `"auto"`, o fluxo de vídeo de origem é preservado em vez de ser re-codificado. O arquivo salvo usa um sufixo de contador para evitar sobrescrever arquivos existentes.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `vídeo` | O vídeo de entrada, inalterado. | VIDEO |
| `ui` | Uma prévia do arquivo de vídeo salvo, incluindo o caminho do arquivo e informações de subpasta para exibição na interface do usuário. | PREVIEW_VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `8078f692b5c366447a1b08f351637baff901e489f2389e7a26c945661f75c37a`

# Salvar Vídeo

O nó Save Video salva o vídeo de entrada no diretório de saída do ComfyUI. Você pode escolher o prefixo do nome do arquivo, o formato do contêiner, o codec de vídeo e opções de codificação, como qualidade. O nó gera automaticamente um nome de arquivo exclusivo usando um contador e pode incorporar metadados do workflow no arquivo salvo.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `vídeo` | O vídeo a ser salvo. | VIDEO | Sim | - |
| `prefixo_do_arquivo` | O prefixo do arquivo a ser salvo. Pode incluir informações de formatação, como `%date:yyyy-MM-dd%` ou `%Empty Latent Image.width%`, para incluir valores de nós (padrão: `video/ComfyUI`). | STRING | Sim | - |
| `formato` | O contêiner de saída. O modo Auto usa MOV para ProRes, WebM para AV1 e MP4 nos demais casos. MP4, MKV, WebM e MOV selecionam um contêiner específico. Selecionar um formato também determina quais opções de codec estão disponíveis (padrão: `auto`). | DYNAMIC_COMBO | Sim | `"auto"`<br>`"mp4"`<br>`"mkv"`<br>`"webm"`<br>`"mov"` |
| `codec` | O codec de vídeo de saída. O modo Auto preserva um fluxo de origem compatível. A recodificação em H.264 e AV1 oferece suporte a SDR, HDR (HLG) e HDR PQ. Este seletor fica aninhado sob o formato escolhido (padrão: `auto`). | DYNAMIC_COMBO | Não | `"auto"`<br>`"h264"`<br>`"av1"` (não disponível com o formato `webm`)<br>`"prores"` (somente com os formatos `auto`, `mkv` e `mov`) |

### Entradas do H.264

Estas entradas aparecem quando `codec` é `"h264"` e estão disponíveis com os formatos `auto`, `mp4` e `mkv`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `encoding` | Automático preserva fluxos H.264 compatíveis. Recodificar aplica opções de codificação personalizadas. | DYNAMIC_COMBO | Não | `"auto"`<br>`"re-encode"` |
| `crf` | Valores mais baixos produzem maior qualidade e arquivos maiores. Aparece quando `encoding` é `"re-encode"` (padrão: 23.0). | FLOAT | Não | 0.0 a 51.0 |

### Entradas do AV1

Estas entradas aparecem quando `codec` é `"av1"` e estão disponíveis com os formatos `auto`, `mp4`, `mkv` e `webm`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `encoding` | Automático preserva fluxos AV1 compatíveis. Recodificar aplica opções de codificação personalizadas. | DYNAMIC_COMBO | Não | `"auto"`<br>`"re-encode"` |
| `crf` | Valores mais baixos produzem maior qualidade e arquivos maiores. Aparece quando `encoding` é `"re-encode"` (padrão: 30.0). | FLOAT | Não | 0.0 a 63.0 |

Nota: Quando `format` é `"auto"`, o contêiner salvo é escolhido automaticamente: `av1` produz WebM, `prores` produz MOV, enquanto `auto` e `h264` produzem MP4. O formato `webm` permite apenas os codecs `auto` e `av1`, e o formato `mov` permite apenas `prores`. Quando `codec` é `"auto"`, o fluxo de vídeo de origem é preservado em vez de recodificado. O arquivo salvo usa um sufixo de contador para evitar sobrescrever arquivos existentes. A extensão do arquivo é determinada pelo contêiner resolvido. Metadados do workflow (o prompt e informações extras dos nós) são incorporados ao arquivo salvo, a menos que o salvamento de metadados esteja desativado na inicialização.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `video` | O vídeo de entrada, inalterado. | VIDEO |
| `ui` | Uma prévia do arquivo de vídeo salvo, incluindo o caminho do arquivo e informações da subpasta para exibição na interface. | PREVIEW_VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b8d3b6191a3e14ee305a7dd848c0988877a0b0ec8963daaff6568092a0939197`

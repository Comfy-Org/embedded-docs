# Salvar Vídeo

O nó Save Video salva o vídeo de entrada no diretório de saída do ComfyUI. Você pode escolher o prefixo do nome do arquivo, o formato do contêiner, o codec de vídeo e opções de codificação como qualidade e espaço de cor. O nó lida automaticamente com a nomeação de arquivos com incrementos de contador e pode incorporar metadados do fluxo de trabalho no arquivo salvo.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `vídeo` | O vídeo a ser salvo. | VIDEO | Sim | - |
| `prefixo_do_arquivo` | O prefixo para o arquivo a ser salvo. Pode incluir informações de formatação como `%date:yyyy-MM-dd%` ou `%Empty Latent Image.width%` para incluir valores de nós (padrão: "video/ComfyUI"). | STRING | Sim | - |
| `formato` | O contêiner de saída. Automático preserva o contêiner de origem quando possível; MP4, MKV e WebM selecionam um contêiner específico (padrão: "auto"). | DYNAMIC_COMBO | Sim | `"auto"`<br>`"mp4"`<br>`"mkv"`<br>`"webm"` |
| `codec` | O codec de vídeo de saída. Automático preserva um fluxo de origem compatível. A re-codificação H.264 e AV1 suporta SDR, HDR (HLG) e HDR PQ. Aparece quando um formato é selecionado (padrão: "auto"). | DYNAMIC_COMBO | Não | `"auto"`<br>`"h264"`<br>`"av1"` |

### Entradas de H.264

Estas entradas aparecem quando `codec` é `"h264"`. Este codec está disponível com os formatos `auto`, `mp4` e `mkv`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `encoding` | Automático preserva fluxos H.264 compatíveis. Re-codificar aplica opções de codificação personalizadas. | DYNAMIC_COMBO | Não | `"auto"`<br>`"re-encode"` |
| `crf` | Valores menores produzem maior qualidade e arquivos maiores. Aparece quando `encoding` é `"re-encode"` (padrão: 23.0). | FLOAT | Não | 0.0 a 51.0 |
| `color_space` | Automático usa sRGB para vídeos criados a partir de imagens e preserva cores reconhecidas em vídeos carregados. sRGB grava SDR BT.709/sRGB. HDR grava BT.2020/HLG de 10 bits; HDR PQ grava BT.2020/PQ. Outros pixels de entrada devem já usar o espaço de cor selecionado. Aparece quando `encoding` é `"re-encode"` (padrão: "auto"). | COMBO | Não | `"auto"`<br>`"sRGB"`<br>`"HDR"`<br>`"HDR PQ"` |

### Entradas de AV1

Estas entradas aparecem quando `codec` é `"av1"`. Este codec está disponível com os formatos `auto`, `mp4`, `mkv` e `webm`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `encoding` | Automático preserva fluxos AV1 compatíveis. Re-codificar aplica opções de codificação personalizadas. | DYNAMIC_COMBO | Não | `"auto"`<br>`"re-encode"` |
| `crf` | Valores menores produzem maior qualidade e arquivos maiores. Aparece quando `encoding` é `"re-encode"` (padrão: 30.0). | FLOAT | Não | 0.0 a 63.0 |
| `color_space` | Automático usa sRGB para vídeos criados a partir de imagens e preserva cores reconhecidas em vídeos carregados. sRGB grava SDR BT.709/sRGB. HDR grava BT.2020/HLG de 10 bits; HDR PQ grava BT.2020/PQ. Outros pixels de entrada devem já usar o espaço de cor selecionado. Aparece quando `encoding` é `"re-encode"` (padrão: "auto"). | COMBO | Não | `"auto"`<br>`"sRGB"`<br>`"HDR"`<br>`"HDR PQ"` |

Nota: O formato `webm` suporta apenas os codecs `auto` e `av1`. Quando `format` é `"auto"`, o contêiner de origem é preservado quando possível. Quando `color_space` é `"auto"`, nenhum espaço de cor explícito é aplicado e o espaço de cor é determinado automaticamente.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `vídeo` | O vídeo de entrada, inalterado. | VIDEO |
| `ui` | Uma prévia do arquivo de vídeo salvo, incluindo o caminho do arquivo e informações da subpasta para exibição na interface. | PREVIEW_VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `39b168eab2d6798adfec6ace3d4320f26217d893844ba54e62041cfdf0183e6f`

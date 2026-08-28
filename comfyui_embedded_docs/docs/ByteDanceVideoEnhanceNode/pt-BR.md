# ByteDanceVideoEnhanceNode

Este nó faz upscale e restaura vídeos usando o ByteDance vCube. Ele pode aumentar a resolução em até 8K, remover artefatos de compressão e ruído, melhorar cor e nitidez e, opcionalmente, interpolar quadros para uma taxa de quadros mais alta. O vídeo é enviado ao serviço vCube, processado com a predefinição de aprimoramento selecionada e retornado como um arquivo de vídeo aprimorado.

## Entradas

### Entradas comuns

Estas entradas estão sempre visíveis.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-------------|------------|-----------|
| `video` | Vídeo a ser aprimorado. A resolução de origem deve ser de no máximo 2560x1440 (2K); o tamanho da saída é definido pela entrada `resolution`. | VIDEO | Sim | No máximo 2560x1440 (2K) |
| `tool_version` | 'standard' equilibra velocidade e qualidade com mais de 10 algoritmos de aprimoramento. 'professional' usa mais de 30 algoritmos para restauração com qualidade de cinema, leva cerca de 3x mais tempo e custa 10x mais. | DYNAMIC_COMBO | Sim | "standard"<br>"professional" |
| `resolution` | Resolução de saída. O lado curto é definido para o nível escolhido e o lado longo segue a proporção de aspecto da origem. 'source' mantém o tamanho da origem, 'custom' define o lado curto em pixels. Vídeos de origem mais largos ou mais altos do que cerca de 2,2:1 são cobrados um nível de resolução acima. | DYNAMIC_COMBO | Sim | "720p"<br>"1080p"<br>"2k"<br>"4k"<br>"8k"<br>"source"<br>"custom" |
| `fps` | Taxa de quadros de saída. Uma taxa maior que a da origem permite interpolação de quadros por IA; uma menor descarta quadros. 'source' mantém a taxa da origem, até 120 fps. Taxas acima de 30 fps custam 2x; acima de 60 fps, 4x. (padrão: "source") | COMBO | Sim | "source" (padrão)<br>Valores numéricos de taxa de quadros até 120 fps |
| `bitrate_level` | Taxa de bits alvo do arquivo entregue, dimensionada de acordo com a resolução e a taxa de quadros de saída. (padrão: "medium") | COMBO | Sim | "low"<br>"medium"<br>"high" |

### Entradas padrão

Exibidas quando `tool_version` está definido como "standard".

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-------------|------------|-----------|
| `scene` | Predefinição ajustada ao conteúdo: 'aigc' para material de vídeo gerado por IA, 'common' para vídeo em geral, 'ugc' para clipes de celular comprimidos, 'short_series' para dramas com rostos, 'old_film' para filmagens de arquivo arranhadas ou com oscilação. (padrão: "aigc") | COMBO | Sim | "aigc"<br>"common"<br>"ugc"<br>"short_series"<br>"old_film" |
| `enhance_style` | 'hd' aplica um aprimoramento mais nítido; 'natural' reduz a intensidade para um visual mais suave e com menos nitidez. (padrão: "hd") | COMBO | Sim | "hd"<br>"natural" |

### Entradas profissionais

Exibidas quando `tool_version` está definido como "professional".

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-------------|------------|-----------|
| `enhance_style` | 'hd' aplica um aprimoramento mais nítido; 'natural' reduz a intensidade para um visual mais suave e com menos nitidez. (padrão: "hd") | COMBO | Sim | "hd"<br>"natural" |

### Entradas de resolução personalizada

Exibidas quando `resolution` está definido como "custom".

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-------------|------------|-----------|
| `short_side` | Lado curto da saída em pixels; o lado longo segue a proporção de aspecto da origem. (padrão: 1080) | INT | Sim | Padrão 1080; sujeito aos limites mínimo e máximo de lado curto do vCube |

### Notas

- O vídeo de origem deve ter no máximo 2560x1440 (2K). Vídeos maiores que isso são rejeitados e devem ser reduzidos antes de serem aprimorados.
- A duração do vídeo de origem é limitada à duração máxima suportada pelo serviço vCube.
- Quando `tool_version` é "standard", tanto `scene` quanto `enhance_style` estão disponíveis. Quando é "professional", apenas `enhance_style` está disponível.
- Quando `resolution` é "custom", o valor de `short_side` é obrigatório. As predefinições de resolução e "source" não usam `short_side`.
- Quando `resolution` é "source", a saída mantém a resolução de origem.
- Quando `fps` é "source", a taxa de quadros de saída corresponde à taxa de quadros de origem, até 120 fps.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|---------------|-------------|---------------|
| `video` | O vídeo aprimorado, com upscale e restauração na resolução e na taxa de quadros solicitadas. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceVideoEnhanceNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `bfdd55ce12cabd6e6504129084e86dcf96abd8db4ff64abbe5974c0da7a42bda`

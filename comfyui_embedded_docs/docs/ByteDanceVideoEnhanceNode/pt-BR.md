# ByteDanceVideoEnhanceNode

Este nó amplia e restaura vídeos usando o ByteDance vCube. Ele pode aumentar a resolução até 8K, remover artefatos de compressão e ruído, melhorar cor e nitidez e, opcionalmente, interpolar quadros para uma taxa de quadros mais alta. O vídeo é enviado ao serviço vCube, processado com a predefinição de aprimoramento selecionada e retornado como um arquivo de vídeo aprimorado.

## Entradas

### Entradas Comuns

Estas entradas estão sempre visíveis.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `video` | Vídeo a ser aprimorado. A resolução de origem deve ser de no máximo 2560x1440 (2K); o tamanho da saída é definido pela entrada de resolução. | VIDEO | Sim | No máximo 2560x1440 (2K) |
| `tool_version` | 'standard' equilibra velocidade e qualidade com 10+ algoritmos de aprimoramento. 'professional' usa 30+ algoritmos para restauração com qualidade de cinema, levando cerca de 3x mais tempo e custando 10x mais. | DYNAMIC_COMBO | Sim | "standard"<br>"professional" |
| `resolution` | Resolução de saída. O lado menor é definido para o nível escolhido e o lado maior segue a proporção de aspecto da origem. 'source' mantém o tamanho da origem, 'custom' define o lado menor em pixels. Origens mais largas ou mais altas que cerca de 2.2:1 são cobradas um nível de resolução acima. | DYNAMIC_COMBO | Sim | "720p"<br>"1080p"<br>"2k"<br>"4k"<br>"8k"<br>"source"<br>"custom" |
| `fps` | Taxa de quadros de saída. Uma taxa maior que a da origem permite interpolação de quadros por IA; uma menor descarta quadros. 'source' mantém a taxa da origem, até 120 fps. Taxas acima de 30 fps custam 2x, acima de 60 fps, 4x. (padrão: "source") | COMBO | Sim | "source" (padrão)<br>Taxas de quadros numéricas até 120 fps |
| `bitrate_level` | Taxa de bits alvo do arquivo entregue, dimensionada para a resolução de saída e a taxa de quadros. (padrão: "medium") | COMBO | Sim | "low"<br>"medium"<br>"high" |

### Entradas Padrão

Exibidas quando `tool_version` está definido como "standard".

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `scene` | Predefinição ajustada ao conteúdo: 'aigc' para material gerado por IA, 'common' para vídeo geral, 'ugc' para clipes de celular comprimidos, 'short_series' para dramas com rostos, 'old_film' para material de arquivo arranhado ou com cintilação. (padrão: "aigc") | COMBO | Sim | "aigc"<br>"common"<br>"ugc"<br>"short_series"<br>"old_film" |
| `enhance_style` | 'hd' aplica um aprimoramento mais nítido; 'natural' reduz a intensidade para uma aparência mais suave e menos nítida. (padrão: "hd") | COMBO | Sim | "hd"<br>"natural" |

### Entradas Profissionais

Exibidas quando `tool_version` está definido como "professional".

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `enhance_style` | 'hd' aplica um aprimoramento mais nítido; 'natural' reduz a intensidade para uma aparência mais suave e menos nítida. (padrão: "hd") | COMBO | Sim | "hd"<br>"natural" |

### Entradas de Resolução Personalizada

Exibidas quando `resolution` está definido como "custom".

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `short_side` | Lado menor da saída em pixels; o lado maior segue a proporção de aspecto da origem. (padrão: 1080) | INT | Sim | Padrão 1080; limitado pelos limites mínimo e máximo de lado menor do vCube |

### Notas

- O vídeo de origem deve ter no máximo 2560x1440 (2K). Vídeos maiores que isso são rejeitados e devem ser reduzidos antes do aprimoramento.
- A duração do vídeo de origem é limitada à duração máxima suportada pelo serviço vCube.
- Quando `tool_version` é "standard", tanto `scene` quanto `enhance_style` estão disponíveis. Quando é "professional", apenas `enhance_style` está disponível.
- Quando `resolution` é "custom", o valor de `short_side` é obrigatório. As predefinições de resolução e "source" não usam `short_side`.
- Quando `resolution` é "source", a saída mantém a resolução da origem.
- Quando `fps` é "source", a taxa de quadros de saída corresponde à taxa de quadros da origem, até 120 fps.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `video` | O vídeo aprimorado, ampliado e restaurado na resolução e taxa de quadros solicitadas. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceVideoEnhanceNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `bfdd55ce12cabd6e6504129084e86dcf96abd8db4ff64abbe5974c0da7a42bda`

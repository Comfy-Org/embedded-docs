# Reve Image Remix

O nó Reve Image Remix utiliza a API da Reve para gerar uma nova imagem. Ele combina uma ou mais imagens de referência com um prompt de texto para criar uma nova imagem remixada com base na descrição fornecida.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `model` | Versão do modelo a ser usada para o remix. | DYNAMIC_COMBO | Sim | `"reve-remix@20250915"`<br>`"reve-remix-fast@20251030"` |
| `prompt` | Descrição em texto da imagem desejada. Pode incluir tags XML img para referenciar imagens específicas por índice, ex.: `<img>0</img>`, `<img>1</img>`, etc. (padrão: vazio) | STRING | Sim | 1 a 2560 caracteres |
| `upscale` | Aumenta a escala da imagem gerada. Pode adicionar custo extra. (padrão: "disabled") | DYNAMIC_COMBO | Não | `"disabled"`<br>`"enabled"` |
| `remove_background` | Remove o fundo da imagem gerada. Pode adicionar custo extra. (padrão: false) | BOOLEAN | Não | `true`<br>`false` |
| `seed` | A semente controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente da semente. (padrão: 0) | INT | Não | 0 a 2147483647 |

### Entradas do modelo (compartilhadas por reve-remix@20250915 e reve-remix-fast@20251030)

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `aspect_ratio` | Proporção de aspecto da imagem de saída. (padrão: "auto") | COMBO | Sim | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"3:2"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"1:1"` |
| `test_time_scaling` | Valores mais altos produzem imagens melhores, mas custam mais créditos. (padrão: 1) | INT | Não | 1 a 5 |

### Entradas de upscale (aparecem quando `upscale` está definido como "enabled")

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `upscale_factor` | Fator de aumento de escala (2x, 3x ou 4x). (padrão: 2) | INT | Não | 2 a 4 |

### Entradas de referência

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | Slot expansível: conecte de 1 a 6 imagens (`image_1` a `image_6`) para usar como base visual do remix. Pelo menos uma imagem de referência é obrigatória. | IMAGE | Sim | 1 a 6 imagens |

**Observação:** O prompt deve conter entre 1 e 2560 caracteres. Quando `aspect_ratio` está definido como "auto", o serviço determina a proporção de aspecto da imagem de saída. Um valor de `test_time_scaling` igual a 1 aplica o processamento padrão; valores mais altos melhoram a qualidade da imagem, mas consomem mais créditos. O widget `upscale_factor` só aparece quando `upscale` está definido como "enabled". Os resultados do remix são não determinísticos independentemente do valor da semente. Este nó está obsoleto.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `image` | A nova imagem gerada pelo processo de remix da Reve. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReveImageRemixNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `9cf0c6653aa620179ed5d888a455fe248a240b0db04687eade6652730eb5f003`

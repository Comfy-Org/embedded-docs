# Reve Image Remix

O nó Reve Image Remix usa a API da Reve para gerar uma nova imagem. Ele combina uma ou mais imagens de referência com um prompt de texto para criar uma imagem nova, remixada, com base na descrição fornecida. Duas versões de modelo estão disponíveis, e pós-processamento opcional, como aumento de escala (upscale) ou remoção de fundo, pode ser aplicado.

## Entradas

### Entradas Comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | Versão do modelo a ser usada para remixagem. Selecionar um modelo revela suas configurações de proporção de aspecto e de escalonamento em tempo de teste. | DYNAMIC_COMBO | Sim | `reve-remix@20250915`<br>`reve-remix-fast@20251030` |
| `prompt` | Descrição textual da imagem desejada. Pode incluir tags XML `<img>` para referenciar imagens específicas por índice, por exemplo, `<img>0</img>`, `<img>1</img>`, etc. (padrão: vazio) | STRING | Sim | 1 a 2560 caracteres |
| `upscale` | Aplica aumento de escala à imagem gerada. Pode adicionar custo extra. Quando definido como "enabled", uma configuração `upscale_factor` é revelada. (padrão: "disabled") | DYNAMIC_COMBO | Não | `"disabled"`<br>`"enabled"` |
| `remove_background` | Remove o fundo da imagem gerada. Pode adicionar custo extra. (padrão: false) | BOOLEAN | Não | `true`<br>`false` |
| `seed` | A seed controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente da seed. (padrão: 0) | INT | Não | 0 a 2147483647 |

### Entradas da Versão do Modelo (compartilhadas por `reve-remix@20250915` e `reve-remix-fast@20251030`)

Ambas as versões do modelo expõem as mesmas configurações.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `aspect_ratio` | Proporção de aspecto da imagem de saída. Quando definido como "auto", a API decide automaticamente a proporção de aspecto. | COMBO | Não | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"3:2"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"1:1"` |
| `test_time_scaling` | Valores mais altos produzem imagens melhores, mas custam mais créditos. (padrão: 1; apenas valores maiores que 1 são aplicados) | INT | Não | 1 a 5 (passo 1) |

### Entradas de Referência

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | Slot expansível: conecte de 1 a 6 imagens de referência para usar como base para a remixagem (os slots são nomeados `image_1`, `image_2`, etc.). É necessária pelo menos uma imagem de referência. | IMAGE | Sim | 1 a 6 imagens |

**Nota:** O prompt deve ter entre 1 e 2560 caracteres. Quando `upscale` está definido como "enabled", a configuração aninhada `upscale_factor` aceita 2, 3 ou 4 (padrão: 2) e pode adicionar custo extra. Remover o fundo também pode adicionar custo extra.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `image` | A nova imagem gerada pelo processo de remixagem da Reve. | IMAGE |

Nota: Este nó está marcado como obsoleto.

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReveImageRemixNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `9cf0c6653aa620179ed5d888a455fe248a240b0db04687eade6652730eb5f003`

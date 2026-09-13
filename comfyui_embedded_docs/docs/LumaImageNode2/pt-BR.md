# Luma UNI-1 Image

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `prompt` | Descrição textual da imagem desejada. 1–6000 caracteres. (padrão: "") | STRING | Sim | 1 a 6000 caracteres |
| `model` | Modelo a ser usado para geração. Selecionar um modelo revela configurações adicionais para esse modelo. (padrão: primeira opção, `"uni-1"`) | DYNAMIC_COMBO | Sim | `"uni-1"`<br>`"uni-1-max"` |
| `seed` | A seed controla se o nó deve ser executado novamente; os resultados não são determinísticos independentemente da seed. (padrão: 0) | INT | Sim | 0 a 2147483647 |

### Entradas do uni-1 e uni-1-max

Compartilhadas pelas opções de modelo `uni-1` e `uni-1-max`. Essas configurações aparecem quando qualquer um dos modelos é selecionado.

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `aspect_ratio` | Proporção da imagem de saída. `"auto"` permite que o modelo escolha com base no prompt. (padrão: `"auto"`) | COMBO | Sim | `"auto"`<br>`"3:1"`<br>`"2:1"`<br>`"16:9"`<br>`"3:2"`<br>`"1:1"`<br>`"2:3"`<br>`"9:16"`<br>`"1:2"`<br>`"1:3"` |
| `style` | Predefinição de estilo. `"auto"` escolhe com base no prompt; `"manga"` aplica uma estética de mangá/anime e exige uma proporção retrato (2:3, 9:16, 1:2, 1:3). (padrão: `"auto"`) | COMBO | Sim | `"auto"`<br>`"manga"` |
| `web_search` | Pesquisar na web por referências visuais antes de gerar. (padrão: False) | BOOLEAN | Sim | True / False |

### Entradas de referência

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `image_ref` | Slot expansível: conecte de 1 a 9 itens (ex.: `image_1` a `image_9`). Até 9 imagens de referência para orientação de estilo/conteúdo. | IMAGE | Não | Até 9 imagens |

**Observação:** Se `style` estiver definido como `"manga"`, o `aspect_ratio` deve ser `"auto"` ou uma das proporções retrato `"2:3"`, `"9:16"`, `"1:2"`, `"1:3"`. Usar qualquer outra proporção com o estilo `"manga"` causará um erro. O número máximo de imagens de referência é 9 tanto para `uni-1` quanto para `uni-1-max`.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
| --- | --- | --- |
| `image` | A imagem gerada. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageNode2/pt-BR.md)

---
**Source fingerprint (SHA-256):** `27254fe4627fd340426a68f651cab4513ffb6668cafc0accd17f2c442f7d3125`

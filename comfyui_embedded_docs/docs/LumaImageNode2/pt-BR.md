# Luma UNI-1 Image

## Visão Geral

Este nó gera imagens a partir de descrições textuais usando o modelo Luma UNI-1. Ele recebe um prompt de texto e configurações opcionais, como proporção de aspecto e estilo, e envia a solicitação para a API da Luma para criar uma imagem. Duas variantes do modelo estão disponíveis: `uni-1` e `uni-1-max`.

## Entradas

### Entradas Comuns

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model` | Modelo a ser usado para a geração. Selecionar um modelo revela configurações adicionais para esse modelo. | DYNAMIC_COMBO | Sim | `"uni-1"`<br>`"uni-1-max"` |
| `prompt` | Descrição textual da imagem desejada. De 1 a 6000 caracteres. | STRING | Sim | 1 a 6000 caracteres |
| `seed` | A semente controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente da semente. (padrão: 0) | INT | Sim | 0 a 2147483647 |

### Entradas de uni-1 e uni-1-max

Compartilhadas pelas opções de modelo `uni-1` e `uni-1-max`. Essas configurações aparecem quando qualquer um dos modelos é selecionado.

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `aspect_ratio` | Proporção de aspecto da imagem de saída. `"auto"` permite que o modelo escolha com base no prompt. (padrão: `"auto"`) | COMBO | Sim | `"auto"`<br>`"3:1"`<br>`"2:1"`<br>`"16:9"`<br>`"3:2"`<br>`"1:1"`<br>`"2:3"`<br>`"9:16"`<br>`"1:2"`<br>`"1:3"` |
| `style` | Predefinição de estilo. `"auto"` escolhe com base no prompt; `"manga"` aplica uma estética de mangá/anime e exige uma proporção de aspecto retrato (2:3, 9:16, 1:2, 1:3). (padrão: `"auto"`) | COMBO | Sim | `"auto"`<br>`"manga"` |
| `web_search` | Pesquisar na web por referências visuais antes de gerar. (padrão: False) | BOOLEAN | Sim | True / False |

### Entradas de Referência

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `image_ref` | Slot expansível: conecte de 1 a 9 itens (por exemplo, `image_1` a `image_9`). Até 9 imagens de referência para orientação de estilo/conteúdo. | IMAGE | Não | Até 9 imagens |

**Observação:** Se `style` estiver definido como `"manga"`, o `aspect_ratio` deve ser `"auto"` ou uma das proporções retrato `"2:3"`, `"9:16"`, `"1:2"`, `"1:3"`. Usar qualquer outra proporção com o estilo `"manga"` causará um erro. O número máximo de imagens de referência é 9 para ambos `uni-1` e `uni-1-max`.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `image` | A imagem gerada como um tensor. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageNode2/pt-BR.md)

---
**Source fingerprint (SHA-256):** `27254fe4627fd340426a68f651cab4513ffb6668cafc0accd17f2c442f7d3125`

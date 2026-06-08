Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageNode2/en.md)

## Visão Geral

Este nó gera imagens a partir de descrições textuais usando o modelo Luma UNI-1. Ele recebe um prompt de texto e configurações opcionais, como proporção de aspecto e estilo, e então envia a solicitação para a API Luma para criar uma imagem.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `prompt` | Descrição textual da imagem desejada. | STRING | Sim | 1–6000 caracteres |
| `model` | Modelo a ser usado para a geração. Selecionar um modelo revela configurações adicionais para aquele modelo. | COMBO | Sim | `"uni-1"`<br>`"uni-1-max"` |
| `seed` | A semente controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente da semente. (padrão: 0) | INT | Sim | 0 a 2147483647 |

### Entradas Específicas do Modelo

Quando `"uni-1"` ou `"uni-1-max"` é selecionado para o parâmetro `model`, as seguintes entradas ficam disponíveis:

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `aspect_ratio` | Proporção de aspecto da imagem de saída. `"auto"` permite que o modelo escolha com base no prompt. (padrão: `"auto"`) | COMBO | Sim | `"auto"`<br>`"3:1"`<br>`"2:1"`<br>`"16:9"`<br>`"3:2"`<br>`"1:1"`<br>`"2:3"`<br>`"9:16"`<br>`"1:2"`<br>`"1:3"` |
| `style` | O estilo visual para a imagem gerada. (padrão: `"auto"`) | COMBO | Sim | `"auto"`<br>`"manga"` |
| `web_search` | Se o modelo pode pesquisar na web por contexto adicional. (padrão: Falso) | BOOLEAN | Sim | Verdadeiro / Falso |
| `image_ref` | Imagens de referência para guiar a geração. | IMAGE | Não | Até 9 imagens |

**Nota sobre restrições de `style` e `aspect_ratio`:** Se `style` for definido como `"manga"`, a `aspect_ratio` deve ser `"auto"` ou uma das seguintes proporções de retrato: `"2:3"`, `"9:16"`, `"1:2"`, `"1:3"`. Usar uma proporção paisagem ou quadrada com o estilo `"manga"` causará um erro.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `image` | A imagem gerada como um tensor. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageNode2/pt-BR.md)

---
**Source fingerprint (SHA-256):** `0a71bcd7c68c3610c162601b4c3f700034e47af8f16cf7853606753ad270c96e`

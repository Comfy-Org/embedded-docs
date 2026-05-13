> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageNode2/pt-BR.md)

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageNode2/en.md)

## Visão Geral

Este nó gera imagens a partir de descrições textuais usando o modelo Luma UNI-1. Ele recebe um prompt de texto e configurações opcionais, como proporção de aspecto e estilo, e então envia a solicitação para a API Luma para criar uma imagem.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `prompt` | STRING | Sim | 1–6000 caracteres | Descrição textual da imagem desejada. |
| `model` | COMBO | Sim | `"uni-1"`<br>`"uni-1-max"` | Modelo a ser usado para a geração. Selecionar um modelo revela configurações adicionais para aquele modelo. |
| `seed` | INT | Sim | 0 a 2147483647 | A semente controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente da semente. (padrão: 0) |

### Entradas Específicas do Modelo

Quando `"uni-1"` ou `"uni-1-max"` é selecionado para o parâmetro `model`, as seguintes entradas ficam disponíveis:

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `aspect_ratio` | COMBO | Sim | `"auto"`<br>`"3:1"`<br>`"2:1"`<br>`"16:9"`<br>`"3:2"`<br>`"1:1"`<br>`"2:3"`<br>`"9:16"`<br>`"1:2"`<br>`"1:3"` | Proporção de aspecto da imagem de saída. `"auto"` permite que o modelo escolha com base no prompt. (padrão: `"auto"`) |
| `style` | COMBO | Sim | `"auto"`<br>`"manga"` | O estilo visual para a imagem gerada. (padrão: `"auto"`) |
| `web_search` | BOOLEAN | Sim | Verdadeiro / Falso | Se o modelo pode pesquisar na web por contexto adicional. (padrão: Falso) |
| `image_ref` | IMAGE | Não | Até 9 imagens | Imagens de referência para guiar a geração. |

**Nota sobre restrições de `style` e `aspect_ratio`:** Se `style` for definido como `"manga"`, a `aspect_ratio` deve ser `"auto"` ou uma das seguintes proporções de retrato: `"2:3"`, `"9:16"`, `"1:2"`, `"1:3"`. Usar uma proporção paisagem ou quadrada com o estilo `"manga"` causará um erro.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `image` | IMAGE | A imagem gerada como um tensor. |

---
**Source fingerprint (SHA-256):** `0a71bcd7c68c3610c162601b4c3f700034e47af8f16cf7853606753ad270c96e`

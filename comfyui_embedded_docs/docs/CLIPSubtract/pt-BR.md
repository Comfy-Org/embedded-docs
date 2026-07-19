# CLIPSubtract

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPSubtract/en.md)

O nó CLIPSubtract realiza uma operação de subtração entre dois modelos CLIP. Ele utiliza o primeiro modelo CLIP como base e subtrai os patches-chave do segundo modelo CLIP, com um multiplicador opcional para controlar a intensidade da subtração. Isso permite a combinação refinada de modelos, removendo características específicas de um modelo usando outro.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Tipo de Entrada | Padrão | Faixa |
| --- | --- | --- | --- | --- | --- |
| `clip1` | O modelo CLIP base que será modificado | CLIP | Obrigatório | - | - |
| `clip2` | O modelo CLIP cujos patches-chave serão subtraídos do modelo base | CLIP | Obrigatório | - | - |
| `multiplier` | Controla a intensidade da operação de subtração. Valores positivos subtraem características do clip2, valores negativos adicionam características. | FLOAT | Obrigatório | 1.0 | -10.0 a 10.0, passo 0.01 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `CLIP` | O modelo CLIP resultante após a operação de subtração | CLIP |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPSubtract/pt-BR.md)

---
**Source fingerprint (SHA-256):** `ea7b6f838d6eb083d2d9bc07891b6ef2f3e625861ab1de9279df351e58f2a2a8`

# Opções do T5Tokenizer

O nó T5TokenizerOptions configura as configurações do tokenizador para vários tipos de modelo T5. Ele define os parâmetros de padding mínimo e comprimento mínimo para múltiplas variantes do modelo T5, incluindo t5xxl, pile_t5xl, t5base, mt5xl e umt5xxl. O nó recebe uma entrada CLIP, aplica as configurações a uma cópia dela e retorna o CLIP modificado.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `clip` | O modelo CLIP para configurar as opções do tokenizador | CLIP | Sim | - |
| `preenchimento_mínimo` | Valor mínimo de padding a ser definido para todos os tipos de modelo T5 (padrão: 0) | INT | Sim | 0 a 10000 |
| `comprimento_mínimo` | Valor mínimo de comprimento a ser definido para todos os tipos de modelo T5 (padrão: 0) | INT | Sim | 0 a 10000 |

Nota: Este nó está marcado como experimental no ComfyUI.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `output` | O modelo CLIP modificado com as opções atualizadas do tokenizador aplicadas a todas as variantes T5 | CLIP |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/T5TokenizerOptions/pt-BR.md)

---
**Source fingerprint (SHA-256):** `1c9a67781ddcc423fa3f6ed8ae1cb767a18681366aca9f1a4a6aff6b2eb38667`

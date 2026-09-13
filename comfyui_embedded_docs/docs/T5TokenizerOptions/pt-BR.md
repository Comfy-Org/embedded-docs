# Opções do T5Tokenizer

## Visão geral

O nó T5TokenizerOptions configura as opções do tokenizador para vários tipos de modelos T5. Ele define parâmetros de padding mínimo e comprimento mínimo para diversas variantes do modelo T5, incluindo t5xxl, pile_t5xl, t5base, mt5xl e umt5xxl. O nó recebe uma entrada CLIP, aplica as configurações a uma cópia dela e retorna o CLIP modificado.

## Entradas

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `clip` | O modelo CLIP para o qual configurar as opções do tokenizador | CLIP | Sim | - |
| `min_padding` | Valor mínimo de padding a ser definido para todos os tipos de modelo T5 (padrão: 0) | INT | Sim | 0 a 10000 |
| `min_length` | Valor mínimo de comprimento a ser definido para todos os tipos de modelo T5 (padrão: 0) | INT | Sim | 0 a 10000 |

Observação: este nó está marcado como experimental no ComfyUI. As configurações são aplicadas a todas as variantes T5 suportadas de uma só vez: t5xxl, pile_t5xl, t5base, mt5xl e umt5xxl. A entrada `clip` é clonada antes da modificação, portanto o CLIP original não é alterado.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
| --- | --- | --- |
| `output` | O modelo CLIP modificado com opções do tokenizador atualizadas aplicadas a todas as variantes T5 | CLIP |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/T5TokenizerOptions/pt-BR.md)

---
**Source fingerprint (SHA-256):** `1c9a67781ddcc423fa3f6ed8ae1cb767a18681366aca9f1a4a6aff6b2eb38667`

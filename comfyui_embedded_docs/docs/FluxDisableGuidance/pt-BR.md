> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxDisableGuidance/pt-BR.md)

Este nó desabilita completamente a funcionalidade de incorporação de orientação para Flux e modelos similares. Ele recebe dados de condicionamento como entrada e remove o componente de orientação definindo-o como Nulo, efetivamente desativando o condicionamento baseado em orientação para o processo de geração.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `conditioning` | CONDITIONING | Sim | - | Os dados de condicionamento a serem processados e dos quais a orientação será removida |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `conditioning` | CONDITIONING | Os dados de condicionamento modificados com a orientação desabilitada |

---
**Source fingerprint (SHA-256):** `37e544460d5e50542cebb451997c0320f16d822cc5695cb34825d2038866a455`

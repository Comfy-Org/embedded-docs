> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentApplyOperation/pt-BR.md)

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentApplyOperation/en.md)

O nó LatentApplyOperation aplica uma operação específica a amostras latentes. Ele recebe dados latentes e uma operação como entradas, processa as amostras latentes usando a operação fornecida e retorna os dados latentes modificados. Este nó permite transformar ou manipular representações latentes no seu fluxo de trabalho.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Faixa | Descrição |
|-----------|---------------|-------------|-------|-----------|
| `samples` | LATENT | Sim | - | As amostras latentes a serem processadas pela operação |
| `operation` | LATENT_OPERATION | Sim | - | A operação a ser aplicada às amostras latentes |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|---------------|---------------|-----------|
| `output` | LATENT | As amostras latentes modificadas após aplicar a operação |

---
**Source fingerprint (SHA-256):** `77147b480fe8cb48eb26a31f6f0c7bc038e07d26e628ebe361861394946d8678`

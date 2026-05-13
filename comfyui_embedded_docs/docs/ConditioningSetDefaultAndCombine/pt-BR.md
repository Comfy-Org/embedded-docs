> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetDefaultAndCombine/pt-BR.md)

Este nó combina uma entrada de condicionamento primária com uma entrada de condicionamento padrão usando um sistema baseado em ganchos. Ele mescla as duas fontes de condicionamento em uma única saída, permitindo que o condicionamento padrão sirva como fallback ou base quando o condicionamento primário estiver incompleto.

## Entradas

| Parâmetro | Tipo de Dados | Tipo de Entrada | Padrão | Faixa | Descrição |
|-----------|---------------|-----------------|--------|-------|-----------|
| `cond` | CONDITIONING | Obrigatório | - | - | A entrada de condicionamento primária a ser processada e combinada |
| `cond_DEFAULT` | CONDITIONING | Obrigatório | - | - | Os dados de condicionamento padrão a serem combinados com o condicionamento primário |
| `hooks` | HOOKS | Opcional | - | - | Configuração opcional de ganchos que controla como os dados de condicionamento são processados e combinados |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|---------------|---------------|-----------|
| `CONDITIONING` | CONDITIONING | Os dados de condicionamento combinados resultantes da mesclagem das entradas de condicionamento primária e padrão |

---
**Source fingerprint (SHA-256):** `5e6c95f454c7e262878cc362c6b199e01abff10f803c81afe6e76a317c30d039`

Este nó combina uma entrada de condicionamento primária com uma entrada de condicionamento padrão usando um sistema baseado em ganchos. Ele mescla as duas fontes de condicionamento em uma única saída, permitindo que o condicionamento padrão sirva como fallback ou base quando o condicionamento primário estiver incompleto.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Tipo de Entrada | Padrão | Faixa |
| --- | --- | --- | --- | --- | --- |
| `cond` | A entrada de condicionamento primária a ser processada e combinada | CONDITIONING | Obrigatório | - | - |
| `cond_DEFAULT` | Os dados de condicionamento padrão a serem combinados com o condicionamento primário | CONDITIONING | Obrigatório | - | - |
| `hooks` | Configuração opcional de ganchos que controla como os dados de condicionamento são processados e combinados | HOOKS | Opcional | - | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `CONDITIONING` | Os dados de condicionamento combinados resultantes da mesclagem das entradas de condicionamento primária e padrão | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetDefaultAndCombine/pt-BR.md)

---
**Source fingerprint (SHA-256):** `5e6c95f454c7e262878cc362c6b199e01abff10f803c81afe6e76a317c30d039`

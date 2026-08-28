# Desativar Ruído

O nó DisableNoise fornece uma configuração de ruído vazia que pode ser usada para desabilitar a geração de ruído em processos de amostragem. Ele retorna um objeto de ruído especial que não contém dados de ruído, permitindo que outros nós pulem operações relacionadas a ruído quando conectados a esta saída. O nó também pode ser pesquisado pelo alias "zero noise".

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| *Nenhum parâmetro de entrada* | Este nó não requer nenhum parâmetro de entrada. | - | - | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `NOISE` | Retorna uma configuração de ruído vazia que pode ser usada para desabilitar a geração de ruído em processos de amostragem. | NOISE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DisableNoise/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b9edcda655dab3196233b6c66fdb41eb0585b153616b793016d532992b922934`

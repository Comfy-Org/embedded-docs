# Pré-visualizar como Texto

PreviewAny converte qualquer valor de entrada em texto legível para que você possa inspecioná-lo. Strings passam inalteradas, números e booleanos tornam-se texto simples, e outros tipos de dados são serializados em JSON quando possível (recorrendo à forma de string simples se a serialização falhar). O texto resultante é exibido na interface do usuário e também retornado como uma saída de string para processamento adicional.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `source` | Aceita qualquer tipo de dados de entrada para exibição na pré-visualização. Se nenhum valor for fornecido, a pré-visualização mostra 'None'. | ANY | Sim | Qualquer tipo de dados |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `result` | O valor de entrada convertido para o formato de texto. O mesmo texto também é exibido na interface do usuário. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewAny/pt-BR.md)

---
**Source fingerprint (SHA-256):** `9572eac396aa27a83148a940e4bf37a9ec4e4a47e9526db8bb983611f9237536`

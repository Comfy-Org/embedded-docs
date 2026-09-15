# Pré-visualizar como Texto

PreviewAny converte qualquer valor de entrada em texto legível para que você possa inspecioná-lo. Strings passam sem alterações, números e booleanos se tornam texto simples, e outros tipos de dados são serializados para JSON quando possível (recorrendo à sua forma de string simples se a serialização falhar). O texto resultante é exibido na interface do usuário e também retornado como uma saída de string para processamento posterior.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `source` | Aceita qualquer tipo de dados de entrada para exibição na pré-visualização. Se nenhum valor for fornecido, a pré-visualização mostra 'None'. | ANY | Sim | Qualquer tipo de dados |

**Comportamento de conversão**

- Valores do tipo STRING são exibidos exatamente como fornecidos.
- Valores dos tipos INT, FLOAT ou BOOLEAN são convertidos em texto simples.
- Qualquer outro valor não vazio é convertido em texto JSON com recuo de 4 espaços; se essa conversão falhar, o nó recorre à forma de texto simples do valor. Se isso também falhar, a pré-visualização mostra a mensagem 'source exists, but could not be serialized.'
- Se nenhum valor estiver conectado ou o valor estiver vazio, a pré-visualização mostra 'None'.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `result` | O valor de entrada convertido para o formato de texto. O mesmo texto também é exibido na interface do usuário. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewAny/pt-BR.md)

---
**Source fingerprint (SHA-256):** `66b5283b2d7d43e679c0bc6cdcad54c92539a986763333972e722b39c7963be8`

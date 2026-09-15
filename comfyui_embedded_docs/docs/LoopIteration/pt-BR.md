# LoopIteration

Este nó fornece metadados de iteração para fluxos de trabalho no estilo de loop. Ele recebe entradas baseadas em listas e repassa o primeiro elemento de cada lista, para que um loop possa rastrear o índice atual, se é a primeira ou a última etapa, o item atual da lista e qualquer valor corrente da iteração. O comportamento do cache é controlado pela flag `reuse_cache`.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `iteration_index` | O índice da iteração atual, fornecido como uma lista. O primeiro elemento é repassado para a saída. | INT | Sim | - |
| `is_first` | Indica se a iteração atual é a primeira, fornecida como uma lista. O primeiro elemento é repassado para a saída. | BOOLEAN | Sim | - |
| `is_last` | Indica se a iteração atual é a última, fornecida como uma lista. O primeiro elemento é repassado para a saída. | BOOLEAN | Sim | - |
| `list_item` | O item obtido da lista para esta iteração. Opcional; o primeiro elemento é repassado para a saída quando fornecido; caso contrário, None é retornado. | ANY | Não | - |
| `current_iteration_value` | O valor carregado pela iteração atual. Opcional; o primeiro elemento é repassado para a saída quando fornecido; caso contrário, None é retornado. | ANY | Não | - |
| `reuse_cache` | Controla se o resultado pode ser reutilizado a partir do cache. Quando habilitado, o nó mantém uma impressão digital estável para que resultados em cache possam ser reutilizados. Quando desabilitado, uma impressão digital não correspondente é produzida para que o nó seja executado novamente em cada iteração. | BOOLEAN | Sim | - |

Nota: Este nó é compatível com entrada de lista, o que significa que cada entrada deve chegar como uma lista e o nó produz como saída apenas o primeiro elemento de cada lista. Ele também aceita entradas adicionais além das listadas aqui.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-----------|-----------|
| `iteration_index` | O índice da iteração atual. | INT |
| `is_first` | Se a iteração atual é a primeira. | BOOLEAN |
| `is_last` | Se a iteração atual é a última. | BOOLEAN |
| `list_item` | O item obtido da lista para esta iteração, ou None quando nenhum item foi fornecido. | ANY |
| `current_iteration_value` | O valor carregado pela iteração atual, ou None quando nenhum valor foi fornecido. | ANY |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoopIteration/pt-BR.md)

---
**Source fingerprint (SHA-256):** `1d167860b89de0f7b435a3715f6d543cad7602648abb58575b572c0406631cda`

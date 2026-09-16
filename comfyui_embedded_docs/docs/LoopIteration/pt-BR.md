# LoopIteration

Este nó fornece metadados de iteração para fluxos de trabalho no estilo de loop. Ele recebe entradas baseadas em listas e repassa o primeiro elemento de cada lista, para que um loop possa rastrear o índice atual, se é a primeira ou a última etapa, o item atual da lista e qualquer valor de iteração em execução. O comportamento de cache é controlado pela flag `reuse_cache`. Este nó está marcado como exclusivo para desenvolvedores.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `iteration_index` | O índice da iteração atual, fornecido como uma lista. O primeiro elemento é repassado para a saída. | INT | Sim | - |
| `is_first` | Indica se a iteração atual é a primeira, fornecida como uma lista. O primeiro elemento é repassado para a saída. | BOOLEAN | Sim | - |
| `is_last` | Indica se a iteração atual é a última, fornecida como uma lista. O primeiro elemento é repassado para a saída. | BOOLEAN | Sim | - |
| `list_item` | O item obtido da lista para esta iteração. Opcional; o primeiro elemento é repassado para a saída quando fornecido; caso contrário, None é retornado. | ANY | Não | - |
| `current_iteration_value` | O valor carregado pela iteração atual. Opcional; quando fornecido, o valor completo é repassado para a saída; caso contrário, None é retornado. | ANY | Não | - |
| `reuse_cache` | Controla se o resultado pode ser reutilizado a partir do cache. Quando ativado, o nó mantém uma impressão digital estável para que resultados em cache possam ser reutilizados. Quando desativado, uma impressão digital não correspondente é produzida para que o nó seja executado novamente a cada iteração. | BOOLEAN | Sim | - |

Observação: Este nó tem entrada de lista habilitada, o que significa que cada entrada deve chegar como uma lista e o nó produz apenas o primeiro elemento de cada lista (exceto `current_iteration_value`, que é repassado como uma lista). Ele também aceita entradas adicionais além das listadas aqui.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `iteration_index` | O índice da iteração atual. | INT |
| `is_first` | Se a iteração atual é a primeira. | BOOLEAN |
| `is_last` | Se a iteração atual é a última. | BOOLEAN |
| `list_item` | O item obtido da lista para esta iteração, ou None quando nenhum item foi fornecido. | ANY |
| `current_iteration_value` | O valor carregado pela iteração atual, ou None quando nenhum valor foi fornecido. Esta saída é retornada como uma lista. | ANY |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoopIteration/pt-BR.md)

---
**Source fingerprint (SHA-256):** `c7072f22bd382f567792d2ea7a30312c64d33c213551f8983c25cd7b95adc4fb`

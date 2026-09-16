# StartLoop

O nó Start Loop inicia uma estrutura de repetição dentro de um workflow. Ele executa o corpo do loop conectado uma vez por iteração e pode contar iterações de três formas: um número fixo de repetições (simple), um intervalo de índices numéricos (For) ou uma passagem por item em uma lista (List). Cada passagem expõe o índice atual, os sinalizadores de primeiro/último e um valor carregado opcional que pode ser passado de uma iteração para a próxima.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `mode` | O modo de iteração do loop (padrão: "simple"). O modo selecionado determina quais parâmetros adicionais são exibidos. | DYNAMIC_COMBO | Sim | `"simple"`<br>`"For"`<br>`"List"` |
| `cache_iterations` | Reutiliza resultados de iterações inalteradas de execuções anteriores. Desative para executar cada iteração novamente. Padrão: false. | BOOLEAN | Sim | true<br>false |
| `parent_iteration` | Conecte iteration_index de um Start Loop externo para aninhar este loop. Esta entrada é somente force-input (um link é necessário). | INT | Não | Qualquer inteiro |
| `initial_iteration_value` | Valor exposto como current_iteration_value na primeira iteração. | ANY (tipo correspondente) | Não | Qualquer valor |

### Entradas do modo Simple

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `num_iterations` | Número de vezes para executar o corpo do loop. Padrão: 4. | INT | Sim | Mínimo 0 |

### Entradas do modo For

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `start_iteration_index` | Índice da primeira iteração ao usar o modo de loop For. Padrão: 0. | INT | Sim | Qualquer inteiro |
| `max_iteration` | O valor de parada exclusivo para iteration_index no modo For. Padrão: 4. | INT | Sim | Máximo 0xffffffffffffffff |
| `step` | O tamanho do passo do índice entre cada iteração ao usar o modo de loop For. Padrão: 1. | INT | Sim | Mínimo 1 |

### Entradas do modo List

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `list` | Lista de itens sobre os quais o loop itera. O corpo do loop é executado uma vez por item. | ANY (item de lista com tipo correspondente) | Sim | Qualquer lista |

Notas:

- Apenas os parâmetros pertencentes ao `mode` selecionado no momento são exibidos e usados.
- No modo Simple, os índices de iteração vão de 0 até `num_iterations` menos 1. No modo For, os índices vão de `start_iteration_index` até (mas sem incluir) `max_iteration`, aumentando em `step`. No modo List, uma iteração é executada por item em `list`.
- `step` não pode ser 0; um valor 0 gera um erro. Valores abaixo de 1 não são permitidos.
- Se o número calculado de iterações for zero, a saída `is_last` é reportada como true e o corpo do loop não é executado.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|-------------|-------------|-----------|
| `iteration_index` | Índice da iteração atual do loop. | INT |
| `is_first` | True durante a primeira iteração do loop. | BOOLEAN |
| `is_last` | True durante a última iteração do loop. | BOOLEAN |
| `list_item` | Item atual da lista ao usar o modo List. Nenhum nos modos Simple e For. | ANY (tipo correspondente) |
| `current_iteration_value` | Valor carregado pelo loop para a iteração atual: initial_iteration_value na primeira iteração, depois next_iteration_value do End Loop em cada iteração subsequente. | ANY (tipo correspondente) |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StartLoop/pt-BR.md)

---
**Source fingerprint (SHA-256):** `be34fedd4db9d4f4cc795855c87f6489f294e029da316b5dc66e5af7dff004a9`

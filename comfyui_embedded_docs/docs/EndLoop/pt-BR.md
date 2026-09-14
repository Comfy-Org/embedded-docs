# EndLoop

End Loop marca o fim de um bloco de loop. Ele coleta o valor produzido pelo último nó no corpo do loop e retorna apenas a iteração final ou todas as iterações, dependendo da configuração `accumulate`, além de também passar um valor de volta para Start Loop para que a próxima iteração possa começar.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `output_value` | Valor retornado por End Loop. Retorna a iteração final ou todas as iterações de acordo com accumulate. | ANY | Não | Qualquer tipo de valor |
| `next_iteration_value` | Valor enviado de End Loop de volta para Start Loop para a próxima iteração. | ANY | Não | Qualquer tipo de valor |
| `accumulate` | Retorna output_value de todas as iterações quando habilitado; caso contrário, retorna apenas a iteração final. | BOOLEAN | Não | `true`<br>`false` (padrão: `false`) |
| `terminations` | Conecte saídas que devem ser executadas em todas as iterações. Seus valores não são retornados. Slots expansíveis chamados `termination_1`, `termination_2` e assim por diante. | ANY | Não | 0 a 50 slots |

Observação: `terminations` é uma lista expansível de slots com mínimo de 0 e máximo de 50 conexões. Valores conectados aqui forçam a execução em todas as iterações, mas não fazem parte do resultado retornado.

Observação: Este nó é um nó de lista de entradas, então suas entradas recebem os valores coletados de todas as iterações do loop.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `outputs` | O output_value da iteração final, ou valores acumulados ao longo das iterações quando accumulate está habilitado. | ANY (list) |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EndLoop/pt-BR.md)

---
**Source fingerprint (SHA-256):** `473ba61d8e6fecdd1205297e2c602e3fd821044aff87d15a3f4b7646748d9999`

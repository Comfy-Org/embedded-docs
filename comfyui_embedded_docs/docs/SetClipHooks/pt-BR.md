> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetClipHooks/pt-BR.md)

O nó SetClipHooks permite que você aplique *hooks* personalizados a um modelo CLIP, possibilitando modificações avançadas em seu comportamento. Ele pode aplicar *hooks* às saídas de condicionamento e, opcionalmente, habilitar a funcionalidade de agendamento de CLIP (*clip scheduling*). Este nó cria uma cópia clonada do modelo CLIP de entrada com as configurações de *hook* especificadas aplicadas.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `clip` | CLIP | Sim | - | O modelo CLIP ao qual os *hooks* serão aplicados |
| `apply_to_conds` | BOOLEAN | Sim | - | Define se os *hooks* devem ser aplicados às saídas de condicionamento (padrão: Verdadeiro) |
| `schedule_clip` | BOOLEAN | Sim | - | Define se o agendamento de CLIP (*clip scheduling*) deve ser habilitado (padrão: Falso) |
| `hooks` | HOOKS | Não | - | Grupo de *hooks* opcional a ser aplicado ao modelo CLIP |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `clip` | CLIP | Um modelo CLIP clonado com os *hooks* especificados aplicados |

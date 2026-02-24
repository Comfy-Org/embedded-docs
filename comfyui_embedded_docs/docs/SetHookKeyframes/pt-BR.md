> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetHookKeyframes/pt-BR.md)

O nó Set Hook Keyframes permite que você aplique agendamento por quadros-chave a grupos de hooks existentes. Ele recebe um grupo de hooks e, opcionalmente, aplica informações de temporização de quadros-chave para controlar quando diferentes hooks são executados durante o processo de geração. Quando os quadros-chave são fornecidos, o nó clona o grupo de hooks e define a temporização dos quadros-chave em todos os hooks dentro do grupo.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `hooks` | HOOKS | Sim | - | O grupo de hooks ao qual o agendamento por quadros-chave será aplicado |
| `hook_kf` | HOOK_KEYFRAMES | Não | - | Grupo opcional de quadros-chave contendo informações de temporização para a execução dos hooks |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `hooks` | HOOKS | O grupo de hooks modificado com o agendamento por quadros-chave aplicado (clonado se os quadros-chave foram fornecidos) |

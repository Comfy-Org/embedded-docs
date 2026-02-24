> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookKeyframe/pt-BR.md)

O nó Create Hook Keyframe permite que você defina pontos específicos em um processo de geração onde o comportamento dos *hooks* muda. Ele cria *keyframes* que modificam a força dos *hooks* em porcentagens específicas do progresso da geração, e esses *keyframes* podem ser encadeados para criar padrões de agendamento complexos.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `strength_mult` | FLOAT | Sim | -20.0 a 20.0 | Multiplicador para a força do *hook* neste *keyframe* (padrão: 1.0) |
| `start_percent` | FLOAT | Sim | 0.0 a 1.0 | O ponto percentual no processo de geração onde este *keyframe* entra em vigor (padrão: 0.0) |
| `prev_hook_kf` | HOOK_KEYFRAMES | Não | - | Grupo opcional de *keyframes* de *hook* anterior ao qual adicionar este *keyframe* |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `HOOK_KF` | HOOK_KEYFRAMES | Um grupo de *keyframes* de *hook* incluindo o *keyframe* recém-criado |

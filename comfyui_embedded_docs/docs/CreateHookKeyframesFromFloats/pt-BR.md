> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookKeyframesFromFloats/pt-BR.md)

Este nó cria keyframes de gancho a partir de uma lista de valores de força de ponto flutuante, distribuindo-os uniformemente entre porcentagens de início e fim especificadas. Ele gera uma sequência de keyframes onde cada valor de força é atribuído a uma posição percentual específica na linha do tempo da animação. O nó pode criar um novo grupo de keyframes ou adicionar a um existente, com uma opção para imprimir os keyframes gerados para fins de depuração.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `floats_strength` | FLOATS | Sim | -1 a ∞ | Um único valor float ou uma lista de valores float representando os valores de força para os keyframes (padrão: -1) |
| `start_percent` | FLOAT | Sim | 0.0 a 1.0 | A posição percentual inicial para o primeiro keyframe na linha do tempo (padrão: 0.0) |
| `end_percent` | FLOAT | Sim | 0.0 a 1.0 | A posição percentual final para o último keyframe na linha do tempo (padrão: 1.0) |
| `print_keyframes` | BOOLEAN | Sim | True/False | Quando habilitado, imprime as informações dos keyframes gerados no console (padrão: False) |
| `prev_hook_kf` | HOOK_KEYFRAMES | Não | - | Um grupo de keyframes de gancho existente para adicionar os novos keyframes, ou cria um novo grupo se não fornecido |

**Observação:** O parâmetro `floats_strength` aceita um único valor float ou uma lista iterável de floats. Os keyframes são distribuídos linearmente entre `start_percent` e `end_percent` com base no número de valores de força fornecidos.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `HOOK_KF` | HOOK_KEYFRAMES | Um grupo de keyframes de gancho contendo os keyframes recém-criados, seja como um novo grupo ou anexado ao grupo de keyframes de entrada |

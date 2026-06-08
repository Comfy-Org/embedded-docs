Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetHookKeyframes/en.md)

O nó Set Hook Keyframes permite aplicar agendamento de quadros-chave a grupos de hooks existentes. Ele recebe um grupo de hooks e, opcionalmente, aplica informações de temporização de quadros-chave para controlar quando diferentes hooks são executados durante o processo de geração. Quando quadros-chave são fornecidos, o nó clona o grupo de hooks e define a temporização dos quadros-chave em todos os hooks dentro do grupo.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `hooks` | O grupo de hooks ao qual o agendamento de quadros-chave será aplicado | HOOKS | Sim | - |
| `hook_kf` | Grupo opcional de quadros-chave contendo informações de temporização para execução dos hooks | HOOK_KEYFRAMES | Não | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `hooks` | O grupo de hooks modificado com o agendamento de quadros-chave aplicado (clonado se quadros-chave foram fornecidos) | HOOKS |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetHookKeyframes/pt-BR.md)

---
**Source fingerprint (SHA-256):** `48908e5247b18e5b7b1d894c2f1adcf6403e499125b0c3eb05978584b3d5759b`

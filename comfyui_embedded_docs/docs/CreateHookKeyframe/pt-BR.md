> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookKeyframe/pt-BR.md)

Esta documentação foi gerada por IA. Caso encontre erros ou tenha sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookKeyframe/en.md)

O nó Criar Keyframe de Hook permite definir pontos específicos em um processo de geração onde o comportamento do hook é alterado. Ele cria keyframes que modificam a intensidade dos hooks em porcentagens específicas do progresso da geração, e esses keyframes podem ser encadeados para criar padrões de agendamento complexos.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `multiplicador_de_força` | FLOAT | Sim | -20.0 a 20.0 | Multiplicador da intensidade do hook neste keyframe (padrão: 1.0) |
| `percentual_inicial` | FLOAT | Sim | 0.0 a 1.0 | O ponto percentual no processo de geração onde este keyframe entra em vigor (padrão: 0.0) |
| `quadro-chave_gancho_anterior` | HOOK_KEYFRAMES | Não | - | Grupo opcional de keyframes de hook anterior para adicionar este keyframe |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `HOOK_KF` | HOOK_KEYFRAMES | Um grupo de keyframes de hook incluindo o keyframe recém-criado |

---
**Source fingerprint (SHA-256):** `51893311a0623cafcf8c2d8af00e4005ca2fea2df9474e87d7d4b332b38435c3`

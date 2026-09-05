# TripoRigCheckNode

Este nó envia o ID de uma tarefa concluída de modelo 3D Tripo para a API do Tripo e verifica se esse modelo pode ser rigado. Ele aguarda a conclusão da verificação e retorna um resultado sim/não, além do tipo de esqueleto que o Tripo recomenda para o modelo.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
|-----------|-------------|--------------|-------------|-----------|
| `model_task_id` | O ID da tarefa Tripo do modelo a ser analisado. Ele identifica um modelo que foi previamente gerado, importado ou criado de outra forma por meio de uma tarefa Tripo. | STRING | Sim | N/A |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|---------------|-------------|--------------|
| `riggable` | Indica se o modelo pode ser rigado. | BOOLEAN |
| `rig_type` | Esqueleto recomendado: biped, quadruped, hexapod, octopod, avian, serpentine ou aquatic; 'others' quando o modelo não pode ser rigado. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRigCheckNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `3aa0bc194e887804b92ca1f9f2b12997c73e111fb282c5de96e55f664c21545e`

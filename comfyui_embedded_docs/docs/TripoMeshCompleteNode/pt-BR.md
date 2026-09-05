# TripoMeshCompleteNode

Completa partes ausentes ou incompletas de um modelo 3D já segmentado e repara regiões danificadas da malha. Ele recebe o ID da tarefa de um resultado de segmentação de malha da Tripo e solicita que a Tripo complete o modelo, aguardando a conclusão do trabalho. As partes concluídas são retornadas como um arquivo GLB, e você pode opcionalmente limitar o trabalho a nomes de partes específicos.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `segment_task_id` | ID da tarefa de uma segmentação de malha da Tripo. As partes do modelo segmentado desta tarefa são concluídas. Conecte a saída SEGMENT_TASK_ID de um nó anterior de segmentação de malha da Tripo. | SEGMENT_TASK_ID | Sim | ID de tarefa única |
| `part_names` | Nomes de partes separados por vírgula para concluir. Vazio conclui todas as partes. Padrão: string vazia. Espaços extras ao redor dos nomes são removidos e nomes duplicados são ignorados. | STRING | Não | Texto livre ou vazio |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `model_file` | Nome do arquivo do modelo concluído. Esta saída existe apenas para compatibilidade com versões anteriores. | STRING |
| `task_id do modelo` | ID da tarefa da conclusão de malha da Tripo concluída. Pode ser usado como entrada por outros nós da Tripo que esperam um ID de tarefa de modelo. | MODEL_TASK_ID |
| `GLB` | O modelo 3D concluído com partes reparadas, baixado como um arquivo GLB. | GLB |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoMeshCompleteNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `aa7173f25f54d9fca9605e246a93fe319cf46c07d8d3aacc214a24a60c92e611`

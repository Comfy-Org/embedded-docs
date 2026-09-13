# Tripo: Segmentar modelo

Este nó divide um modelo 3D em partes individuais. Ele envia o modelo para o serviço de segmentação Tripo, aguarda a conclusão da tarefa e retorna o modelo segmentado no formato GLB, juntamente com uma lista de nomes de partes separados por vírgula. Esses nomes de partes alimentam etapas posteriores, como Tripo: Complete Mesh Parts, Tripo: Retopology e Tripo: Convert model.

## Entradas

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model_task_id` | O ID da tarefa do modelo 3D a ser segmentado em partes. | MODEL_TASK_ID | Sim | N/A |

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|-------------|-------------|-----------|
| `model_file` | Nome do arquivo de saída do modelo GLB segmentado, no formato `<task_id>.glb`. Mantido apenas para compatibilidade com versões anteriores. | STRING |
| `segment task_id` | O ID da tarefa do trabalho de segmentação que produziu o resultado. | SEGMENT_TASK_ID |
| `GLB` | O modelo 3D segmentado, como um arquivo GLB. | GLB |
| `part_names` | Nomes das partes separados por vírgula. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSegmentNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `3218f87bfdc347d58b639cbe57b01cf7625c95c753bf381e35b4a28376eeb0e8`

# TripoSegmentNode

Este nó divide um modelo 3D em partes individuais. Ele envia o modelo para o serviço de segmentação Tripo, aguarda a conclusão do processo e retorna o modelo segmentado no formato GLB com uma lista separada por vírgulas dos nomes das partes. Esses nomes de partes alimentam etapas posteriores, como Tripo: Complete Mesh Parts, Tripo: Retopology e Tripo: Convert model.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model_task_id` | O ID da tarefa do modelo 3D a ser segmentado em partes. | MODEL_TASK_ID | Sim | N/A |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `model_file` | Nome do arquivo de saída do modelo GLB segmentado. Mantido apenas para compatibilidade com versões anteriores. | STRING |
| `segment task_id` | O ID da tarefa do processo de segmentação que gerou o resultado. | SEGMENT_TASK_ID |
| `GLB` | O modelo 3D segmentado, como um arquivo GLB. | GLB |
| `part_names` | Nomes das partes separados por vírgula. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSegmentNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `d27580a7f2118e76cecff5e1d682c7605f966bf657d7a02b2d2ddf764d9b72d0`

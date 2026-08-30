# Meshy: Animar Modelo

Este nó aplica uma ação de animação específica a um personagem 3D previamente rigado usando o serviço Meshy. Ele recebe um ID de tarefa de uma operação de rigging anterior e um ID de ação para selecionar a animação desejada na biblioteca e retorna o modelo animado nos formatos de arquivo GLB e FBX.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `rig_task_id` | O ID de tarefa único de uma operação de rigging de personagem Meshy concluída anteriormente. | STRING | Sim | N/A |
| `action_id` | O número de ID da ação de animação a ser aplicada. Visite https://docs.meshy.ai/en/api/animation-library para obter uma lista de valores disponíveis. (padrão: 0) | INT | Sim | 0 a 696 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `arquivo_do_modelo` | Um identificador de string para o modelo animado. Esta saída é fornecida apenas para compatibilidade retroativa. | STRING |
| `GLB` | O arquivo do modelo 3D animado no formato GLB. | FILE3DGLB |
| `FBX` | O arquivo do modelo 3D animado no formato FBX. | FILE3DFBX |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyAnimateModelNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `760e94d3a92910051d9b473545191842dc9672e6c4a59c3d1cd9cfdc5eb2589d`

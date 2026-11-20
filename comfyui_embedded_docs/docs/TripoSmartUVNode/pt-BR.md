# Tripo: Smart UV

Tripo: Smart UV refaz o unwrap das UVs de um modelo e remapeia suas texturas, rig e animação para o novo layout. Use quando o layout original de UVs de um modelo for inutilizável, por exemplo, após retopologia ou quando as costuras de textura precisarem ser refeitas. O modelo de entrada não deve exceder 80.000 triângulos (um quad conta como dois), então reduza modelos maiores com Tripo: Retopology ou um `face_limit` primeiro.

> **Nota:** O Tripo mantém registros de tarefas em seus servidores por 7 dias (em vigor a partir de 1º de dezembro de 2026). Um ID de tarefa mais antigo que isso não pode mais ser resolvido, então reexecutar um fluxo de trabalho salvo após essa janela falha neste nó. Execute novamente o nó Tripo anterior para criar um novo ID de tarefa, ou reimporte o modelo baixado com **Tripo: Import Model**.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model_task_id` | ID da tarefa do modelo a ser submetido novamente ao unwrap. Aceita um ID de tarefa de modelo de um nó de geração do Tripo, ou um ID de tarefa de rig, retarget ou segmentação. | MODEL_TASK_ID | Sim | ID de tarefa do Tripo |
| `bake` | Faça o bake das texturas existentes no novo layout de UVs. Desativado, pula o bake e retorna o modelo sem suas texturas de cor (padrão: True). | BOOLEAN | Sim | `True`<br>`False` |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `model task_id` | ID da tarefa de UV concluída. Pode ser passado para outros nós Tripo, por exemplo, Tripo: Texture. | MODEL_TASK_ID |
| `GLB` | O modelo com unwrap refeito em formato GLB. Vazio quando o modelo de origem é FBX. | FILE_3D_GLB |
| `FBX` | O modelo com unwrap refeito em formato FBX. Preenchido apenas quando o modelo de origem é FBX, por exemplo, uma malha de quads. | FILE_3D_FBX |
| `UV atlas` | O layout de UVs renderizado do modelo como uma imagem. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSmartUVNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `55c9352c7c8129fa7a4f99f803bdc6db112830454e7d9566fa734063cb283532`

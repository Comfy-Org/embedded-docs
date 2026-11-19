# Tripo: Smart UV

Tripo: Smart UV refaz o desembrulho UV de um modelo e remapeia suas texturas, rig e animação para o novo layout. Use-o quando o layout UV original de um modelo é inutilizável, por exemplo, após retopologia ou quando as costuras de textura precisam ser refeitas. O modelo de entrada não deve exceder 80.000 triângulos (um quad conta como dois), então reduza modelos maiores com Tripo: Retopology ou um `face_limit` primeiro.

> **Nota:** O Tripo mantém registros de tarefas em seus servidores por 7 dias (a partir de 1º de dezembro de 2026). Um ID de tarefa mais antigo que isso não pode mais ser resolvido, então executar novamente um fluxo de trabalho salvo após esse período falha neste nó. Execute o nó Tripo anterior novamente para criar um novo ID de tarefa, ou reimporte o modelo baixado com **Tripo: Import Model**.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model_task_id` | ID da tarefa do modelo para refazer o desembrulho UV. Aceita um ID de tarefa de modelo de um nó de geração Tripo, ou um ID de tarefa de rig, retarget ou segmento. | MODEL_TASK_ID | Sim | ID da tarefa Tripo |
| `bake` | Assar as texturas existentes no novo layout UV. Desativado pula a assagem e retorna o modelo sem suas texturas de cor (padrão: True). | BOOLEAN | Sim | `True`<br>`False` |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `model task_id` | ID da tarefa da tarefa UV concluída. Pode ser passado para outros nós Tripo, por exemplo, Tripo: Texture. | MODEL_TASK_ID |
| `GLB` | O modelo com desembrulho UV refeito no formato GLB. Vazio quando o modelo de origem é FBX. | GLB FILE |
| `FBX` | O modelo com desembrulho UV refeito no formato FBX. Preenchido apenas quando o modelo de origem é FBX, por exemplo, uma malha de quads. | FBX FILE |
| `UV atlas` | O layout UV renderizado do modelo como uma imagem. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSmartUVNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `55c9352c7c8129fa7a4f99f803bdc6db112830454e7d9566fa734063cb283532`

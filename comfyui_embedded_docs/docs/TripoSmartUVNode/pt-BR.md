# Tripo: Smart UV

Tripo: Smart UV refaz o unwrap das UVs de um modelo e remapeia suas texturas, rig e animação para o novo layout. Use-o quando o layout de UV original de um modelo não for utilizável, por exemplo após retopologia ou quando as costuras de textura precisarem ser refeitas. O modelo de entrada não deve exceder 80.000 triângulos (um quad conta como dois), então reduza modelos maiores com Tripo: Retopology ou um `face_limit` primeiro.

> **Nota:** O Tripo mantém os registros de tarefas em seus servidores por 7 dias (em vigor a partir de 1º de dezembro de 2026). Um ID de tarefa mais antigo que isso não pode mais ser resolvido, então executar novamente um workflow salvo após esse período falha neste nó. Execute novamente os nós Tripo a montante que produziram a tarefa ou reimporte um modelo baixado com **Tripo: Import Model**. Baixe o modelo antes que o período termine: um ativo expirado não pode ser recuperado do registro da tarefa.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model_task_id` | ID da tarefa do modelo para refazer o unwrap. Aceita um ID de tarefa de modelo de um nó de geração do Tripo, ou um ID de tarefa de rig, retarget ou segment. | MODEL_TASK_ID | Sim | ID de tarefa do Tripo |
| `bake` | Grava (bake) as texturas existentes no novo layout de UV. Desativado, ignora o bake e retorna o modelo sem suas texturas de cor (padrão: True). | BOOLEAN | Sim | `True`<br>`False` |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `model task_id` | ID da tarefa de UV concluída. Pode ser passado para outros nós do Tripo, por exemplo Tripo: Texture. | MODEL_TASK_ID |
| `GLB` | O modelo com o unwrap refeito no formato GLB. Vazio quando o modelo de origem é FBX. | FILE_3D_GLB |
| `FBX` | O modelo com o unwrap refeito no formato FBX. Preenchido apenas quando o modelo de origem é FBX, por exemplo uma malha de quads. | FILE_3D_FBX |
| `UV atlas` | O layout de UV renderizado do modelo como uma imagem. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSmartUVNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `55c9352c7c8129fa7a4f99f803bdc6db112830454e7d9566fa734063cb283532`

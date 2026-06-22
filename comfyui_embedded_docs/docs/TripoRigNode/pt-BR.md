# Tripo: Rig no modelo

O nó TripoRigNode gera um modelo 3D rigado a partir do ID de tarefa de um modelo original. Ele envia uma solicitação para a API Tripo criar uma rig de animação no formato GLB usando a especificação Tripo e, em seguida, consulta a API até que a tarefa de geração da rig seja concluída.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `id_da_tarefa_do_modelo_original` | O ID da tarefa do modelo 3D original a ser rigado | MODEL_TASK_ID | Sim | - |
| `auth_token` | Token de autenticação para acesso à API Comfy.org | AUTH_TOKEN_COMFY_ORG | Não | - |
| `comfy_api_key` | Chave de API para autenticação no serviço Comfy.org | API_KEY_COMFY_ORG | Não | - |
| `unique_id` | Identificador único para rastreamento da operação | UNIQUE_ID | Não | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `model_file` | O arquivo do modelo 3D rigado gerado (mantido para compatibilidade reversa) | STRING |
| `rig task_id` | O ID da tarefa para rastrear o processo de geração da rig | RIG_TASK_ID |
| `GLB` | O modelo 3D rigado gerado no formato GLB | FILE3DGLB |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRigNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `621a4d08f3b8a349c3afff3dbf888b20d524eb3337685769b7a7badcb28986e4`

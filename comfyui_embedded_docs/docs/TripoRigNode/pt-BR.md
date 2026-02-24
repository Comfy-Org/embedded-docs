> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRigNode/pt-BR.md)

O TripoRigNode gera um modelo 3D com rig a partir de um ID de tarefa de modelo original. Ele envia uma solicitação para a API do Tripo para criar um rig animado no formato GLB usando a especificação Tripo e, em seguida, consulta a API repetidamente até que a tarefa de geração do rig seja concluída.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `original_model_task_id` | MODEL_TASK_ID | Sim | - | O ID da tarefa do modelo 3D original a ser rigado |
| `auth_token` | AUTH_TOKEN_COMFY_ORG | Não | - | Token de autenticação para acesso à API do Comfy.org |
| `comfy_api_key` | API_KEY_COMFY_ORG | Não | - | Chave de API para autenticação no serviço Comfy.org |
| `unique_id` | UNIQUE_ID | Não | - | Identificador único para rastrear a operação |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `model_file` | STRING | O arquivo do modelo 3D rigado gerado |
| `rig task_id` | RIG_TASK_ID | O ID da tarefa para rastrear o processo de geração do rig |

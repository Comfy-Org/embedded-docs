> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRigNode/pt-BR.md)

O nó TripoRigNode gera um modelo 3D rigado a partir do ID de tarefa de um modelo original. Ele envia uma solicitação para a API Tripo criar uma rig de animação no formato GLB usando a especificação Tripo e, em seguida, consulta a API até que a tarefa de geração da rig seja concluída.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|---------------|-------------|-----------|-----------|
| `id_da_tarefa_do_modelo_original` | MODEL_TASK_ID | Sim | - | O ID da tarefa do modelo 3D original a ser rigado |
| `auth_token` | AUTH_TOKEN_COMFY_ORG | Não | - | Token de autenticação para acesso à API Comfy.org |
| `comfy_api_key` | API_KEY_COMFY_ORG | Não | - | Chave de API para autenticação no serviço Comfy.org |
| `unique_id` | UNIQUE_ID | Não | - | Identificador único para rastreamento da operação |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|---------------|---------------|-----------|
| `model_file` | STRING | O arquivo do modelo 3D rigado gerado (mantido para compatibilidade reversa) |
| `rig task_id` | RIG_TASK_ID | O ID da tarefa para rastrear o processo de geração da rig |
| `GLB` | FILE3DGLB | O modelo 3D rigado gerado no formato GLB |

---
**Source fingerprint (SHA-256):** `621a4d08f3b8a349c3afff3dbf888b20d524eb3337685769b7a7badcb28986e4`

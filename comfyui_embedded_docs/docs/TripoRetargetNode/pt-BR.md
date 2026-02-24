> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRetargetNode/pt-BR.md)

O TripoRetargetNode aplica animações predefinidas a modelos de personagens 3D através do redirecionamento de dados de movimento. Ele recebe um modelo 3D previamente processado e aplica uma das várias animações predefinidas, gerando um arquivo de modelo 3D animado como saída. O nó se comunica com a API Tripo para processar a operação de redirecionamento de animação.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `original_model_task_id` | RIG_TASK_ID | Sim | - | O ID da tarefa do modelo 3D previamente processado ao qual a animação será aplicada |
| `animation` | STRING | Sim | "preset:idle"<br>"preset:walk"<br>"preset:climb"<br>"preset:jump"<br>"preset:slash"<br>"preset:shoot"<br>"preset:hurt"<br>"preset:fall"<br>"preset:turn" | A predefinição de animação a ser aplicada ao modelo 3D |
| `auth_token` | AUTH_TOKEN_COMFY_ORG | Não | - | Token de autenticação para acesso à API do Comfy.org |
| `comfy_api_key` | API_KEY_COMFY_ORG | Não | - | Chave de API para acesso ao serviço Comfy.org |
| `unique_id` | UNIQUE_ID | Não | - | Identificador único para rastrear a operação |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `model_file` | STRING | O arquivo do modelo 3D animado gerado |
| `retarget task_id` | RETARGET_TASK_ID | O ID da tarefa para rastrear a operação de redirecionamento |

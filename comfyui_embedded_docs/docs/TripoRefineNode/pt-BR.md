> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRefineNode/pt-BR.md)

O TripoRefineNode refina modelos 3D preliminares criados especificamente pelos modelos Tripo v1.4. Ele recebe um ID de tarefa de modelo e o processa através da API Tripo para gerar uma versão aprimorada do modelo. Este nó foi projetado para funcionar exclusivamente com modelos preliminares produzidos pelos modelos Tripo v1.4.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model_task_id` | MODEL_TASK_ID | Sim | - | Deve ser um modelo Tripo v1.4 |
| `auth_token` | AUTH_TOKEN_COMFY_ORG | Não | - | Token de autenticação para a API do Comfy.org |
| `comfy_api_key` | API_KEY_COMFY_ORG | Não | - | Chave de API para os serviços do Comfy.org |
| `unique_id` | UNIQUE_ID | Não | - | Identificador único para a operação |

**Observação:** Este nó aceita apenas modelos preliminares criados pelos modelos Tripo v1.4. O uso de modelos de outras versões pode resultar em erros.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `model_file` | STRING | O caminho do arquivo ou referência para o modelo refinado |
| `model task_id` | MODEL_TASK_ID | O identificador da tarefa para a operação de refinamento do modelo |

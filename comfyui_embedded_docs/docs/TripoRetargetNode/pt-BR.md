> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRetargetNode/pt-BR.md)

O nó TripoRetargetNode aplica animações predefinidas a modelos de personagens 3D por meio da reorientação de dados de movimento. Ele recebe um modelo 3D previamente rigado e aplica uma de várias animações predefinidas, gerando um arquivo de modelo 3D animado como saída. O nó se comunica com a API Tripo para processar a operação de reorientação de animação.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|--------------|-------------|-----------|-----------|
| `id_da_tarefa_do_modelo_original` | RIG_TASK_ID | Sim | - | O ID da tarefa do modelo 3D rigado processado anteriormente ao qual aplicar a animação |
| `animação` | STRING | Sim | "preset:idle"<br>"preset:walk"<br>"preset:run"<br>"preset:dive"<br>"preset:climb"<br>"preset:jump"<br>"preset:slash"<br>"preset:shoot"<br>"preset:hurt"<br>"preset:fall"<br>"preset:turn"<br>"preset:quadruped:walk"<br>"preset:hexapod:walk"<br>"preset:octopod:walk"<br>"preset:serpentine:march"<br>"preset:aquatic:march" | A predefinição de animação a ser aplicada ao modelo 3D. As opções incluem animações humanoides (parado, andar, correr, mergulhar, escalar, pular, golpear, atirar, ferido, cair, girar) e animações de criaturas (andar quadrúpede, andar hexápode, andar octópode, marcha serpentina, marcha aquática). |
| `auth_token_comfy_org` | AUTH_TOKEN_COMFY_ORG | Não | - | Token de autenticação para acesso à API Comfy.org (parâmetro oculto) |
| `api_key_comfy_org` | API_KEY_COMFY_ORG | Não | - | Chave de API para acesso ao serviço Comfy.org (parâmetro oculto) |
| `unique_id` | UNIQUE_ID | Não | - | Identificador único para rastreamento da operação (parâmetro oculto) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `model_file` | STRING | O arquivo de modelo 3D animado gerado (apenas para compatibilidade com versões anteriores) |
| `retarget task_id` | RETARGET_TASK_ID | O ID da tarefa para rastreamento da operação de reorientação |
| `GLB` | FILE3DGLB | O modelo 3D animado no formato GLB |

---
**Source fingerprint (SHA-256):** `304326afdc1fa3e8c3593f151f771f93520e061802c831838c58ebc401b9e9e2`

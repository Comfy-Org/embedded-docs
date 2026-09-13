# Tripo: Retarget para modelo com rig

O TripoRetargetNode aplica uma animação predefinida a um modelo 3D com rig existente. Ele recebe o ID da tarefa de um modelo que foi previamente riggado, envia uma solicitação de retarget para a API da Tripo e baixa o arquivo animado resultante. O modelo animado pode ser retornado como GLB ou FBX, com geometria de malha opcional e reprodução no local opcional.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `id_da_tarefa_do_modelo_original` | O ID da tarefa do modelo 3D previamente riggado a sofrer retarget. A tarefa referenciada deve ser uma tarefa de rig. | RIG_TASK_ID | Sim | - |
| `animação` | A predefinição de animação a ser aplicada ao modelo com rig. Animações `preset:*` funcionam com ambos os modelos de rig. Animações `preset:biped:*` são feitas para rigs do modelo v1.0-20240301; um rig v2.5 aceita apenas chop, climb, dive, fall, hurt, idle, jump, run, shoot, slash, turn e walk. | COMBO | Sim | `"preset:idle"`<br>`"preset:walk"`<br>`"preset:run"`<br>`"preset:dive"`<br>`"preset:climb"`<br>`"preset:jump"`<br>`"preset:slash"`<br>`"preset:shoot"`<br>`"preset:hurt"`<br>`"preset:fall"`<br>`"preset:turn"`<br>`"preset:quadruped:walk"`<br>`"preset:hexapod:walk"`<br>`"preset:octopod:walk"`<br>`"preset:serpentine:march"`<br>`"preset:aquatic:march"`<br>além de opções adicionais `"preset:biped:*"` mostradas na UI |
| `out_format` | Formato do arquivo de saída; o resultado chega na saída correspondente. (padrão: glb) | COMBO | Não | `"glb"`<br>`"fbx"` |
| `export_with_geometry` | Inclui a malha na exportação; quando desativado, exporta apenas o esqueleto animado. (padrão: True) | BOOLEAN | Não | True<br>False |
| `animate_in_place` | Reproduz a animação no local, sem deslocamento da raiz. (padrão: False) | BOOLEAN | Não | True<br>False |
| `auth_token_comfy_org` | Token de autenticação para acesso à API do Comfy.org (parâmetro oculto). | AUTH_TOKEN_COMFY_ORG | Não | - |
| `api_key_comfy_org` | Chave de API para acesso ao serviço Comfy.org (parâmetro oculto). | API_KEY_COMFY_ORG | Não | - |
| `unique_id` | Identificador único para rastrear a operação (parâmetro oculto). | UNIQUE_ID | Não | - |

Nota: Animações no grupo `preset:*` funcionam com ambos os modelos de rig. Animações no grupo `preset:biped:*` são feitas para rigs do modelo v1.0-20240301; um rig v2.5 aceita apenas chop, climb, dive, fall, hurt, idle, jump, run, shoot, slash, turn e walk. Se o rig referenciado foi criado com a especificação Mixamo e uma versão de modelo que começa com `v1.0`, a chamada de retarget falha com um erro. O formato de saída solicitado deve ser GLB ou FBX; se o serviço retornar qualquer outro tipo de arquivo, o nó gera um erro.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `model_file` | O arquivo de modelo 3D animado gerado (apenas para compatibilidade com versões anteriores). | STRING |
| `retarget task_id` | O ID da tarefa para rastrear a operação de retargeting. | RETARGET_TASK_ID |
| `GLB` | O modelo 3D animado no formato GLB. Preenchido quando `out_format` é glb. | FILE3DGLB |
| `FBX` | O modelo 3D animado no formato FBX. Preenchido quando `out_format` é fbx. | FILE3DFBX |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRetargetNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `4814858b940ece13f85010ff81fcdac0258fe8550aebd914be2613e8f40c0e5a`

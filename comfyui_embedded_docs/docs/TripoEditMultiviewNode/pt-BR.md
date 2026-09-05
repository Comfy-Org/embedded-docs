# TripoEditMultiviewNode

Tripo: Edit Multiview edita as quatro vistas de um resultado do Tripo: Image to Multiview, usando uma instrução de texto separada para cada vista. Vistas sem instrução permanecem inalteradas. As imagens editadas devem ser conectadas ao Tripo: Multiview to Model para criar um modelo 3D.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `multiview_task_id` | ID da tarefa do resultado do Tripo: Image to Multiview cujas vistas serão editadas. | MULTIVIEW_TASK_ID | Sim | ID da tarefa |
| `front_prompt` | Instrução de texto descrevendo a edição a ser aplicada à vista frontal. Quando vazia, a vista frontal permanece inalterada. Padrão: vazio. | STRING | Não | Texto multilinha |
| `left_prompt` | Instrução de texto descrevendo a edição a ser aplicada à vista esquerda. Quando vazia, a vista esquerda permanece inalterada. Padrão: vazio. | STRING | Não | Texto multilinha |
| `back_prompt` | Instrução de texto descrevendo a edição a ser aplicada à vista traseira. Quando vazia, a vista traseira permanece inalterada. Padrão: vazio. | STRING | Não | Texto multilinha |
| `right_prompt` | Instrução de texto descrevendo a edição a ser aplicada à vista direita. Quando vazia, a vista direita permanece inalterada. Padrão: vazio. | STRING | Não | Texto multilinha |

Observação: Pelo menos um dos quatro prompts (`front_prompt`, `left_prompt`, `back_prompt`, `right_prompt`) deve conter texto não vazio; caso contrário, o nó gera um erro. O `multiview_task_id` deve vir do nó Tripo: Image to Multiview. Um conjunto multiview editado não pode ser editado novamente.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `frente` | Imagem da vista frontal editada. | IMAGE |
| `esquerda` | Imagem da vista esquerda editada. | IMAGE |
| `traseira` | Imagem da vista traseira editada. | IMAGE |
| `direita` | Imagem da vista direita editada. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoEditMultiviewNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `7a25f3867776c01ab606d43a988b5491e543b72d3eedac1779fa170453c1ca21`

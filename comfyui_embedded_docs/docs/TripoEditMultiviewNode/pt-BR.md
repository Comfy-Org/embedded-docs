# Tripo: Editar Multiview

Edita as vistas de um resultado do Tripo: Image to Multiview usando uma instrução de texto separada para cada vista. Vistas sem instrução permanecem inalteradas. As imagens editadas devem ser conectadas ao Tripo: Multiview to Model para criar um modelo 3D; um conjunto de vistas múltiplas editado não pode ser editado novamente.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `multiview_task_id` | ID da tarefa do resultado do Tripo: Image to Multiview cujas vistas serão editadas. Deve vir do nó Tripo: Image to Multiview. | MULTIVIEW_TASK_ID | Sim | ID da tarefa |
| `front_prompt` | Instrução de texto que descreve a edição a ser aplicada à vista frontal. Quando vazia, a vista frontal permanece inalterada. Padrão: string vazia. | STRING | Não | Texto multilinha |
| `left_prompt` | Instrução de texto que descreve a edição a ser aplicada à vista esquerda. Quando vazia, a vista esquerda permanece inalterada. Padrão: string vazia. | STRING | Não | Texto multilinha |
| `back_prompt` | Instrução de texto que descreve a edição a ser aplicada à vista traseira. Quando vazia, a vista traseira permanece inalterada. Padrão: string vazia. | STRING | Não | Texto multilinha |
| `right_prompt` | Instrução de texto que descreve a edição a ser aplicada à vista direita. Quando vazia, a vista direita permanece inalterada. Padrão: string vazia. | STRING | Não | Texto multilinha |

Observação: Pelo menos um dos quatro prompts (`front_prompt`, `left_prompt`, `back_prompt`, `right_prompt`) deve conter texto não vazio; texto composto apenas por espaços em branco é tratado como vazio e, se todos os prompts estiverem vazios, o nó gera um erro.

Observação: O custo é de aproximadamente 0,05 USD por vista que tiver uma instrução de edição.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `front` | Imagem editada da vista frontal. | IMAGE |
| `left` | Imagem editada da vista esquerda. | IMAGE |
| `back` | Imagem editada da vista traseira. | IMAGE |
| `right` | Imagem editada da vista direita. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoEditMultiviewNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `db8b0a3ffe4332fcbcaac4da0d7b07217d01d2f05526750540f6036293e013ab`

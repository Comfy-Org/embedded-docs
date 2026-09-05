# TripoImageToMultiviewNode

Gera as vistas frontal, esquerda, traseira e direita do objeto a partir de uma única imagem de entrada, usando a API Tripo. Esta é uma tarefa paga, cobrada em aproximadamente 0,10 USD. O nó faz o upload da imagem, aguarda a conclusão da tarefa de geração na Tripo e retorna as quatro vistas juntamente com o ID da tarefa multiview.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `image` | A imagem de origem do objeto a partir da qual a Tripo gera as vistas frontal, esquerda, traseira e direita. Exatamente uma imagem é usada na solicitação. | IMAGE | Sim | Uma única imagem |

Nota: O nó chama a API em nuvem da Tripo e aguarda a conclusão da tarefa de geração. Uma tarefa típica leva cerca de 25 segundos. A autenticação é tratada automaticamente por meio das entradas ocultas do nó, portanto, nenhuma chave de API da Tripo precisa ser fornecida no fluxo de trabalho.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| MULTIVIEW_TASK_ID | O identificador da tarefa retornado pela Tripo para a solicitação de geração de imagens multiview. É um identificador do tipo string que pode ser usado para referenciar a tarefa concluída. | MULTIVIEW_TASK_ID |
| front | A vista frontal gerada do objeto. | IMAGE |
| left | A vista lateral esquerda gerada do objeto. | IMAGE |
| back | A vista traseira gerada do objeto. | IMAGE |
| right | A vista lateral direita gerada do objeto. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoImageToMultiviewNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `3beca1feeb88aa080330e6867ffd7076bd45b2c52471d1bfacc71f66452211a5`

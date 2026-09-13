# Tripo: Imagem para Multiview

Gera vistas frontal, esquerda, traseira e direita do sujeito a partir de uma única imagem de entrada usando a API do Tripo. A imagem é enviada, uma tarefa de geração multivisão é iniciada e consultada até ser concluída, e as quatro vistas resultantes são retornadas junto com o ID da tarefa. Esta é uma tarefa paga, cobrada em aproximadamente US$ 0,10.

## Entradas

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `image` | A imagem de origem do sujeito a partir da qual o Tripo gera as vistas frontal, esquerda, traseira e direita. Apenas uma imagem é usada para a requisição, mesmo se um lote for fornecido. | IMAGE | Sim | Imagem única |

Nota: O nó chama a API em nuvem do Tripo e aguarda a conclusão da tarefa de geração. Uma tarefa típica leva cerca de 25 segundos. A autenticação é tratada automaticamente por meio das entradas ocultas do nó, portanto nenhuma chave de API do Tripo precisa ser fornecida no fluxo de trabalho. O nó exige todas as quatro URLs de vistas na resposta do Tripo (`front_view_url`, `left_view_url`, `back_view_url`, `right_view_url`); se qualquer vista estiver ausente, a execução falha com um erro.

## Saídas

| Nome de saída | Descrição | Tipo de dados |
|-------------|-------------|-----------|
| `multiview task_id` | O identificador da tarefa retornado pelo Tripo para a requisição de geração de imagens multivisão. Pode ser usado para referenciar a tarefa concluída, por exemplo, ao refinar as vistas com Tripo: Edit Multiview. | MULTIVIEW_TASK_ID |
| `front` | A vista frontal gerada do sujeito. | IMAGE |
| `left` | A vista lateral esquerda gerada do sujeito. | IMAGE |
| `back` | A vista traseira gerada do sujeito. | IMAGE |
| `right` | A vista lateral direita gerada do sujeito. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoImageToMultiviewNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `7e96d327940f1f09a3e84031c773c1439380f20afae49c79fd4350fcf0aba5da`

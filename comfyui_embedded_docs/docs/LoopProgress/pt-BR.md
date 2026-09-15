# LoopProgress

LoopProgress é um nó auxiliar apenas para desenvolvimento que reporta o progresso de um loop à interface do servidor do ComfyUI. A cada execução, ele envia o texto "Iteration X / Y" ao cliente e retorna a posição atual da iteração inalterada, o que permite que ele fique em linha dentro de um loop sem alterar o fluxo de dados.

## Entradas

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `start_id` | Identificador da instância de prompt/loop à qual a mensagem de progresso pertence. O primeiro item da lista fornecida é usado para direcionar o texto de progresso à execução em andamento correta. | STRING | Sim | - |
| `position` | A posição atual da iteração (índice). O primeiro item da lista fornecida é usado na mensagem de progresso e também é retornado como saída. | INT | Sim | - |
| `total` | O número total de iterações. Usado junto com `position` para construir a mensagem de progresso "Iteration X / Y". | INT | Sim | - |

Observação: este nó é declarado com entradas de lista (`is_input_list=True`) e aceita todas as entradas, então cada valor conectado é tratado como uma lista e somente seu primeiro elemento é lido. O nó sempre é executado (sua impressão digital de entrada é fixa), então ele é reexecutado a cada passagem do loop.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|-------------|-------------|-----------|
| `position` | A posição atual da iteração, repassada inalterada a partir da entrada `position`. | INT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoopProgress/pt-BR.md)

---
**Source fingerprint (SHA-256):** `505ba814b93533679516b4f4239f5eee0dbac125d7ea16746c6cdbb7a68f803d`

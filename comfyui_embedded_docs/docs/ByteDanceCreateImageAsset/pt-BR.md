> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceCreateImageAsset/pt-BR.md)

Este nó cria um ativo de imagem pessoal para o serviço Seedance 2.0 da ByteDance. Ele faz upload de uma imagem de entrada e a registra em um grupo de ativos especificado. Se nenhum ID de grupo for fornecido, ele iniciará um processo de autenticação de pessoa real no seu navegador para criar um novo grupo antes de adicionar o ativo.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|---------------|-------------|-----------|-----------|
| `image` | IMAGE | Sim | | A imagem a ser registrada como um ativo pessoal. |
| `group_id` | STRING | Não | | Reutiliza um ID de grupo de ativos Seedance existente para evitar verificação humana repetida para a mesma pessoa. Deixe vazio para executar a autenticação de pessoa real no navegador e criar um novo grupo (padrão: vazio). |

**Restrições da Imagem:**
*   A largura da imagem deve estar entre 300 e 6000 pixels.
*   A altura da imagem deve estar entre 300 e 6000 pixels.
*   A proporção da imagem deve estar entre 0,4:1 e 2,5:1.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|---------------|---------------|-----------|
| `asset_id` | STRING | O identificador único para o ativo de imagem recém-criado. |
| `group_id` | STRING | O identificador para o grupo de ativos. Será o `group_id` fornecido ou um recém-criado. |
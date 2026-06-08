Este nó cria um ativo de imagem pessoal para o serviço Seedance 2.0 da ByteDance. Ele faz upload de uma imagem de entrada e a registra em um grupo de ativos especificado. Se nenhum ID de grupo for fornecido, ele iniciará um processo de autenticação de pessoa real no seu navegador para criar um novo grupo antes de adicionar o ativo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `image` | A imagem a ser registrada como um ativo pessoal. | IMAGE | Sim |  |
| `group_id` | Reutiliza um ID de grupo de ativos Seedance existente para evitar repetir a verificação humana para a mesma pessoa. Deixe vazio para executar a autenticação de pessoa real no navegador e criar um novo grupo (padrão: vazio). | STRING | Não |  |

**Restrições da Imagem:**
*   A largura da imagem deve estar entre 300 e 6000 pixels.
*   A altura da imagem deve estar entre 300 e 6000 pixels.
*   A proporção da imagem deve estar entre 0,4:1 e 2,5:1.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `asset_id` | O identificador único para o ativo de imagem recém-criado. | STRING |
| `group_id` | O identificador para o grupo de ativos. Será o `group_id` fornecido ou um recém-criado. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceCreateImageAsset/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b8b7b4cbbc16a8bb0102982757496ad4e8140bd87155902668c0be0d8b4d3d98`

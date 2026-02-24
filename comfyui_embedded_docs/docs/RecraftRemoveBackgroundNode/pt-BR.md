> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftRemoveBackgroundNode/pt-BR.md)

Este nó remove o fundo de imagens utilizando o serviço de API Recraft. Ele processa cada imagem no lote de entrada e retorna tanto as imagens processadas com fundos transparentes quanto as máscaras alfa correspondentes que indicam as áreas de fundo removidas.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Sim | - | A(s) imagem(ns) de entrada a ser(em) processada(s) para remoção de fundo |
| `auth_token` | STRING | Não | - | Token de autenticação para acesso à API Recraft |
| `comfy_api_key` | STRING | Não | - | Chave de API para integração com o serviço Comfy.org |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `image` | IMAGE | Imagens processadas com fundos transparentes |
| `mask` | MASK | Máscaras do canal alfa indicando as áreas de fundo removidas |

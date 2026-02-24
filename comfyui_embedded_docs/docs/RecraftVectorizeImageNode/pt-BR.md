> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftVectorizeImageNode/pt-BR.md)

Gera SVG de forma síncrona a partir de uma imagem de entrada. Este nó converte imagens rasterizadas em formato de gráficos vetoriais processando cada imagem do lote de entrada e combinando os resultados em uma única saída SVG.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Sim | - | A imagem de entrada a ser convertida para o formato SVG |
| `auth_token` | AUTH_TOKEN_COMFY_ORG | Não | - | Token de autenticação para acesso à API |
| `comfy_api_key` | API_KEY_COMFY_ORG | Não | - | Chave de API para os serviços do Comfy.org |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `SVG` | SVG | A saída de gráficos vetoriais gerada, combinando todas as imagens processadas |

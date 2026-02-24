> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftCrispUpscaleNode/pt-BR.md)

Melhora a imagem de forma síncrona. Aprimora uma imagem raster fornecida usando a ferramenta 'crisp upscale', aumentando a resolução da imagem, tornando-a mais nítida e limpa.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Sim | - | A imagem de entrada a ser melhorada |
| `auth_token` | STRING | Não | - | Token de autenticação para a API do Recraft |
| `comfy_api_key` | STRING | Não | - | Chave de API para os serviços do Comfy.org |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `image` | IMAGE | A imagem melhorada com resolução e clareza aprimoradas |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageModifyNode/pt-BR.md)

Modifica imagens de forma síncrona com base em um prompt e na proporção de aspecto. Este nó recebe uma imagem de entrada e a transforma de acordo com o prompt de texto fornecido, mantendo a proporção de aspecto original da imagem.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Sim | - | A imagem de entrada a ser modificada |
| `prompt` | STRING | Sim | - | Prompt para a geração da imagem (padrão: "") |
| `image_weight` | FLOAT | Não | 0.0-0.98 | Peso da imagem; quanto mais próximo de 1.0, menos a imagem será modificada (padrão: 0.1) |
| `model` | MODEL | Sim | Múltiplas opções disponíveis | O modelo Luma a ser usado para a modificação da imagem |
| `seed` | INT | Não | 0-18446744073709551615 | Semente para determinar se o nó deve ser executado novamente; os resultados reais são não determinísticos independentemente da semente (padrão: 0) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `image` | IMAGE | A imagem modificada gerada pelo modelo Luma |

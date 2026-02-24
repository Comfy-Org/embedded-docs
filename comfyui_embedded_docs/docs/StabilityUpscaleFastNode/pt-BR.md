> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityUpscaleFastNode/pt-BR.md)

Aumenta rapidamente uma imagem via chamada de API da Stability para 4x seu tamanho original. Este nó é especificamente destinado a aumentar a escala de imagens de baixa qualidade ou comprimidas, enviando-as para o serviço de upscaling rápido da Stability AI.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Sim | - | A imagem de entrada a ser aumentada em escala |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `output` | IMAGE | A imagem com escala aumentada retornada pela API da Stability AI |

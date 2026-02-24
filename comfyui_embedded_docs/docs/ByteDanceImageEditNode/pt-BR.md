> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceImageEditNode/pt-BR.md)

O nó ByteDance Image Edit permite modificar imagens usando os modelos de IA da ByteDance por meio de uma API. Você fornece uma imagem de entrada e um prompt de texto descrevendo as alterações desejadas, e o nó processa a imagem de acordo com suas instruções. O nó gerencia a comunicação com a API automaticamente e retorna a imagem editada.

## Entradas

| Parâmetro | Tipo de Dado | Tipo de Entrada | Padrão | Intervalo | Descrição |
|-----------|-----------|------------|---------|-------|-------------|
| `model` | MODEL | COMBO | seededit_3 | Opções de Image2ImageModelName | Nome do modelo |
| `image` | IMAGE | IMAGE | - | - | A imagem base a ser editada |
| `prompt` | STRING | STRING | "" | - | Instrução para editar a imagem |
| `seed` | INT | INT | 0 | 0-2147483647 | Semente a ser usada para a geração |
| `guidance_scale` | FLOAT | FLOAT | 5.5 | 1.0-10.0 | Valores mais altos fazem a imagem seguir o prompt mais de perto |
| `watermark` | BOOLEAN | BOOLEAN | True | - | Se deve adicionar uma marca d'água "Gerado por IA" à imagem |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | A imagem editada retornada pela API da ByteDance |

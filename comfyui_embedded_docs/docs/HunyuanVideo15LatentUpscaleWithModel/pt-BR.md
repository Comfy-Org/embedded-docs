> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15LatentUpscaleWithModel/pt-BR.md)

O nó **Hunyuan Video 15 Latent Upscale With Model** aumenta a resolução de uma representação de imagem latente. Primeiro, ele faz o *upscale* das amostras latentes para um tamanho especificado usando um método de interpolação escolhido e, em seguida, refina o resultado ampliado usando um modelo especializado de *upscale* Hunyuan Video 1.5 para melhorar a qualidade.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model` | LATENT_UPSCALE_MODEL | Sim | N/A | O modelo de *upscale* latente Hunyuan Video 1.5 usado para refinar as amostras ampliadas. |
| `samples` | LATENT | Sim | N/A | A representação de imagem latente a ser ampliada. |
| `upscale_method` | COMBO | Não | `"nearest-exact"`<br>`"bilinear"`<br>`"area"`<br>`"bicubic"`<br>`"bislerp"` | O algoritmo de interpolação usado para a etapa inicial de *upscale* (padrão: `"bilinear"`). |
| `width` | INT | Não | 0 a 16384 | A largura alvo para o latente ampliado, em pixels. Um valor de 0 calculará a largura automaticamente com base na altura alvo e na proporção original. A largura final da saída será um múltiplo de 16 (padrão: 1280). |
| `height` | INT | Não | 0 a 16384 | A altura alvo para o latente ampliado, em pixels. Um valor de 0 calculará a altura automaticamente com base na largura alvo e na proporção original. A altura final da saída será um múltiplo de 16 (padrão: 720). |
| `crop` | COMBO | Não | `"disabled"`<br>`"center"` | Determina como o latente ampliado é cortado para se ajustar às dimensões alvo. |

**Nota sobre Dimensões:** Se tanto `width` quanto `height` forem definidos como 0, o nó retorna as `samples` de entrada inalteradas. Se apenas uma dimensão for definida como 0, a outra dimensão será calculada para preservar a proporção original. As dimensões finais são sempre ajustadas para ter pelo menos 64 pixels e serem divisíveis por 16.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `LATENT` | LATENT | A representação de imagem latente ampliada e refinada pelo modelo. |

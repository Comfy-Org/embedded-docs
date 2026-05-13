> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentUpscale/pt-BR.md)

O nó LatentUpscale foi projetado para aumentar a resolução de representações latentes de imagens. Ele permite ajustar as dimensões da imagem de saída e o método de ampliação, oferecendo flexibilidade para melhorar a resolução de imagens latentes.

## Entradas

| Parâmetro | Tipo de Dados | Descrição |
|-----------|---------------|-----------|
| `amostras` | `LATENT` | A representação latente de uma imagem a ser ampliada. Este parâmetro é essencial para determinar o ponto de partida do processo de ampliação. |
| `método_de_upscale` | COMBO[STRING] | Especifica o método usado para ampliar a imagem latente. Diferentes métodos podem afetar a qualidade e as características da imagem ampliada. |
| `largura` | `INT` | A largura desejada para a imagem ampliada. Se definido como 0, será calculado com base na altura para manter a proporção. |
| `altura` | `INT` | A altura desejada para a imagem ampliada. Se definido como 0, será calculado com base na largura para manter a proporção. |
| `corte` | COMBO[STRING] | Determina como a imagem ampliada deve ser cortada, afetando a aparência final e as dimensões da saída. |

## Saídas

| Parâmetro | Tipo de Dados | Descrição |
|-----------|---------------|-----------|
| `latent` | `LATENT` | A representação latente ampliada da imagem, pronta para processamento adicional ou geração. |
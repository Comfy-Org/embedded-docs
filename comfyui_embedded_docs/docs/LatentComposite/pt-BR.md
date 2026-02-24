> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentComposite/pt-BR.md)

O nó LatentComposite é projetado para mesclar ou fundir duas representações latentes em uma única saída. Este processo é essencial para criar imagens ou características compostas, combinando os atributos das latentes de entrada de maneira controlada.

## Entradas

| Parâmetro    | Tipo de Dados | Descrição |
|--------------|-------------|-------------|
| `samples_to` | `LATENT`    | A representação latente 'samples_to' sobre a qual a 'samples_from' será composta. Serve como base para a operação de composição. |
| `samples_from` | `LATENT` | A representação latente 'samples_from' a ser composta sobre a 'samples_to'. Contribui com suas características para a saída composta final. |
| `x`          | `INT`      | A coordenada x (posição horizontal) onde a latente 'samples_from' será posicionada sobre a 'samples_to'. Determina o alinhamento horizontal da composição. |
| `y`          | `INT`      | A coordenada y (posição vertical) onde a latente 'samples_from' será posicionada sobre a 'samples_to'. Determina o alinhamento vertical da composição. |
| `feather`    | `INT`      | Um booleano que indica se a latente 'samples_from' deve ser redimensionada para corresponder à 'samples_to' antes da composição. Isso pode afetar a escala e a proporção do resultado composto. |

## Saídas

| Parâmetro | Tipo de Dados | Descrição |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | A saída é uma representação latente composta, mesclando as características das latentes 'samples_to' e 'samples_from' com base nas coordenadas e na opção de redimensionamento especificadas. |

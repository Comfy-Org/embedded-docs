> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/InpaintModelConditioning/pt-BR.md)

O nó InpaintModelConditioning é projetado para facilitar o processo de condicionamento para modelos de inpainting, permitindo a integração e manipulação de várias entradas de condicionamento para personalizar a saída do inpainting. Ele abrange uma ampla gama de funcionalidades, desde carregar checkpoints de modelos específicos e aplicar modelos de estilo ou control net, até codificar e combinar elementos de condicionamento, servindo assim como uma ferramenta abrangente para personalizar tarefas de inpainting.

## Entradas

| Parâmetro | Tipo Comfy         | Descrição |
|-----------|--------------------|-------------|
| `positive`| `CONDITIONING`     | Representa as informações ou parâmetros de condicionamento positivo a serem aplicados ao modelo de inpainting. Esta entrada é crucial para definir o contexto ou as restrições sob as quais a operação de inpainting deve ser realizada, afetando significativamente a saída final. |
| `negative`| `CONDITIONING`     | Representa as informações ou parâmetros de condicionamento negativo a serem aplicados ao modelo de inpainting. Esta entrada é essencial para especificar as condições ou contextos a serem evitados durante o processo de inpainting, influenciando assim a saída final. |
| `vae`     | `VAE`              | Especifica o modelo VAE a ser usado no processo de condicionamento. Esta entrada é crucial para determinar a arquitetura específica e os parâmetros do modelo VAE que serão utilizados. |
| `pixels`  | `IMAGE`            | Representa os dados de pixel da imagem a ser submetida ao inpainting. Esta entrada é essencial para fornecer o contexto visual necessário para a tarefa de inpainting. |
| `mask`    | `MASK`             | Especifica a máscara a ser aplicada à imagem, indicando as áreas a serem preenchidas. Esta entrada é crucial para definir as regiões específicas dentro da imagem que requerem inpainting. |

## Saídas

| Parâmetro | Tipo de Dados | Descrição |
|-----------|--------------|-------------|
| `positive`| `CONDITIONING` | As informações de condicionamento positivo modificadas após o processamento, prontas para serem aplicadas ao modelo de inpainting. Esta saída é essencial para guiar o processo de inpainting de acordo com as condições positivas especificadas. |
| `negative`| `CONDITIONING` | As informações de condicionamento negativo modificadas após o processamento, prontas para serem aplicadas ao modelo de inpainting. Esta saída é essencial para guiar o processo de inpainting de acordo com as condições negativas especificadas. |
| `latent`  | `LATENT`     | A representação latente derivada do processo de condicionamento. Esta saída é crucial para compreender as características subjacentes da imagem que está sendo submetida ao inpainting. |

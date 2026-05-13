> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/InpaintModelConditioning/pt-BR.md)

O nó **InpaintModelConditioning** foi projetado para facilitar o processo de condicionamento para modelos de inpaint, permitindo a integração e manipulação de diversas entradas de condicionamento para personalizar o resultado da pintura. Ele abrange uma ampla gama de funcionalidades, desde carregar checkpoints específicos de modelos e aplicar modelos de estilo ou control net, até codificar e combinar elementos de condicionamento, servindo assim como uma ferramenta abrangente para customizar tarefas de inpaint.

## Entradas

| Parâmetro | Tipo Comfy        | Descrição |
|-----------|--------------------|-------------|
| `positive`| `CONDITIONING`     | Representa as informações ou parâmetros de condicionamento positivo que serão aplicados ao modelo de inpaint. Esta entrada é crucial para definir o contexto ou as restrições sob as quais a operação de inpaint deve ser realizada, afetando significativamente o resultado final. |
| `negative`| `CONDITIONING`     | Representa as informações ou parâmetros de condicionamento negativo que serão aplicados ao modelo de inpaint. Esta entrada é essencial para especificar as condições ou contextos a serem evitados durante o processo de inpaint, influenciando assim o resultado final. |
| `vae`     | `VAE`              | Especifica o modelo VAE a ser utilizado no processo de condicionamento. Esta entrada é crucial para determinar a arquitetura e os parâmetros específicos do modelo VAE que será utilizado. |
| `pixels`  | `IMAGE`            | Representa os dados de pixel da imagem a ser pintada. Esta entrada é essencial para fornecer o contexto visual necessário para a tarefa de inpaint. |
| `mask`    | `MASK`             | Especifica a máscara a ser aplicada à imagem, indicando as áreas que serão pintadas. Esta entrada é crucial para definir as regiões específicas dentro da imagem que necessitam de inpaint. |

## Saídas

| Parâmetro | Tipo de Dados | Descrição |
|-----------|--------------|-------------|
| `positive`| `CONDITIONING` | As informações de condicionamento positivo modificadas após o processamento, prontas para serem aplicadas ao modelo de inpaint. Esta saída é essencial para guiar o processo de inpaint de acordo com as condições positivas especificadas. |
| `negative`| `CONDITIONING` | As informações de condicionamento negativo modificadas após o processamento, prontas para serem aplicadas ao modelo de inpaint. Esta saída é essencial para guiar o processo de inpaint de acordo com as condições negativas especificadas. |
| `latent`  | `LATENT`     | A representação latente derivada do processo de condicionamento. Esta saída é crucial para compreender as características e os atributos subjacentes da imagem que está sendo pintada. |
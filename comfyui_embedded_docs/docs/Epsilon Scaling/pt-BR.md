> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Epsilon%20Scaling/pt-BR.md)

Este nó implementa o método de Escalonamento de Épsilon do artigo de pesquisa "Elucidating the Exposure Bias in Diffusion Models". Ele funciona escalando o ruído previsto durante o processo de amostragem para ajudar a reduzir o viés de exposição, o que pode levar a uma qualidade melhorada nas imagens geradas. Esta implementação utiliza o "cronograma uniforme" recomendado pelo artigo.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sim | - | O modelo ao qual o patch de escalonamento de épsilon será aplicado. |
| `scaling_factor` | FLOAT | Não | 0.5 - 1.5 | O fator pelo qual o ruído previsto é escalado. Um valor maior que 1.0 reduz o ruído, enquanto um valor menor que 1.0 o aumenta (padrão: 1.005). |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `model` | MODEL | Uma versão modificada do modelo de entrada com a função de escalonamento de épsilon aplicada ao seu processo de amostragem. |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MakeTrainingDataset/pt-BR.md)

Este nó prepara dados para treinamento codificando imagens e texto. Ele recebe uma lista de imagens e uma lista correspondente de legendas de texto, então usa um modelo VAE para converter as imagens em representações latentes e um modelo CLIP para converter o texto em dados de condicionamento. Os pares resultantes de latentes e condicionamentos são fornecidos como listas, prontos para uso em fluxos de trabalho de treinamento.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `images` | IMAGE | Sim | N/A | Lista de imagens a serem codificadas. |
| `vae` | VAE | Sim | N/A | Modelo VAE para codificar imagens em latentes. |
| `clip` | CLIP | Sim | N/A | Modelo CLIP para codificar texto em condicionamento. |
| `texts` | STRING | Não | N/A | Lista de legendas de texto. Pode ter comprimento n (correspondendo às imagens), 1 (repetido para todas) ou ser omitida (usa string vazia). |

**Restrições dos Parâmetros:**

* O número de itens na lista `texts` deve ser 0, 1 ou corresponder exatamente ao número de itens na lista `images`. Se for 0, uma string vazia é usada para todas as imagens. Se for 1, esse texto único é repetido para todas as imagens.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `latents` | LATENT | Lista de dicionários latentes. |
| `conditioning` | CONDITIONING | Lista de listas de condicionamento. |

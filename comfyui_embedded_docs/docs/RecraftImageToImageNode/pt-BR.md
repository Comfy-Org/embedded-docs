> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftImageToImageNode/pt-BR.md)

Este nó modifica uma imagem existente com base em um prompt de texto e um parâmetro de força. Ele utiliza a API Recraft para transformar a imagem de entrada de acordo com a descrição fornecida, mantendo um certo grau de semelhança com a imagem original, definido pela configuração de força.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Sim | - | A imagem de entrada a ser modificada |
| `prompt` | STRING | Sim | - | Prompt para a geração da imagem (padrão: "") |
| `n` | INT | Sim | 1-6 | O número de imagens a serem geradas (padrão: 1) |
| `strength` | FLOAT | Sim | 0.0-1.0 | Define a diferença em relação à imagem original, deve estar no intervalo [0, 1], onde 0 significa quase idêntica e 1 significa semelhança mínima (padrão: 0.5) |
| `seed` | INT | Sim | 0-18446744073709551615 | Semente para determinar se o nó deve ser reexecutado; os resultados reais são não determinísticos, independentemente da semente (padrão: 0) |
| `recraft_style` | STYLEV3 | Não | - | Seleção de estilo opcional para a geração da imagem |
| `negative_prompt` | STRING | Não | - | Uma descrição de texto opcional de elementos indesejados na imagem (padrão: "") |
| `recraft_controls` | CONTROLS | Não | - | Controles adicionais opcionais sobre a geração via o nó Recraft Controls |

**Observação:** O parâmetro `seed` apenas dispara a reexecução do nó, mas não garante resultados determinísticos. O parâmetro de força é arredondado internamente para 2 casas decimais.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `image` | IMAGE | A(s) imagem(ns) gerada(s) com base na imagem de entrada e no prompt |

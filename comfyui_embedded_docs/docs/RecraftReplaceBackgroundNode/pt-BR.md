> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftReplaceBackgroundNode/pt-BR.md)

Substituir o fundo da imagem com base no prompt fornecido. Este nó utiliza a API Recraft para gerar novos fundos para suas imagens de acordo com sua descrição textual, permitindo que você transforme completamente o plano de fundo enquanto mantém o assunto principal intacto.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Sim | - | A imagem de entrada a ser processada |
| `prompt` | STRING | Sim | - | Prompt para a geração da imagem (padrão: vazio) |
| `n` | INT | Sim | 1-6 | O número de imagens a serem geradas (padrão: 1) |
| `seed` | INT | Sim | 0-18446744073709551615 | Semente para determinar se o nó deve ser reexecutado; os resultados reais são não determinísticos independentemente da semente (padrão: 0) |
| `recraft_style` | STYLEV3 | Não | - | Seleção de estilo opcional para o fundo gerado |
| `negative_prompt` | STRING | Não | - | Uma descrição textual opcional de elementos indesejados na imagem (padrão: vazio) |

**Observação:** O parâmetro `seed` controla quando o nó é reexecutado, mas não garante resultados determinísticos devido à natureza da API externa.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | A(s) imagem(ns) gerada(s) com o fundo substituído |

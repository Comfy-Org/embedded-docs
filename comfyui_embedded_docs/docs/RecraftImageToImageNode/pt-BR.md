> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftImageToImageNode/pt-BR.md)

Este nó modifica uma imagem existente com base em um prompt de texto e um parâmetro de intensidade. Ele utiliza a API Recraft para transformar a imagem de entrada de acordo com a descrição fornecida, mantendo alguma similaridade com a imagem original com base na configuração de intensidade.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|--------------|-------------|-----------|-----------|
| `image` | IMAGE | Sim | - | A imagem de entrada a ser modificada |
| `prompt` | STRING | Sim | - | Prompt para a geração da imagem (padrão: "", comprimento máximo: 1000 caracteres) |
| `n` | INT | Sim | 1-6 | O número de imagens a serem geradas (padrão: 1) |
| `strength` | FLOAT | Sim | 0.0-1.0 | Define a diferença em relação à imagem original, deve estar em [0, 1], onde 0 significa quase idêntico e 1 significa similaridade mínima (padrão: 0.5) |
| `seed` | INT | Sim | 0-18446744073709551615 | Semente para determinar se o nó deve ser reexecutado; os resultados reais são não determinísticos independentemente da semente (padrão: 0) |
| `recraft_style` | STYLEV3 | Não | - | Seleção opcional de estilo para a geração da imagem. Se não for fornecido, o padrão é `realistic_image` |
| `negative_prompt` | STRING | Não | - | Uma descrição textual opcional de elementos indesejados na imagem (padrão: "") |
| `recraft_controls` | CONTROLS | Não | - | Controles adicionais opcionais sobre a geração através do nó Recraft Controls |

**Observação:** O parâmetro `seed` apenas aciona a reexecução do nó, mas não garante resultados determinísticos. O parâmetro de intensidade é arredondado para 2 casas decimais internamente. O prompt é validado e não deve exceder 1000 caracteres. Se `recraft_style` não for fornecido, o nó usará o estilo `realistic_image` como padrão.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `image` | IMAGE | A(s) imagem(ns) gerada(s) com base na imagem de entrada e no prompt |

---
**Source fingerprint (SHA-256):** `e47ab70e77186e62c253c976cdd7942cfb949ba6461914d2b4341f3eca8e14aa`

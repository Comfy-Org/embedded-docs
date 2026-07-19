# Recraft Imagem para Imagem

Este nó modifica uma imagem existente com base em um prompt de texto e um parâmetro de intensidade. Ele utiliza a API Recraft para transformar a imagem de entrada de acordo com a descrição fornecida, mantendo alguma similaridade com a imagem original com base na configuração de intensidade.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `imagem` | A imagem de entrada a ser modificada | IMAGE | Sim | - |
| `prompt` | Prompt para a geração da imagem (padrão: "", comprimento máximo: 1000 caracteres) | STRING | Sim | - |
| `n` | O número de imagens a serem geradas (padrão: 1) | INT | Sim | 1-6 |
| `intensidade` | Define a diferença em relação à imagem original, deve estar em [0, 1], onde 0 significa quase idêntico e 1 significa similaridade mínima (padrão: 0.5) | FLOAT | Sim | 0.0-1.0 |
| `semente` | Semente para determinar se o nó deve ser reexecutado; os resultados reais são não determinísticos independentemente da semente (padrão: 0) | INT | Sim | 0-18446744073709551615 |
| `recraft_style` | Seleção opcional de estilo para a geração da imagem. Se não for fornecido, o padrão é `realistic_image` | STYLEV3 | Não | - |
| `prompt_negativo` | Uma descrição textual opcional de elementos indesejados na imagem (padrão: "") | STRING | Não | - |
| `recraft_controls` | Controles adicionais opcionais sobre a geração através do nó Recraft Controls | CONTROLS | Não | - |

**Observação:** O parâmetro `seed` apenas aciona a reexecução do nó, mas não garante resultados determinísticos. O parâmetro de intensidade é arredondado para 2 casas decimais internamente. O prompt é validado e não deve exceder 1000 caracteres. Se `recraft_style` não for fornecido, o nó usará o estilo `realistic_image` como padrão.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `imagem` | A(s) imagem(ns) gerada(s) com base na imagem de entrada e no prompt | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftImageToImageNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `e47ab70e77186e62c253c976cdd7942cfb949ba6461914d2b4341f3eca8e14aa`

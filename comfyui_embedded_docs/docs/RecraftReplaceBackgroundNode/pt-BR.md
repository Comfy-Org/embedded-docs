# Recraft Substituir Fundo

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftReplaceBackgroundNode/en.md)

Substitui o fundo da imagem com base no prompt fornecido. Este nó utiliza a API Recraft para gerar novos fundos para suas imagens de acordo com sua descrição textual, permitindo transformar completamente o fundo enquanto mantém o objeto principal intacto.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `imagem` | A imagem de entrada a ser processada | IMAGE | Sim | - |
| `prompt` | Prompt para a geração da imagem (padrão: vazio) | STRING | Sim | - |
| `n` | O número de imagens a serem geradas (padrão: 1) | INT | Sim | 1-6 |
| `semente` | Semente para determinar se o nó deve ser reexecutado; os resultados reais são não determinísticos independentemente da semente (padrão: 0) | INT | Sim | 0-18446744073709551615 |
| `recraft_style` | Seleção opcional de estilo para o fundo gerado. Se não for fornecido, o padrão é o estilo "realistic_image" | STYLEV3 | Não | - |
| `prompt_negativo` | Uma descrição textual opcional de elementos indesejados na imagem (padrão: vazio) | STRING | Não | - |

**Nota:** O parâmetro `seed` controla quando o nó é reexecutado, mas não garante resultados determinísticos devido à natureza da API externa.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `IMAGE` | A(s) imagem(ns) gerada(s) com o fundo substituído | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftReplaceBackgroundNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `305cb8c542159a089b1fa03971205b23d50c8a328af006e284fb27011070f6bd`

# Recraft Substituir Fundo

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `imagem` | A imagem de entrada a ser processada | IMAGE | Sim | - |
| `prompt` | Prompt para a geração da imagem (padrão: vazio) | STRING | Sim | - |
| `n` | O número de imagens a gerar (padrão: 1) | INT | Sim | 1-6 |
| `semente` | Seed para determinar se o nó deve ser executado novamente; os resultados reais são não determinísticos independentemente da seed (padrão: 0) | INT | Sim | 0-18446744073709551615 |
| `recraft_style` | Seleção opcional de estilo para o fundo gerado. Se não for fornecida, o padrão é o estilo "realistic_image" | STYLEV3 | Não | - |
| `prompt_negativo` | Uma descrição textual opcional de elementos indesejados em uma imagem (padrão: vazio) | STRING | Não | - |

**Nota:** O parâmetro `seed` controla quando o nó é executado novamente, mas não garante resultados determinísticos devido à natureza da API externa.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|-------------|-------------|-----------|
| `IMAGE` | A(s) imagem(ns) gerada(s) com o fundo substituído. Para cada imagem de entrada, o número de resultados gerados é determinado por `n`. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftReplaceBackgroundNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `45a2607ae73cc67caa98d33bf536feda83a2021d960dec7cca76cbe0b9fc47ef`

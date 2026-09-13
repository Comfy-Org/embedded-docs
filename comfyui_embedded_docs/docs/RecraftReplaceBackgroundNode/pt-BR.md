# Recraft Substituir Fundo

Substitua o fundo da imagem com base no prompt fornecido. Este nó usa a API Recraft para gerar novos fundos para suas imagens de acordo com sua descrição de texto, permitindo transformar completamente o fundo enquanto mantém o assunto principal intacto. Cada imagem no lote de entrada é processada separadamente, e os resultados são combinados em um único lote de saída.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `image` | A imagem de entrada a ser processada | IMAGE | Sim | - |
| `prompt` | Prompt para a geração da imagem (padrão: vazio) | STRING | Sim | - |
| `n` | O número de imagens a serem geradas (padrão: 1) | INT | Sim | 1-6 |
| `seed` | Semente para determinar se o nó deve ser reexecutado; os resultados reais são não determinísticos independentemente da semente (padrão: 0) | INT | Sim | 0-18446744073709551615 |
| `recraft_style` | Seleção opcional de estilo para o fundo gerado. Se não for fornecida, o padrão é o estilo "realistic_image" | STYLEV3 | Não | - |
| `negative_prompt` | Uma descrição de texto opcional de elementos indesejados em uma imagem (padrão: vazio) | STRING | Não | - |

**Notas:**
- O parâmetro `seed` controla quando o nó é reexecutado, mas não garante resultados determinísticos devido à natureza da API externa.
- Quando `recraft_style` não está conectado ou é deixado vazio, o nó recorre ao estilo `realistic_image`.
- Quando `negative_prompt` é deixado vazio, ele não é enviado com a solicitação.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `IMAGE` | A(s) imagem(ns) gerada(s) com o fundo substituído. Para cada imagem de entrada, o número de resultados gerados é determinado por `n`. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftReplaceBackgroundNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `45a2607ae73cc67caa98d33bf536feda83a2021d960dec7cca76cbe0b9fc47ef`

# Recraft Substituir Fundo

Substituir o fundo da imagem com base no prompt fornecido. Este nó utiliza a API Recraft para gerar novos fundos para suas imagens de acordo com sua descrição textual, permitindo transformar completamente o fundo enquanto mantém o assunto principal intacto.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `image` | A imagem de entrada a ser processada | IMAGE | Sim | - |
| `prompt` | Prompt para a geração da imagem (padrão: vazio) | STRING | Sim | - |
| `n` | O número de imagens a gerar (padrão: 1) | INT | Sim | 1-6 |
| `seed` | Semente para determinar se o nó deve ser executado novamente; os resultados reais são não determinísticos independentemente da semente (padrão: 0) | INT | Sim | 0-18446744073709551615 |
| `recraft_style` | Seleção opcional de estilo para o fundo gerado. Se não for fornecida, o padrão é o estilo "realistic_image" | STYLEV3 | Não | - |
| `negative_prompt` | Uma descrição textual opcional de elementos indesejáveis em uma imagem (padrão: vazio) | STRING | Não | - |

**Observação:** O parâmetro `seed` controla quando o nó é executado novamente, mas não garante resultados determinísticos devido à natureza da API externa.

**Observação:** Cada imagem no lote de entrada é processada individualmente; o nó retorna `n` imagens com fundo substituído para cada imagem de entrada.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|-------------|-------------|-----------|
| `IMAGE` | A(s) imagem(ns) gerada(s) com fundo substituído | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftReplaceBackgroundNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `45a2607ae73cc67caa98d33bf536feda83a2021d960dec7cca76cbe0b9fc47ef`

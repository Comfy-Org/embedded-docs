> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokImageEditNode/pt-BR.md)

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokImageEditNode/en.md)

O nó Grok Image Edit modifica uma imagem existente com base em um prompt de texto. Ele usa a API Grok para gerar uma ou mais novas imagens que são variações da entrada, guiadas pela sua descrição.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Faixa | Descrição |
|-----------|---------------|-------------|-------|-----------|
| `model` | COMBO | Sim | `"grok-imagine-image-quality"`<br>`"grok-imagine-image-pro"`<br>`"grok-imagine-image"`<br>`"grok-imagine-image-beta"` | O modelo de IA específico a ser usado para edição de imagem. |
| `image` | IMAGE | Sim | | A(s) imagem(ns) de entrada a ser(em) editada(s). Suporta até 3 imagens de entrada, exceto para o modelo "pro" que suporta apenas 1. |
| `prompt` | STRING | Sim | | O prompt de texto usado para gerar a imagem editada. Deve ter pelo menos 1 caractere após remover espaços em branco. |
| `resolution` | COMBO | Sim | `"1K"`<br>`"2K"` | A resolução da imagem de saída. |
| `number_of_images` | INT | Não | 1 a 10 | Número de imagens editadas a serem geradas (padrão: 1). |
| `seed` | INT | Não | 0 a 2147483647 | Semente para determinar se o nó deve ser executado novamente; os resultados reais são não determinísticos independentemente da semente (padrão: 0). |
| `aspect_ratio` | COMBO | Não | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"9:16"`<br>`"16:9"`<br>`"9:19.5"`<br>`"19.5:9"`<br>`"9:20"`<br>`"20:9"`<br>`"1:2"`<br>`"2:1"` | A proporção de aspecto para a imagem de saída. Permitida apenas quando múltiplas imagens estão conectadas à entrada de imagem. Se definido como "auto", a proporção de aspecto é determinada automaticamente (padrão: "auto"). |

**Restrições importantes:**
- A entrada `image` suporta até 3 imagens, exceto ao usar o modelo `grok-imagine-image-pro`, que suporta apenas 1 imagem de entrada.
- O parâmetro `aspect_ratio` só pode ser definido com um valor personalizado (diferente de "auto") quando múltiplas imagens estão conectadas à entrada `image`. Definir uma proporção de aspecto personalizada com uma única imagem de entrada causará um erro.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|---------------|---------------|-----------|
| `output` | IMAGE | A(s) imagem(ns) editada(s) gerada(s) pelo nó. Se `number_of_images` for maior que 1, as saídas são concatenadas em um lote. |

---
**Source fingerprint (SHA-256):** `021d867e9e04451c0c4ef035c19fa86ebc8d4a3f64572aff33f493324d7fe308`

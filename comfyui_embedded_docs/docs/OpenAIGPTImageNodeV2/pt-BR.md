> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIGPTImageNodeV2/pt-BR.md)

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIGPTImageNodeV2/en.md)

## Visão Geral

Este nó gera imagens usando a API GPT Image da OpenAI. Ele oferece suporte a vários modelos, permite fornecer imagens de entrada para edição e pode usar uma máscara para especificar quais partes de uma imagem modificar.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `prompt` | STRING | Sim | N/A | Prompt de texto para a GPT Image (padrão: ""). |
| `model` | COMBO | Sim | `"gpt-image-2"`<br>`"gpt-image-1.5"`<br>`"gpt-image-1"` | O modelo GPT Image da OpenAI a ser usado. Selecionar um modelo revela parâmetros adicionais específicos para aquele modelo. |
| `model.size` | COMBO | Sim | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"`<br>`"2048x2048"`<br>`"2048x1152"`<br>`"1152x2048"`<br>`"3840x2160"`<br>`"2160x3840"`<br>`"Custom"` | Tamanho da imagem. Selecione 'Custom' para usar largura e altura personalizadas (padrão: "auto"). Disponível apenas para `gpt-image-2`. |
| `model.custom_width` | INT | Não | 1024 a 3840 | Usado apenas quando `size` é 'Custom'. Deve ser um múltiplo de 16 (padrão: 1024). Disponível apenas para `gpt-image-2`. |
| `model.custom_height` | INT | Não | 1024 a 3840 | Usado apenas quando `size` é 'Custom'. Deve ser um múltiplo de 16 (padrão: 1024). Disponível apenas para `gpt-image-2`. |
| `model.background` | COMBO | Sim | `"auto"`<br>`"opaque"` | Retorna imagem com ou sem fundo (padrão: "auto"). Disponível apenas para `gpt-image-2`. |
| `model.quality` | COMBO | Sim | `"standard"`<br>`"hd"` | A qualidade da imagem gerada. Disponível apenas para `gpt-image-2`. |
| `model.images` | IMAGE | Não | N/A | Imagens de entrada para edição. Disponível apenas para `gpt-image-2`. |
| `model.mask` | MASK | Não | N/A | Uma máscara para especificar quais partes da imagem de entrada editar. Disponível apenas para `gpt-image-2`. |
| `n` | INT | Sim | 1 a 8 | Quantas imagens gerar (padrão: 1). |
| `seed` | INT | Sim | 0 a 2147483647 | Semente para reprodutibilidade (padrão: 0). Observação: ainda não implementado no backend. |

**Restrições e Limitações dos Parâmetros:**

- Ao usar `gpt-image-2` com `model.size` como "Custom", o `custom_width` e `custom_height` devem ser múltiplos de 16, a borda máxima deve ser <= 3840, a proporção de aspecto não deve exceder 3:1 e a contagem total de pixels deve estar entre 655.360 e 8.294.400.
- Se uma `mask` for fornecida, uma imagem de entrada (`model.images`) é necessária. Uma máscara não pode ser usada sem uma imagem de entrada.
- Uma máscara não pode ser usada com múltiplas imagens de entrada.
- Quando uma máscara é fornecida, as dimensões da máscara devem corresponder às dimensões da imagem de entrada.
- O parâmetro `seed` atualmente não é funcional.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `image` | IMAGE | A imagem ou imagens geradas. |

---
**Source fingerprint (SHA-256):** `a757208cf6cc151594599b35b0ef73f2caf7274189e948799211c0714a6a8f89`

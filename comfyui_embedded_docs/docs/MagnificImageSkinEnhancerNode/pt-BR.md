# Magnific Realce de Pele em Imagem

O nó **Magnific Image Skin Enhancer** aplica processamento especializado de IA a imagens de retrato para melhorar a aparência da pele. Ele oferece três modos distintos para diferentes objetivos de aprimoramento: criativo para efeitos artísticos, fiel para preservar a aparência original e flexível para melhorias direcionadas, como iluminação ou realismo. O nó envia a imagem para uma API externa para processamento e retorna o resultado aprimorado.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `image` | A imagem de retrato a ser aprimorada. | IMAGE | Sim | - |
| `sharpen` | Nível de intensidade de nitidez (padrão: 0). | INT | Não | 0 a 100 |
| `smart_grain` | Nível de intensidade de granulação inteligente (padrão: 2). | INT | Não | 0 a 100 |
| `mode` | O modo de processamento a ser usado. `"creative"` é para aprimoramento artístico, `"faithful"` para preservar a aparência original e `"flexible"` para otimização direcionada. | COMBO | Sim | `"creative"`<br>`"faithful"`<br>`"flexible"` |
| `skin_detail` | Nível de aprimoramento de detalhes da pele. Esta entrada está disponível e é obrigatória apenas quando o `mode` está definido como `"faithful"` (padrão: 80). | INT | Não | 0 a 100 |
| `optimized_for` | Alvo de otimização do aprimoramento. Esta entrada está disponível e é obrigatória apenas quando o `mode` está definido como `"flexible"`. | COMBO | Não | `"enhance_skin"`<br>`"improve_lighting"`<br>`"enhance_everything"`<br>`"transform_to_real"`<br>`"no_make_up"` |

**Restrições:**

* O nó aceita exatamente uma imagem de entrada.
* A imagem de entrada deve ter altura e largura mínimas de 160 pixels.
* A proporção da imagem de entrada deve estar entre 1:3 e 3:1 (validação não rigorosa).
* O parâmetro `skin_detail` só está ativo quando `mode` está definido como `"faithful"`.
* O parâmetro `optimized_for` só está ativo quando `mode` está definido como `"flexible"`.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `image` | A imagem de retrato aprimorada. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MagnificImageSkinEnhancerNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `e02cae2e119ddab931b790865889adf53f47a2ebb03d488477c289dfda7204f5`

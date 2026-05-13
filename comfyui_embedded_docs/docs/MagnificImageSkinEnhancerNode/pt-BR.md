> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MagnificImageSkinEnhancerNode/pt-BR.md)

O nó **Magnific Image Skin Enhancer** aplica processamento especializado de IA a imagens de retrato para melhorar a aparência da pele. Ele oferece três modos distintos para diferentes objetivos de aprimoramento: criativo para efeitos artísticos, fiel para preservar a aparência original e flexível para melhorias direcionadas, como iluminação ou realismo. O nó envia a imagem para uma API externa para processamento e retorna o resultado aprimorado.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `image` | IMAGE | Sim | - | A imagem de retrato a ser aprimorada. |
| `sharpen` | INT | Não | 0 a 100 | Nível de intensidade de nitidez (padrão: 0). |
| `smart_grain` | INT | Não | 0 a 100 | Nível de intensidade de granulação inteligente (padrão: 2). |
| `mode` | COMBO | Sim | `"creative"`<br>`"faithful"`<br>`"flexible"` | O modo de processamento a ser usado. `"creative"` é para aprimoramento artístico, `"faithful"` para preservar a aparência original e `"flexible"` para otimização direcionada. |
| `skin_detail` | INT | Não | 0 a 100 | Nível de aprimoramento de detalhes da pele. Esta entrada está disponível e é obrigatória apenas quando o `mode` está definido como `"faithful"` (padrão: 80). |
| `optimized_for` | COMBO | Não | `"enhance_skin"`<br>`"improve_lighting"`<br>`"enhance_everything"`<br>`"transform_to_real"`<br>`"no_make_up"` | Alvo de otimização do aprimoramento. Esta entrada está disponível e é obrigatória apenas quando o `mode` está definido como `"flexible"`. |

**Restrições:**

* O nó aceita exatamente uma imagem de entrada.
* A imagem de entrada deve ter altura e largura mínimas de 160 pixels.
* A proporção da imagem de entrada deve estar entre 1:3 e 3:1 (validação não rigorosa).
* O parâmetro `skin_detail` só está ativo quando `mode` está definido como `"faithful"`.
* O parâmetro `optimized_for` só está ativo quando `mode` está definido como `"flexible"`.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `image` | IMAGE | A imagem de retrato aprimorada. |

---
**Source fingerprint (SHA-256):** `e02cae2e119ddab931b790865889adf53f47a2ebb03d488477c289dfda7204f5`

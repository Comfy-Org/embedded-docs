Este nó foi projetado para integrar as saídas de visão do CLIP no processo de condicionamento, ajustando a influência dessas saídas com base em parâmetros especificados de intensidade e aumento de ruído. Ele enriquece o condicionamento com contexto visual, aprimorando o processo de geração.

## Entradas

| Parâmetro | Descrição | Tipo Comfy |
| --- | --- | --- |
| `condicionamento` | Os dados de condicionamento base aos quais as saídas de visão do CLIP serão adicionadas, servindo como base para modificações posteriores. | `CONDITIONING` |
| `clip_vision_output` | A saída de um modelo de visão CLIP, fornecendo contexto visual que é integrado ao condicionamento. | `CLIP_VISION_OUTPUT` |
| `força` | Determina a intensidade da influência da saída de visão do CLIP sobre o condicionamento. | `FLOAT` |
| `aumento_ruído` | Especifica o nível de aumento de ruído a ser aplicado à saída de visão do CLIP antes de integrá-la ao condicionamento. | `FLOAT` |

## Saídas

| Parâmetro | Descrição | Tipo Comfy |
| --- | --- | --- |
| `condicionamento` | Os dados de condicionamento enriquecidos, agora contendo saídas de visão do CLIP integradas com intensidade e aumento de ruído aplicados. | `CONDITIONING` |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/unCLIPConditioning/pt-BR.md)

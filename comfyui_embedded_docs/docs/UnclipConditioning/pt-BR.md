> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/unCLIPConditioning/pt-BR.md)

Este nó foi projetado para integrar as saídas de visão do CLIP no processo de condicionamento, ajustando a influência dessas saídas com base em parâmetros especificados de intensidade e aumento de ruído. Ele enriquece o condicionamento com contexto visual, aprimorando o processo de geração.

## Entradas

| Parâmetro              | Tipo Comfy            | Descrição |
|------------------------|------------------------|-------------|
| `condicionamento`         | `CONDITIONING`         | Os dados de condicionamento base aos quais as saídas de visão do CLIP serão adicionadas, servindo como base para modificações posteriores. |
| `clip_vision_output`   | `CLIP_VISION_OUTPUT`   | A saída de um modelo de visão CLIP, fornecendo contexto visual que é integrado ao condicionamento. |
| `força`             | `FLOAT`                | Determina a intensidade da influência da saída de visão do CLIP sobre o condicionamento. |
| `aumento_ruído`   | `FLOAT`                | Especifica o nível de aumento de ruído a ser aplicado à saída de visão do CLIP antes de integrá-la ao condicionamento. |

## Saídas

| Parâmetro             | Tipo Comfy            | Descrição |
|-----------------------|------------------------|-------------|
| `condicionamento`         | `CONDITIONING`         | Os dados de condicionamento enriquecidos, agora contendo saídas de visão do CLIP integradas com intensidade e aumento de ruído aplicados. |
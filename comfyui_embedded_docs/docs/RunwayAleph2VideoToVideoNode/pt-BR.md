# Nó de Vídeo para Vídeo Runway Aleph2

Este nó edita um vídeo usando um prompt de texto com o modelo Aleph2 da Runway. Ele transforma sua gravação alterando o estilo, a iluminação, adicionando ou removendo elementos, ou mudando o ponto de vista, preservando o movimento e o ritmo originais.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Descreve o que deve aparecer na saída (1-1000 caracteres). | STRING | Sim | 1-1000 caracteres |
| `video` | Vídeo de entrada a ser editado. Deve ter 2-30 segundos a 30 fps ou menos. | VIDEO | Sim | Duração de 2-30 segundos, máximo de 30 fps |
| `seed` | Semente aleatória para geração (padrão: 0). | INT | Sim | 0 a 4294967295 |
| `public_figure_threshold` | Moderação de conteúdo para figuras públicas reconhecíveis (padrão: "low"). | COMBO | Sim | "auto"<br>"low" |
| `keyframes` | Imagens-guia ancoradas ao vídeo de entrada, provenientes de nós Aleph2 Keyframe (até 5). Use keyframes ou imagens de prompt, não ambos. | KEYFRAME | Não | Até 5 itens |
| `prompt_images` | Imagens-guia ancoradas ao vídeo de saída, provenientes de nós Aleph2 Prompt Image (até 5). Use keyframes ou imagens de prompt, não ambos. | PROMPT_IMAGE | Não | Até 5 itens |

**Restrições importantes:**
- O vídeo de entrada deve ter entre 2 e 30 segundos de duração e uma taxa de quadros de 30 fps ou menos.
- Você pode usar `keyframes` ou `prompt_images` como guia, mas não ambos ao mesmo tempo.
- Cada entrada-guia (keyframes ou imagens de prompt) suporta no máximo 5 itens.
- Os timestamps dos keyframes e os timestamps das imagens de prompt não devem exceder a duração do vídeo de entrada.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|-------------|-------------|-----------|
| `video` | O vídeo editado gerado pelo modelo Aleph2. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayAleph2VideoToVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `bda4d0f49843c1a8f311ddbce5911a2a157cae798a26f7a183b31fe41686d0b7`

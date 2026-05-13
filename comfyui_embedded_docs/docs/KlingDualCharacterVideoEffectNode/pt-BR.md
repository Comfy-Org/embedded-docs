> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingDualCharacterVideoEffectNode/pt-BR.md)

Este é um nó especializado em efeitos de vídeo com dois personagens da Kling. Ele cria vídeos com efeitos especiais baseados na cena selecionada. O nó recebe duas imagens e posiciona a primeira no lado esquerdo e a segunda no lado direito do vídeo composto. Diferentes efeitos visuais são aplicados dependendo da cena de efeito escolhida.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `image_left` | IMAGE | Sim | - | Imagem do lado esquerdo |
| `image_right` | IMAGE | Sim | - | Imagem do lado direito |
| `effect_scene` | COMBO | Sim | `"chat"`<br>`"dance"`<br>`"hug"`<br>`"kill"`<br>`"kiss"`<br>`"pat"`<br>`"punch"`<br>`"shrug"`<br>`"slap"`<br>`"tickle"` | O tipo de cena de efeito especial a ser aplicada na geração do vídeo |
| `model_name` | COMBO | Não | `"kling-v1"`<br>`"kling-v1-5"`<br>`"kling-v1-6"` | O modelo a ser usado para os efeitos dos personagens (padrão: "kling-v1") |
| `mode` | COMBO | Não | `"std"`<br>`"pro"` | O modo de geração do vídeo (padrão: "std") |
| `duration` | COMBO | Sim | `"5"`<br>`"10"` | A duração do vídeo gerado em segundos |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `output` | VIDEO | O vídeo gerado com efeitos de dois personagens |
| `duration` | STRING | As informações de duração do vídeo gerado |

---
**Source fingerprint (SHA-256):** `4ee0c3cd834e1c70e41b40b66ac98d15a8b88993e7dc9d9df9fb4fadb868f079`

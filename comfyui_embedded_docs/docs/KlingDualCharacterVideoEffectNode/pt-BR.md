# Efeitos de Vídeo com Dois Personagens Kling

Este é um nó especializado em efeitos de vídeo com dois personagens da Kling. Ele cria vídeos com efeitos especiais baseados na cena selecionada. O nó recebe duas imagens e posiciona a primeira no lado esquerdo e a segunda no lado direito do vídeo composto. Diferentes efeitos visuais são aplicados dependendo da cena de efeito escolhida.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `image_left` | Imagem do lado esquerdo | IMAGE | Sim | - |
| `image_right` | Imagem do lado direito | IMAGE | Sim | - |
| `effect_scene` | O tipo de cena de efeito especial a ser aplicada na geração do vídeo | COMBO | Sim | `"chat"`<br>`"dance"`<br>`"hug"`<br>`"kill"`<br>`"kiss"`<br>`"pat"`<br>`"punch"`<br>`"shrug"`<br>`"slap"`<br>`"tickle"` |
| `model_name` | O modelo a ser usado para os efeitos dos personagens (padrão: "kling-v1") | COMBO | Não | `"kling-v1"`<br>`"kling-v1-5"`<br>`"kling-v1-6"` |
| `mode` | O modo de geração do vídeo (padrão: "std") | COMBO | Não | `"std"`<br>`"pro"` |
| `duration` | A duração do vídeo gerado em segundos | COMBO | Sim | `"5"`<br>`"10"` |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `output` | O vídeo gerado com efeitos de dois personagens | VIDEO |
| `duration` | As informações de duração do vídeo gerado | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingDualCharacterVideoEffectNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `4ee0c3cd834e1c70e41b40b66ac98d15a8b88993e7dc9d9df9fb4fadb868f079`

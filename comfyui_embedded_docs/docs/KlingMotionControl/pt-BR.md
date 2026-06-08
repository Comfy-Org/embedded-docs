O nó Kling Motion Control gera um vídeo aplicando os movimentos, expressões e movimentos de câmera de um vídeo de referência a um personagem definido por uma imagem de referência e um prompt de texto. Ele permite controlar se a orientação final do personagem vem do vídeo de referência ou da imagem de referência.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `prompt` | Uma descrição textual do vídeo desejado. O comprimento máximo é de 2500 caracteres. | STRING | Sim | N/A |
| `imagem_de_referência` | Uma imagem do personagem a ser animado. As dimensões mínimas são 340x340 pixels. A proporção deve estar entre 1:2,5 e 2,5:1. | IMAGE | Sim | N/A |
| `vídeo_de_referência` | Um vídeo de referência de movimento usado para orientar o movimento e a expressão do personagem. As dimensões mínimas são 340x340 pixels, as dimensões máximas são 3850x3850 pixels. Os limites de duração dependem da configuração `orientação_do_personagem`. | VIDEO | Sim | N/A |
| `manter_som_original` | Determina se o áudio original do vídeo de referência é mantido na saída. O padrão é `True`. | BOOLEAN | Não | N/A |
| `orientação_do_personagem` | Controla de onde vem a orientação/posição do personagem. `"video"`: movimentos, expressões, movimentos de câmera e orientação seguem o vídeo de referência de movimento (outros detalhes via prompt). `"image"`: movimentos e expressões ainda seguem o vídeo de referência de movimento, mas a orientação do personagem corresponde à imagem de referência (câmera/outros detalhes via prompt). | COMBO | Não | `"video"`<br>`"image"` |
| `modo` | O modo de geração a ser utilizado. | COMBO | Não | `"pro"`<br>`"std"` |
| `modelo` | A versão do modelo Kling a ser utilizada. O padrão é `"kling-v2-6"`. | COMBO | Não | `"kling-v3"`<br>`"kling-v2-6"` |

**Restrições:**

* A duração do `reference_video` deve estar entre 3 e 30 segundos quando `character_orientation` estiver definido como `"video"`.
* A duração do `reference_video` deve estar entre 3 e 10 segundos quando `character_orientation` estiver definido como `"image"`.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `output` | O vídeo gerado com o personagem executando o movimento do vídeo de referência. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingMotionControl/pt-BR.md)

---
**Source fingerprint (SHA-256):** `4159b10496e85ae93f522865494e9bc99ba08bda00df1601bca2314e61fb32df`

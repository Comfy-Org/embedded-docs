> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MagnificImageUpscalerCreativeNode/pt-BR.md)

Este nó utiliza o serviço de IA Magnific para aumentar a resolução e aprimorar criativamente uma imagem. Ele permite guiar o aprimoramento com um prompt de texto, escolher um estilo específico para otimização e controlar vários aspectos do processo criativo, como detalhe, semelhança com o original e força da estilização. O nó produz uma imagem com resolução aumentada no fator escolhido (2x, 4x, 8x ou 16x), com um tamanho máximo de saída de 25,3 megapixels.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `imagem` | IMAGE | Sim | - | A imagem de entrada a ser ampliada e aprimorada. |
| `prompt` | STRING | Não | - | Uma descrição textual para guiar o aprimoramento criativo da imagem. Este campo é opcional (padrão: vazio). |
| `fator de escala` | COMBO | Sim | `"2x"`<br>`"4x"`<br>`"8x"`<br>`"16x"` | O fator pelo qual as dimensões da imagem serão ampliadas. |
| `otimizado para` | COMBO | Sim | `"standard"`<br>`"soft_portraits"`<br>`"hard_portraits"`<br>`"art_n_illustration"`<br>`"videogame_assets"`<br>`"nature_n_landscapes"`<br>`"films_n_photography"`<br>`"3d_renders"`<br>`"science_fiction_n_horror"` | O estilo ou tipo de conteúdo para o qual o processo de aprimoramento será otimizado. |
| `criatividade` | INT | Não | -10 a 10 | Controla o nível de interpretação criativa aplicada à imagem (padrão: 0). |
| `hdr` | INT | Não | -10 a 10 | O nível de definição e detalhe (padrão: 0). |
| `semelhança` | INT | Não | -10 a 10 | O nível de semelhança com a imagem original (padrão: 0). |
| `fractalidade` | INT | Não | -10 a 10 | A força do prompt e o nível de detalhamento por pixel quadrado (padrão: 0). |
| `engine` | COMBO | Sim | `"automatic"`<br>`"magnific_illusio"`<br>`"magnific_sharpy"`<br>`"magnific_sparkle"` | O mecanismo de IA específico a ser usado para o processamento. Este é um parâmetro avançado. |
| `redução automática` | BOOLEAN | Não | - | Quando ativado, o nó reduzirá automaticamente a resolução da imagem de entrada se a ampliação solicitada exceder o tamanho máximo permitido de saída de 25,3 megapixels. Este é um parâmetro avançado (padrão: Falso). |

**Restrições:**

* A `image` de entrada deve ser exatamente uma imagem.
* A imagem de entrada deve ter altura e largura mínimas de 160 pixels.
* A proporção de aspecto da imagem de entrada deve estar entre 1:3 e 3:1.
* O tamanho final da saída (dimensões de entrada multiplicadas pelo `scale_factor`) não pode exceder 25.300.000 pixels. Se `auto_downscale` estiver desativado e esse limite for excedido, o nó gerará um erro.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `imagem` | IMAGE | A imagem de saída com resolução aumentada e aprimorada criativamente. |

---
**Source fingerprint (SHA-256):** `f5f046347c2992a2589153e803de14fc23b27187864b45eb566556418ebc161c`

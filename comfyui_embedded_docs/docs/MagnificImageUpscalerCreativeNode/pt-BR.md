# Magnific Image Upscale (Criativo)

Este nó usa o serviço Magnific AI para ampliar e aprimorar criativamente uma imagem. Ele permite orientar o aprimoramento com um prompt de texto, escolher um estilo específico para otimização e controlar vários aspectos do processo criativo, como detalhe, semelhança com o original e intensidade de estilização. O nó gera uma imagem ampliada no fator escolhido (2x, 4x, 8x ou 16x), com tamanho máximo de saída de 25,3 megapixels.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `image` | A imagem de entrada a ser ampliada e aprimorada. | IMAGE | Sim | - |
| `prompt` | Uma descrição textual para orientar o aprimoramento criativo da imagem. O padrão é uma string vazia (nesse caso, nenhum prompt é enviado). | STRING | Sim | - |
| `scale_factor` | O fator pelo qual as dimensões da imagem serão ampliadas. | COMBO | Sim | `"2x"`<br>`"4x"`<br>`"8x"`<br>`"16x"` |
| `optimized_for` | O estilo ou tipo de conteúdo para o qual otimizar o processo de aprimoramento. | COMBO | Sim | `"standard"`<br>`"soft_portraits"`<br>`"hard_portraits"`<br>`"art_n_illustration"`<br>`"videogame_assets"`<br>`"nature_n_landscapes"`<br>`"films_n_photography"`<br>`"3d_renders"`<br>`"science_fiction_n_horror"` |
| `creativity` | Controla o nível de interpretação criativa aplicada à imagem (padrão: 0). | INT | Sim | -10 a 10 |
| `hdr` | O nível de definição e detalhe (padrão: 0). | INT | Sim | -10 a 10 |
| `resemblance` | O nível de semelhança com a imagem original (padrão: 0). | INT | Sim | -10 a 10 |
| `fractality` | A força do prompt e a complexidade por pixel quadrado (padrão: 0). | INT | Sim | -10 a 10 |
| `engine` | O mecanismo de IA específico a ser usado para o processamento. Este é um parâmetro avançado. | COMBO | Sim | `"automatic"`<br>`"magnific_illusio"`<br>`"magnific_sharpy"`<br>`"magnific_sparkle"` |
| `auto_downscale` | Reduz automaticamente a escala da imagem de entrada se a saída exceder o limite máximo de pixels (padrão: False). Este é um parâmetro avançado. | BOOLEAN | Sim | - |

**Restrições:**

* A entrada `image` deve ser exatamente uma imagem.
* A imagem de entrada deve ter altura e largura mínimas de 160 pixels.
* A proporção da imagem de entrada deve estar entre 1:3 e 3:1.
* O tamanho final da saída (dimensões de entrada multiplicadas pelo `scale_factor`) não pode exceder 25.300.000 pixels. Se este limite for excedido:
  - Quando `auto_downscale` estiver habilitado, o nó reduz automaticamente o tamanho da imagem de entrada (a redução adicional é mantida em no máximo 2x) ou usa um `scale_factor` menor para que a saída permaneça dentro do limite.
  - Quando `auto_downscale` estiver desabilitado, o nó gera um erro.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `image` | A imagem de saída ampliada e aprimorada criativamente. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MagnificImageUpscalerCreativeNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `36c38e87f9f1e568c78cf794aeb0a268c6d25d639006eb2cf18ee040d3071ad4`

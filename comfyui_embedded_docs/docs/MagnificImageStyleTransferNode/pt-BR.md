Este nó aplica o estilo visual de uma imagem de referência à sua imagem de entrada. Ele utiliza um serviço de IA externo para processar as imagens, permitindo que você controle a intensidade da transferência de estilo e a preservação da estrutura da imagem original.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `image` | A imagem na qual aplicar a transferência de estilo. | IMAGE | Sim | - |
| `reference_image` | A imagem de referência para extrair o estilo. | IMAGE | Sim | - |
| `prompt` | Um prompt de texto opcional para guiar a transferência de estilo. | STRING | Não | - |
| `style_strength` | Porcentagem da intensidade do estilo (padrão: 100). | INT | Não | 0 a 100 |
| `structure_strength` | Mantém a estrutura da imagem original (padrão: 50). | INT | Não | 0 a 100 |
| `flavor` | Sabor da transferência de estilo. | COMBO | Não | "faithful"<br>"gen_z"<br>"psychedelia"<br>"detaily"<br>"clear"<br>"donotstyle"<br>"donotstyle_sharp" |
| `engine` | Seleção do mecanismo de processamento. | COMBO | Não | "balanced"<br>"definio"<br>"illusio"<br>"3d_cartoon"<br>"colorful_anime"<br>"caricature"<br>"real"<br>"super_real"<br>"softy" |
| `portrait_mode` | Ativa o modo retrato para aprimoramentos faciais. | COMBO | Não | "disabled"<br>"enabled" |
| `portrait_style` | Estilo visual aplicado a imagens de retrato. Esta entrada está disponível apenas quando `portrait_mode` está definido como "enabled". | COMBO | Não | "standard"<br>"pop"<br>"super_pop" |
| `portrait_beautifier` | Intensidade do embelezamento facial em retratos. Esta entrada está disponível apenas quando `portrait_mode` está definido como "enabled". | COMBO | Não | "none"<br>"beautify_face"<br>"beautify_face_max" |
| `fixed_generation` | Quando desativado, cada geração introduz um grau de aleatoriedade, resultando em resultados mais diversos (padrão: True). | BOOLEAN | Não | - |

**Restrições:**

* Exatamente uma `image` e uma `reference_image` são obrigatórias.
* Ambas as imagens devem ter uma proporção de aspecto entre 1:3 e 3:1.
* Ambas as imagens devem ter altura e largura mínimas de 160 pixels.
* Os parâmetros `portrait_style` e `portrait_beautifier` estão ativos e são obrigatórios apenas quando `portrait_mode` está definido como "enabled".

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `image` | A imagem resultante após a aplicação da transferência de estilo. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MagnificImageStyleTransferNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `4ae400183618953c369d089d39b878f0a24592967c29d779c577fb8b7339dea8`

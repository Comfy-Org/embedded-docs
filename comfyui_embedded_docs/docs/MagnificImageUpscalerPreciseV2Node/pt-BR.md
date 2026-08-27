# Magnific Image Upscale (Preciso V2)

O nó The Magnific Image Upscale (Precise V2) realiza o aumento de escala de imagem de alta fidelidade com controle fino sobre nitidez, granulação e aprimoramento de detalhes. Ele processa imagens por meio de uma API externa, suportando até uma resolução máxima de saída de 10060×10060 pixels. O nó oferece diferentes estilos de processamento e pode reduzir automaticamente a escala da entrada se a saída solicitada exceder o tamanho máximo permitido.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `imagem` | A imagem de entrada a ser ampliada. Exatamente uma imagem é obrigatória. As dimensões mínimas são 160x160 pixels. A proporção de aspecto deve estar entre 1:3 e 3:1. | IMAGE | Sim | - |
| `fator de escala` | O multiplicador de aumento de escala desejado. | COMBO | Sim | `"2x"`<br>`"4x"`<br>`"8x"`<br>`"16x"` |
| `estilo` | Estilo de processamento: sublime para uso geral, photo para fotografias, photo_denoiser para fotos com ruído. | COMBO | Sim | `"sublime"`<br>`"photo"`<br>`"photo_denoiser"` |
| `nitidez` | Intensidade da nitidez da imagem. Valores mais altos aumentam a definição das bordas e a clareza. Padrão: 7. | INT | Não | 0 a 100 |
| `granulação inteligente` | Aprimoramento inteligente de granulação/textura para evitar que a imagem pareça lisa demais ou artificial. Padrão: 7. | INT | Não | 0 a 100 |
| `ultra detalhe` | Controla detalhes finos, texturas e microdetalhes adicionados durante o aumento de escala. Padrão: 30. | INT | Não | 0 a 100 |
| `redução automática` | Reduzir automaticamente a escala da imagem de entrada se a saída exceder a resolução máxima. Padrão: False. | BOOLEAN | Não | - |

**Observação:** Se `auto_downscale` estiver desativado e o tamanho de saída solicitado (dimensões da entrada × `scale_factor`) exceder 10060x10060 pixels, o nó gerará um erro. Quando `auto_downscale` estiver ativado, o nó tentará encontrar um fator de escala ideal que mantenha a perda de qualidade mínima.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `image` | A imagem resultante após o aumento de escala. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MagnificImageUpscalerPreciseV2Node/pt-BR.md)

---
**Source fingerprint (SHA-256):** `aeb2b3569fd7b1d2417890586b8ac84ff921c4405f63f190188af93044ccfd28`

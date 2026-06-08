O nó **Magnific Image Upscale (Precise V2)** realiza a ampliação de imagens com alta fidelidade, oferecendo controle preciso sobre nitidez, granulação e realce de detalhes. Ele processa imagens por meio de uma API externa, suportando uma resolução máxima de saída de até 10060×10060 pixels. O nó oferece diferentes estilos de processamento e pode reduzir automaticamente a escala da imagem de entrada caso a saída solicitada exceda o tamanho máximo permitido.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `imagem` | A imagem de entrada a ser ampliada. Exatamente uma imagem é necessária. As dimensões mínimas são 160x160 pixels. A proporção deve estar entre 1:3 e 3:1. | IMAGE | Sim | - |
| `fator de escala` | O multiplicador de ampliação desejado. | STRING | Sim | `"2x"`<br>`"4x"`<br>`"8x"`<br>`"16x"` |
| `estilo` | O estilo de processamento. "sublime" é para uso geral, "photo" é otimizado para fotografias e "photo_denoiser" é para fotos com ruído. | STRING | Sim | `"sublime"`<br>`"photo"`<br>`"photo_denoiser"` |
| `nitidez` | Controla a intensidade da nitidez da imagem para aumentar a definição e clareza das bordas. Valores mais altos produzem um resultado mais nítido. Padrão: 7. | INT | Não | 0 a 100 |
| `granulação inteligente` | Adiciona granulação inteligente ou realce de textura para evitar que a imagem ampliada pareça muito suave ou artificial. Padrão: 7. | INT | Não | 0 a 100 |
| `ultra detalhe` | Controla a quantidade de detalhes finos, texturas e microdetalhes adicionados durante o processo de ampliação. Padrão: 30. | INT | Não | 0 a 100 |
| `redução automática` | Quando ativado, o nó reduzirá automaticamente a escala da imagem de entrada se as dimensões de saída calculadas excederem a resolução máxima permitida de 10060x10060 pixels. Isso ajuda a evitar erros, mas pode afetar a qualidade. Padrão: Falso. | BOOLEAN | Não | - |

**Observação:** Se `auto_downscale` estiver desativado e o tamanho de saída solicitado (dimensões de entrada × `scale_factor`) exceder 10060x10060 pixels, o nó gerará um erro.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `imagem` | A imagem ampliada resultante. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MagnificImageUpscalerPreciseV2Node/pt-BR.md)

---
**Source fingerprint (SHA-256):** `cceff30e9702c6a24ab8102698c59f1afb20ec50e7f279b3c0d50befc9673b24`

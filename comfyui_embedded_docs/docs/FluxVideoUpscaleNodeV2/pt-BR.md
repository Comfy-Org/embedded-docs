# Flux Video Upscale

Flux Video Upscale amplia um vídeo com super-resolução FLUX, seja para um tamanho de quadro fixo de 1080p, 2K ou 4K, seja por 1,5 a 3 vezes. O modo `"creative"` restaura e inventa detalhes finos, o que é adequado para imagens geradas; o modo `"precise"` realça a fonte sem alterá-la, o que é adequado para rostos, produtos e filmagens reais. O clipe é enviado, a tarefa BFL é consultada periodicamente e o vídeo finalizado retorna em 24 fps.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-----------|---------------|-------------|-----------|
| `video` | Clipe de origem de 1 a 20 segundos, com pelo menos 64x64 pixels e proporção entre 1:4 e 4:1. A saída é renderizada em 24 fps e limitada a cerca de 14,4 megapixels por quadro. | VIDEO | Sim | duração de 1 a 20 segundos; proporção entre 1:4 e 4:1; mínimo de 64x64 pixels |
| `target_resolution` | Tamanho da saída. `"1080p"`, `"2K"` e `"4K"` ajustam o resultado para caber em 1920x1080, 2560x1440 ou 3840x2160 pixels, com orientação ajustada para clipes verticais; `"by factor"` usa `upscale_factor` em vez disso. | DYNAMIC_COMBO | Sim | `"2K"`<br>`"4K"`<br>`"1080p"`<br>`"by factor"` |
| `mode` | `"creative"` restaura e inventa detalhes finos, ideal para imagens geradas, texturas e cenários. `"precise"` realça a fonte sem alterá-la, para rostos, produtos e filmagens reais. (padrão: `"creative"`) | COMBO | Sim | `"creative"`<br>`"precise"` |
| `prompt` | Descrição opcional do clipe que orienta o detalhe aprimorado. Deixe vazio para uma ampliação neutra. (padrão: vazio) | STRING | Sim | Texto multilinha |
| `auto_downscale` | Reduz a escala de fontes grandes demais em vez de rejeitá-las: acima de 2560x1440 pixels de área, ou acima de dois terços da resolução de destino. A proporção é preservada. (padrão: true) | BOOLEAN | Sim | true<br>false |
| `safety_tolerance` | Tolerância de moderação; 0 é o mais restritivo. (padrão: 2, parâmetro avançado) | INT | Sim | 0 a 4 |
| `seed` | A seed controla se o nó deve ser executado novamente; o FLUX escolhe a própria seed, então os resultados reais são não determinísticos independentemente deste valor. (padrão: 42) | INT | Sim | 0 a 4294967295 |

### Entradas de by factor

Essas entradas aparecem quando `target_resolution` é definido como `"by factor"`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-----------|---------------|-------------|-----------|
| `upscale_factor` | Tamanho da saída em relação à fonte. Fontes muito grandes são ampliadas por um fator menor que o solicitado devido ao limite por quadro. (padrão: 2.0) | FLOAT | Sim | 1.5 a 3.0 (passo 0.1) |

Um tamanho de destino é aplicado como um fator de ampliação limitado a 1.5-3.0, então uma fonte pequena demais para preencher a caixa em 3x resulta menor que a resolução solicitada, e uma fonte que precisaria de menos de 1.5x para caber na caixa é reduzida primeiro. Com `auto_downscale` desativado, o nó para com um erro em vez de reduzir a escala. A saída é em 24 fps e limitada a cerca de 14,4 megapixels por quadro, então fontes muito grandes podem ser ampliadas por um fator menor que o solicitado.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|---------------|-----------|---------------|
| `video` | O clipe de vídeo ampliado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxVideoUpscaleNodeV2/pt-BR.md)

---
**Source fingerprint (SHA-256):** `bef6ef4614d75bc9e6bab977f5f19c45fe30d300907913462a058e6e7e7e4ac7`

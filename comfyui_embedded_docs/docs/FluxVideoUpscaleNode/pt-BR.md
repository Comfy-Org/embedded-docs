# Ampliação de Vídeo Flux

O Flux Video Upscale aumenta a escala de um clipe de vídeo em 1,5 a 3 vezes usando super-resolução FLUX. No modo creative, ele restaura e inventa detalhes finos; no modo precise, ele aumenta a nitidez da fonte sem alterá-la.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-----------|---------------|-------------|-----------|
| `video` | Clipe de origem de 1 a 20 segundos com proporção de aspecto entre 1:4 e 4:1. A saída é renderizada a 24 fps e limitada a cerca de 14,4 megapixels por quadro. | VIDEO | Sim | duração de 1 a 20 segundos; proporção de aspecto entre 1:4 e 4:1; mínimo de 64x64 pixels |
| `upscale_factor` | Tamanho da saída em relação à fonte. Fontes muito grandes são ampliadas por um fator menor que o solicitado devido ao limite por quadro. (padrão: 2.0) | FLOAT | Sim | 1.5 a 3.0 (passo 0.1) |
| `mode` | 'creative' restaura e inventa detalhes finos, melhor para gravações geradas, texturas e cenários. 'precise' aumenta a nitidez da fonte sem alterá-la, para rostos, produtos e gravações reais. (padrão: "creative") | COMBO | Sim | "creative"<br>"precise" |
| `prompt` | Descrição opcional do clipe que orienta o detalhamento aprimorado. Deixe vazio para um upscale neutro. (padrão: vazio) | STRING | Sim | Texto multilinha |
| `auto_downscale` | Reduz automaticamente a escala de fontes maiores que 3840x2160 pixels de área para se adequarem ao limite de entrada. A proporção de aspecto é preservada; vídeos menores não são alterados. (padrão: true) | BOOLEAN | Sim | true<br>false |
| `safety_tolerance` | Tolerância de moderação; 0 é o mais restritivo. (padrão: 2, parâmetro avançado) | INT | Sim | 0 a 4 |
| `seed` | Semente para determinar se o nó deve ser executado novamente; o FLUX escolhe sua própria semente, então os resultados efetivos são não determinísticos independentemente deste valor. (padrão: 42) | INT | Sim | 0 a 4294967295 |

Observação: O vídeo de origem deve ter entre 1 e 20 segundos de duração, pelo menos 64x64 pixels de tamanho e uma proporção de aspecto entre 1:4 e 4:1. Se `auto_downscale` estiver desativado e a área do vídeo exceder 3840x2160 pixels, o nó gera um erro. O vídeo de saída é renderizado a 24 fps e limitado a cerca de 14,4 megapixels por quadro, portanto fontes muito grandes podem ser ampliadas por um fator menor que o solicitado.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|---------------|-----------|---------------|
| `video` | O clipe de vídeo com resolução aumentada. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxVideoUpscaleNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `22dcf7c176705ce21a9032b1c9f4fe82ee6aa153f5057b90dac653b37281a677`

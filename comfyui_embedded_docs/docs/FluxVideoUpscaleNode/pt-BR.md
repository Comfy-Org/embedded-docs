# FluxVideoUpscaleNode

Flux Video Upscale amplia um clipe de vídeo em 1,5 a 3 vezes usando super-resolução FLUX. No modo criativo, ele restaura e inventa detalhes finos; no modo preciso, ele nitidiza a origem sem alterá-la.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `video` | Clipe de origem de 1 a 20 segundos com proporção de aspecto entre 1:4 e 4:1. A saída é renderizada a 24 fps e limitada a cerca de 14,4 megapixels por quadro. | VIDEO | Sim | duração de 1 a 20 segundos; proporção de aspecto entre 1:4 e 4:1; mínimo de 64x64 pixels |
| `upscale_factor` | Tamanho da saída em relação à origem. Origens muito grandes são ampliadas por um fator menor que o solicitado devido ao limite por quadro. (padrão: 2,0) | FLOAT | Sim | 1,5 a 3,0 (passo 0,1) |
| `mode` | 'creative' restaura e inventa detalhes finos, ideal para gravações geradas, texturas e paisagens. 'precise' nitidiza a origem sem alterá-la, para rostos, produtos e gravações reais. (padrão: "creative") | COMBO | Sim | "creative"<br>"precise" |
| `prompt` | Descrição opcional do clipe que orienta o detalhe aprimorado. Deixe vazio para uma ampliação neutra. (padrão: vazio) | STRING | Sim | Texto multilinha |
| `auto_downscale` | Redimensiona automaticamente origens maiores que 3840x2160 pixels em área para caber no limite de entrada. A proporção de aspecto é preservada; vídeos menores não são alterados. (padrão: true) | BOOLEAN | Sim | true<br>false |
| `safety_tolerance` | Tolerância de moderação, 0 é o mais estrito. (padrão: 2, parâmetro avançado) | INT | Sim | 0 a 4 |
| `seed` | Semente para determinar se o nó deve ser executado novamente; o FLUX escolhe sua própria semente, portanto os resultados reais são não determinísticos independentemente desse valor. (padrão: 42) | INT | Sim | 0 a 4294967295 |

Nota: O vídeo de origem deve ter entre 1 e 20 segundos de duração e pelo menos 64x64 pixels de tamanho. Se `auto_downscale` estiver desativado e a área do vídeo exceder 3840x2160 pixels, o nó gerará um erro. O vídeo de saída é renderizado a 24 fps e limitado a cerca de 14,4 megapixels por quadro, portanto origens muito grandes podem ser ampliadas por um fator menor que o solicitado.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `video` | O clipe de vídeo ampliado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxVideoUpscaleNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `22dcf7c176705ce21a9032b1c9f4fe82ee6aa153f5057b90dac653b37281a677`

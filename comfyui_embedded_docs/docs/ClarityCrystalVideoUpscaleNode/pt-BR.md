# Clarity AI Crystal Video Upscale

Amplie um vídeo com o Crystal Video Upscaler da Clarity AI, um upscaler de alta fidelidade que se mantém fiel à fonte. O clipe é enviado, ampliado pelo fator definido e retornado como vídeo. A saída é limitada a 9 megapixels por quadro (por exemplo, 4000x2250) e a 360 megapixel-segundos por clipe, então clipes grandes ou longos retornam com resolução menor do que o fator solicita.

Selecionar um `model` revela os parâmetros específicos desse modelo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | Modelo a usar. Selecionar um modelo revela os parâmetros específicos dele: `video` e `scale_factor`. | DYNAMIC_COMBO | Sim | `"crystal-video-upscaler"` |
| `video` | O vídeo a ser ampliado. | VIDEO | Sim | N/A |
| `scale_factor` | Fator pelo qual multiplicar a largura e a altura do vídeo. A saída é limitada a 9 megapixels por quadro e a 360 megapixel-segundos por clipe, de modo que vídeos grandes ou longos são ampliados por um fator menor, e o fator é reduzido novamente quando faria um lado ultrapassar 5120 pixels (padrão: 2.0). | FLOAT | Sim | 1.0 a 200.0 (passo 0.1) |

**Observação:** O clipe pode ter no máximo 5120 pixels em cada lado e no máximo 9 megapixels por quadro. O comprimento máximo depende do tamanho do quadro e da taxa de quadros: é 360 megapixel-segundos dividido pelos pixels do quadro e pela taxa de quadros arredondada para cima para um múltiplo de 30 fps, então um clipe 1080p a 30 fps pode durar até cerca de 173 segundos. Clipes acima de 30 fps custam 2x, acima de 60 fps custam 3x, e assim por diante.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `video` | O vídeo ampliado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClarityCrystalVideoUpscaleNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `ca44ed6591474421edaf7e4e99e6da62e0c2e4e66964b7dac51d45758150aaa8`

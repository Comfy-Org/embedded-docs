# Stability AI Stable Image Ultra

Gera imagens de forma síncrona com base no prompt e na resolução. Este nó cria imagens usando o modelo Stable Image Ultra da Stability AI, processando seu prompt de texto e gerando uma imagem correspondente com a proporção e o estilo especificados.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `prompt` | O que você deseja ver na imagem de saída. Um prompt forte e descritivo que defina claramente elementos, cores e assuntos levará a melhores resultados. Para controlar o peso de uma palavra específica, use o formato `(palavra:peso)`, onde `palavra` é o termo que você deseja controlar e `peso` é um valor entre 0 e 1. Por exemplo: `O céu estava azul (azul:0.3) e verde (verde:0.8)` transmitiria um céu que era azul e verde, mas mais verde do que azul. | STRING | Sim | - |
| `aspect_ratio` | Proporção da imagem gerada (padrão: "1:1"). | COMBO | Sim | `"1:1"`<br>`"16:9"`<br>`"21:9"`<br>`"2:3"`<br>`"3:2"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"9:21"` |
| `style_preset` | Estilo desejado opcional para a imagem gerada. Selecione "Nenhum" para não aplicar nenhum preset de estilo. | COMBO | Não | `"3d-model"`<br>`"analog-film"`<br>`"anime"`<br>`"cinematic"`<br>`"comic-book"`<br>`"digital-art"`<br>`"enhance"`<br>`"fantasy-art"`<br>`"isometric"`<br>`"line-art"`<br>`"low-poly"`<br>`"modeling-compound"`<br>`"neon-punk"`<br>`"origami"`<br>`"photographic"`<br>`"pixel-art"`<br>`"tile-texture"` |
| `seed` | A semente aleatória usada para criar o ruído. | INT | Sim | 0 - 4294967294 |
| `image` | Imagem de entrada opcional para geração imagem-para-imagem. | IMAGE | Não | - |
| `negative_prompt` | Um texto descrevendo o que você NÃO deseja ver na imagem de saída. Este é um recurso avançado. | STRING | Não | - |
| `image_denoise` | Redução de ruído da imagem de entrada; 0.0 produz uma imagem idêntica à entrada, 1.0 é como se nenhuma imagem tivesse sido fornecida (padrão: 0.5). | FLOAT | Não | 0.0 - 1.0 |

**Nota:** Quando uma imagem de entrada não é fornecida, o parâmetro `image_denoise` é automaticamente desabilitado e ignorado.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `output` | A imagem gerada com base nos parâmetros de entrada. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityStableImageUltraNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `2fd9e106a3460a39c33ecc9a15ab6414dab1914fdc43e4f546827e02c889cf62`

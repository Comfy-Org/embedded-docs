# VAE Decodificar (Em Blocos)

O nó VAEDecodeTiled decodifica representações latentes em imagens usando uma abordagem em tiles para processar grandes imagens com eficiência. Ele processa a entrada em tiles menores para gerenciar o uso de memória, mantendo a qualidade da imagem. O nó também suporta VAEs de vídeo ao processar quadros temporais em blocos com sobreposição para transições suaves.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `amostras` | A representação latente a ser decodificada em imagens | LATENT | Sim | - |
| `vae` | O modelo VAE usado para decodificar as amostras latentes | VAE | Sim | - |
| `tamanho_do_bloco` | O tamanho de cada tile para processamento (padrão: 512) | INT | Sim | 64-4096 (passo: 32) |
| `sobreposição` | A quantidade de sobreposição entre tiles adjacentes (padrão: 64) | INT | Sim | 0-4096 (passo: 32) |
| `tamanho_temporal` | Usado apenas para VAEs de vídeo: quantidade de quadros a decodificar por vez (padrão: 64) | INT | Sim | 8-4096 (passo: 4) |
| `sobreposição_temporal` | Usado apenas para VAEs de vídeo: quantidade de quadros a sobrepor (padrão: 8) | INT | Sim | 4-4096 (passo: 4) |

**Nota:** O nó ajusta automaticamente os valores de sobreposição se eles excederem os limites práticos. Se `tile_size` for menor que 4 vezes o `overlap`, a sobreposição é reduzida a um quarto do tamanho do tile. Da mesma forma, se `temporal_size` for menor que o dobro de `temporal_overlap`, a sobreposição temporal é reduzida pela metade. O nó também leva em conta as taxas de compressão internas do VAE ao calcular os tamanhos de tile e sobreposição para as dimensões espaciais e temporais. Se o latent de entrada for um lote aninhado de latentes, apenas o primeiro item do lote é decodificado.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `IMAGE` | A imagem ou imagens decodificadas geradas a partir da representação latente. Ao decodificar latents de vídeo, a saída é uma sequência de quadros de imagem. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeTiled/pt-BR.md)

---
**Source fingerprint (SHA-256):** `04136ba1abd0c74e780dc405f916a08b809630ae4f41c183049535488b40fd96`

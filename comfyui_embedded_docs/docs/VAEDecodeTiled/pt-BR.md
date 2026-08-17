# VAE Decodificar (Em Blocos)

O nó VAEDecodeTiled decodifica representações latentes em imagens usando uma abordagem em blocos para lidar com imagens grandes de forma eficiente. Ele processa a entrada em blocos menores para gerenciar o uso de memória, mantendo a qualidade da imagem. O nó também suporta VAEs de vídeo, processando quadros temporais em partes com sobreposição para transições suaves.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `samples` | A representação latente a ser decodificada em imagens | LATENT | Sim | - |
| `vae` | O modelo VAE usado para decodificar as amostras latentes | VAE | Sim | - |
| `tile_size` | O tamanho de cada bloco para processamento (padrão: 512) | INT | Sim | 64-4096 (passo: 32) |
| `overlap` | A quantidade de sobreposição entre blocos adjacentes (padrão: 64) | INT | Sim | 0-4096 (passo: 32) |
| `temporal_size` | Usado apenas para VAEs de vídeo: quantidade de quadros a decodificar por vez (padrão: 64) | INT | Sim | 8-4096 (passo: 4) |
| `temporal_overlap` | Usado apenas para VAEs de vídeo: quantidade de quadros a sobrepor (padrão: 8) | INT | Sim | 4-4096 (passo: 4) |

**Nota:** O nó ajusta automaticamente os valores de sobreposição se eles excederem os limites práticos. Se `tile_size` for menor que 4 vezes o `overlap`, a sobreposição é reduzida para um quarto do tamanho do bloco. Da mesma forma, se `temporal_size` for menor que duas vezes o `temporal_overlap`, a sobreposição temporal é reduzida à metade. O nó também leva em consideração as taxas de compressão internas do VAE ao calcular os tamanhos de bloco e sobreposição para as dimensões espaciais e temporais. Para VAEs sem compressão temporal (VAEs que não são de vídeo), os parâmetros `temporal_size` e `temporal_overlap` são ignorados.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `IMAGE` | A imagem ou as imagens decodificadas geradas a partir da representação latente. Ao decodificar latentes de vídeo, todos os quadros decodificados são combinados em uma única lista de imagens. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeTiled/pt-BR.md)

---
**Source fingerprint (SHA-256):** `04136ba1abd0c74e780dc405f916a08b809630ae4f41c183049535488b40fd96`

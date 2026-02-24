> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeTiled/pt-BR.md)

O nó VAEDecodeTiled decodifica representações latentes em imagens usando uma abordagem em blocos (tiles) para lidar com imagens grandes de forma eficiente. Ele processa a entrada em blocos menores para gerenciar o uso de memória, mantendo a qualidade da imagem. O nó também suporta VAEs de vídeo, processando quadros temporais em blocos com sobreposição para transições suaves.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `samples` | LATENT | Sim | - | A representação latente a ser decodificada em imagens |
| `vae` | VAE | Sim | - | O modelo VAE usado para decodificar as amostras latentes |
| `tile_size` | INT | Sim | 64-4096 (passo: 32) | O tamanho de cada bloco para processamento (padrão: 512) |
| `overlap` | INT | Sim | 0-4096 (passo: 32) | A quantidade de sobreposição entre blocos adjacentes (padrão: 64) |
| `temporal_size` | INT | Sim | 8-4096 (passo: 4) | Usado apenas para VAEs de vídeo: Quantidade de quadros para decodificar de cada vez (padrão: 64) |
| `temporal_overlap` | INT | Sim | 4-4096 (passo: 4) | Usado apenas para VAEs de vídeo: Quantidade de quadros para sobrepor (padrão: 8) |

**Observação:** O nó ajusta automaticamente os valores de sobreposição se eles excederem limites práticos. Se `tile_size` for menor que 4 vezes o `overlap`, a sobreposição é reduzida para um quarto do tamanho do bloco. Da mesma forma, se `temporal_size` for menor que o dobro do `temporal_overlap`, a sobreposição temporal é reduzida pela metade.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | A imagem ou imagens decodificadas geradas a partir da representação latente |

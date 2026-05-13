> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeTiled/pt-BR.md)

O nó VAEDecodeTiled decodifica representações latentes em imagens usando uma abordagem em blocos para processar imagens grandes de forma eficiente. Ele processa a entrada em blocos menores para gerenciar o uso de memória, mantendo a qualidade da imagem. O nó também suporta VAEs de vídeo, processando quadros temporais em partes com sobreposição para transições suaves.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `amostras` | LATENT | Sim | - | A representação latente a ser decodificada em imagens |
| `vae` | VAE | Sim | - | O modelo VAE usado para decodificar as amostras latentes |
| `tamanho_do_bloco` | INT | Sim | 64-4096 (passo: 32) | O tamanho de cada bloco para processamento (padrão: 512) |
| `sobreposição` | INT | Sim | 0-4096 (passo: 32) | A quantidade de sobreposição entre blocos adjacentes (padrão: 64) |
| `tamanho_temporal` | INT | Sim | 8-4096 (passo: 4) | Usado apenas para VAEs de vídeo: quantidade de quadros a decodificar por vez (padrão: 64) |
| `sobreposição_temporal` | INT | Sim | 4-4096 (passo: 4) | Usado apenas para VAEs de vídeo: quantidade de quadros a sobrepor (padrão: 8) |

**Nota:** O nó ajusta automaticamente os valores de sobreposição se eles excederem os limites práticos. Se `tile_size` for menor que 4 vezes o `overlap`, a sobreposição é reduzida para um quarto do tamanho do bloco. Da mesma forma, se `temporal_size` for menor que o dobro do `temporal_overlap`, a sobreposição temporal é reduzida pela metade. O nó também considera as taxas de compressão internas do VAE ao calcular os tamanhos dos blocos e sobreposições para as dimensões espaciais e temporais.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `IMAGE` | IMAGE | A imagem ou imagens decodificadas geradas a partir da representação latente |

---
**Source fingerprint (SHA-256):** `193d5cb219d66855ae581d3e4488b7b6ae3a45b735fb0f9f784fea1f5d466e46`

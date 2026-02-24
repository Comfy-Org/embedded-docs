> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEEncodeTiled/pt-BR.md)

O nó VAEEncodeTiled processa imagens dividindo-as em blocos menores (tiles) e codificando-os usando um Autoencoder Variacional. Essa abordagem em blocos permite o processamento de imagens grandes que, de outra forma, poderiam exceder as limitações de memória. O nó suporta tanto VAEs de imagem quanto de vídeo, com controles de blocagem separados para as dimensões espaciais e temporais.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `pixels` | IMAGE | Sim | - | Os dados da imagem de entrada a serem codificados |
| `vae` | VAE | Sim | - | O modelo de Autoencoder Variacional usado para a codificação |
| `tile_size` | INT | Sim | 64-4096 (passo: 64) | O tamanho de cada bloco para processamento espacial (padrão: 512) |
| `overlap` | INT | Sim | 0-4096 (passo: 32) | A quantidade de sobreposição entre blocos adjacentes (padrão: 64) |
| `temporal_size` | INT | Sim | 8-4096 (passo: 4) | Usado apenas para VAEs de vídeo: Quantidade de quadros a codificar por vez (padrão: 64) |
| `temporal_overlap` | INT | Sim | 4-4096 (passo: 4) | Usado apenas para VAEs de vídeo: Quantidade de quadros para sobreposição (padrão: 8) |

**Observação:** Os parâmetros `temporal_size` e `temporal_overlap` são relevantes apenas ao usar VAEs de vídeo e não têm efeito em VAEs de imagem padrão.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `LATENT` | LATENT | A representação latente codificada da imagem de entrada |

# VAE Codificar (Em Blocos)

O nó VAEEncodeTiled processa imagens dividindo-as em tiles menores e codificando-as usando um Autoencoder Variacional. Essa abordagem em tiles permite o processamento de imagens grandes que, de outra forma, poderiam exceder os limites de memória. O nó suporta VAEs de imagem e vídeo, com controles de tile separados para dimensões espaciais e temporais.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `pixels` | Os dados da imagem de entrada a serem codificados | IMAGE | Sim | - |
| `vae` | O modelo de Autoencoder Variacional usado para codificação | VAE | Sim | - |
| `tamanho_do_bloco` | O tamanho de cada tile para processamento espacial (padrão: 512) | INT | Sim | 64-4096 (passo: 64) |
| `sobreposição` | A quantidade de sobreposição entre tiles adjacentes (padrão: 64) | INT | Sim | 0-4096 (passo: 32) |
| `tamanho_temporal` | Usado apenas para VAEs de vídeo: Número de quadros para codificar por vez (padrão: 64) | INT | Sim | 8-4096 (passo: 4) |
| `sobreposição_temporal` | Usado apenas para VAEs de vídeo: Número de quadros para sobrepor (padrão: 8) | INT | Sim | 4-4096 (passo: 4) |

**Nota:** Os parâmetros `temporal_size` e `temporal_overlap` são relevantes apenas ao usar VAEs de vídeo e não têm efeito em VAEs de imagem padrão.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `LATENT` | A representação latente codificada da imagem de entrada | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEEncodeTiled/pt-BR.md)

---
**Source fingerprint (SHA-256):** `87420b96ef9b2d5ef18ecb0339a62b6955151e2a9d2c4390758048c00432939a`

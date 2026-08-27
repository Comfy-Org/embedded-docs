# VAE Codificar (Em Blocos)

VAEEncodeTiled processa imagens dividindo-as em tiles menores e codificando-as usando um Autoencoder Variacional. Essa abordagem em tiles permite lidar com imagens grandes que, de outra forma, poderiam exceder os limites de memória. O nó suporta VAEs de imagem e de vídeo, com controles de tile separados para as dimensões espacial e temporal.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `pixels` | Os dados da imagem de entrada a serem codificados | IMAGE | Sim | - |
| `vae` | O modelo Autoencoder Variacional usado para codificação | VAE | Sim | - |
| `tamanho_do_bloco` | O tamanho de cada tile para o processamento espacial (padrão: 512) | INT | Sim | 64-4096 (passo: 64) |
| `sobreposição` | A quantidade de sobreposição entre tiles adjacentes (padrão: 64) | INT | Sim | 0-4096 (passo: 32) |
| `tamanho_temporal` | Usado apenas para VAEs de vídeo: quantidade de quadros para codificar por vez (padrão: 64) | INT | Sim | 8-4096 (passo: 4) |
| `sobreposição_temporal` | Usado apenas para VAEs de vídeo: quantidade de quadros para sobrepor (padrão: 8) | INT | Sim | 4-4096 (passo: 4) |

**Nota:** Os parâmetros `temporal_size` e `temporal_overlap` são relevantes apenas ao usar VAEs de vídeo e não têm efeito sobre VAEs de imagem padrão.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `LATENT` | A representação latente codificada da imagem de entrada | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEEncodeTiled/pt-BR.md)

---
**Source fingerprint (SHA-256):** `c36b02f8eeed5c72f9efa2392e2013e89be7644c022d987d413d4da088dfbaad`

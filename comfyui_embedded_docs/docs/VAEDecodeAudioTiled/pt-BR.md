# VAE Decodificar Áudio (Em Blocos)

Este nó converte uma representação de áudio comprimida (amostras latentes) de volta em uma forma de onda de áudio usando um Autoencoder Variacional (VAE). Ele processa os dados em seções menores e sobrepostas (blocos) para gerenciar o uso de memória, tornando-o adequado para lidar com sequências de áudio mais longas.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `samples` | A representação latente comprimida do áudio a ser decodificado. | LATENT | Sim | N/A |
| `vae` | O modelo de Autoencoder Variacional usado para realizar a decodificação. | VAE | Sim | N/A |
| `tile_size` | O tamanho de cada bloco de processamento. O áudio é decodificado em seções desse comprimento para economizar memória (padrão: 512). | INT | Sim | 32 to 8192 |
| `overlap` | O número de amostras em que blocos adjacentes se sobrepõem. Isso ajuda a reduzir artefatos nos limites entre blocos (padrão: 64). | INT | Sim | 0 to 1024 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `output` | A forma de onda de áudio decodificada. | AUDIO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeAudioTiled/pt-BR.md)

---
**Source fingerprint (SHA-256):** `5ddedf218ba27ab9f463646c1e5288091172f2d7fae8f2980bb2b5e4d3dca89c`

Este nó converte uma representação de áudio comprimida (amostras latentes) de volta em uma forma de onda de áudio usando um Autoencoder Variacional (VAE). Ele processa os dados em seções menores e sobrepostas (tiles) para gerenciar o uso de memória, tornando-o adequado para lidar com sequências de áudio mais longas.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `amostras` | A representação latente comprimida do áudio a ser decodificado. | LATENT | Sim | N/A |
| `vae` | O modelo Autoencoder Variacional usado para realizar a decodificação. | VAE | Sim | N/A |
| `tamanho_do_bloco` | O tamanho de cada tile de processamento. O áudio é decodificado em seções deste comprimento para economizar memória (padrão: 512). | INT | Sim | 32 a 8192 |
| `sobreposição` | O número de amostras que tiles adjacentes se sobrepõem. Isso ajuda a reduzir artefatos nos limites entre tiles (padrão: 64). | INT | Sim | 0 a 1024 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `output` | A forma de onda de áudio decodificada. | AUDIO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeAudioTiled/pt-BR.md)

---
**Source fingerprint (SHA-256):** `d989f0cd0e4b4bf992d6860e27c25b8e814df52763c82909a61c58f418306352`

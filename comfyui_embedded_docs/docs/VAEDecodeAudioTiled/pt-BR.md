# VAE Decodificar Áudio (Em Blocos)

Este nó converte uma representação de áudio compactada (amostras latentes) de volta em uma forma de onda de áudio usando um Autoencoder Variacional (VAE). Ele processa os dados em seções menores e sobrepostas (blocos) para gerenciar o uso de memória, sendo adequado para lidar com sequências de áudio mais longas. O áudio decodificado também é normalizado para manter seu nível de volume consistente.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `amostras` | A representação latente compactada do áudio a ser decodificado. | LATENT | Sim | N/A |
| `vae` | O modelo Autoencoder Variacional usado para realizar a decodificação. | VAE | Sim | N/A |
| `tamanho_do_bloco` | O tamanho de cada bloco de processamento. O áudio é decodificado em seções desse comprimento para economizar memória (padrão: 512). | INT | Sim | 32 a 8192 |
| `sobreposição` | O número de amostras em que blocos adjacentes se sobrepõem. Isso ajuda a reduzir artefatos nas bordas entre blocos (padrão: 64). | INT | Sim | 0 a 1024 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `output` | A forma de onda de áudio decodificada, incluindo as informações de taxa de amostragem. | AUDIO |

A taxa de amostragem da saída é obtida da entrada `samples` quando esta contém uma taxa de amostragem; caso contrário, ela é lida do modelo VAE (padrão: 44100 Hz).

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeAudioTiled/pt-BR.md)

---
**Source fingerprint (SHA-256):** `5ddedf218ba27ab9f463646c1e5288091172f2d7fae8f2980bb2b5e4d3dca89c`

Este nó gera um tensor latente vazio projetado para processamento de áudio. Ele cria um áudio latente silencioso com duração e tamanho de lote especificados, que pode ser usado como ponto de partida para fluxos de trabalho de geração de áudio no ComfyUI. O nó calcula o comprimento latente com base nos segundos informados e em uma taxa de amostragem fixa.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `seconds` | A duração do áudio a ser gerado, em segundos (padrão: 120.0). | FLOAT | Sim | 1.0 - 1000.0 |
| `batch_size` | O número de imagens latentes no lote (padrão: 1). | INT | Sim | 1 - 4096 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `LATENT` | Um tensor latente vazio representando áudio silencioso, com um identificador de tipo "audio". | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyAceStep1.5LatentAudio/pt-BR.md)

---
**Source fingerprint (SHA-256):** `8d2b0b8ea110362d5e43a72a27df0ff2012a8577fbaa4fef2bd7905c9c64bd6a`

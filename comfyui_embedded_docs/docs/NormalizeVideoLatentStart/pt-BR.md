# Normalizar Início do Latent de Vídeo

Este nó ajusta os primeiros frames de um latent de vídeo para que se pareçam mais com os frames que vêm depois. Ele calcula a média e a variação de um conjunto de frames de referência mais adiante no vídeo e aplica essas mesmas características aos frames iniciais. Isso ajuda a reduzir diferenças entre os frames iniciais e o restante do vídeo, criando uma transição mais suave e consistente.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `latent` | A representação latente de vídeo a ser processada. | LATENT | Sim | - |
| `start_frame_count` | Número de frames latentes a normalizar, contados a partir do início (padrão: 4). | INT | Sim | 1 a 16384 (resolução máxima) |
| `reference_frame_count` | Número de frames latentes após os frames iniciais a serem usados como referência (padrão: 5). | INT | Sim | 1 a 16384 (resolução máxima) |

**Nota:** Os frames de referência são obtidos imediatamente após os frames definidos por `start_frame_count`. Se houver menos frames disponíveis do que os solicitados por `reference_frame_count`, o nó usa quantos estiverem disponíveis (no máximo um a menos que a contagem total de frames do latent). Se o latent de vídeo tiver apenas 1 frame, nenhuma normalização será realizada e o latent original será retornado sem alterações.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `latent` | O latent de vídeo processado com os frames iniciais normalizados. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/NormalizeVideoLatentStart/pt-BR.md)

---
**Source fingerprint (SHA-256):** `383e5a19ee4cd8bdea5983567ddbdc30bb09c373142a1a934cea985f1b9d1b0d`

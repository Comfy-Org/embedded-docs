# Normalizar Início do Latent de Vídeo

Este nó ajusta os primeiros quadros de um latente de vídeo para que eles se pareçam mais com os quadros que vêm depois. Ele calcula a média e a variação a partir de um conjunto de quadros de referência posteriores no vídeo e aplica essas mesmas características aos quadros iniciais. Isso ajuda a criar uma transição visual mais suave e consistente no início de um vídeo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `latent` | A representação latente de vídeo a ser processada. | LATENT | Sim | - |
| `start_frame_count` | Número de quadros latentes a normalizar, contados a partir do início (padrão: 4). | INT | Sim | 1 a 16384 (resolução máxima) |
| `reference_frame_count` | Número de quadros latentes após os quadros iniciais a serem usados como referência (padrão: 5). | INT | Sim | 1 a 16384 (resolução máxima) |

**Observação:** O `reference_frame_count` é automaticamente limitado ao número de quadros disponíveis após os quadros iniciais. Se o latente de vídeo tiver apenas 1 quadro, nenhuma normalização é realizada e o latente original é retornado inalterado.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `latent` | O latente de vídeo processado com os quadros iniciais normalizados. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/NormalizeVideoLatentStart/pt-BR.md)

---
**Source fingerprint (SHA-256):** `383e5a19ee4cd8bdea5983567ddbdc30bb09c373142a1a934cea985f1b9d1b0d`

Este nó ajusta os primeiros quadros de um vídeo latente para que se assemelhem mais aos quadros subsequentes. Ele calcula a média e a variação de um conjunto de quadros de referência posteriores no vídeo e aplica essas mesmas características aos quadros iniciais. Isso ajuda a criar uma transição visual mais suave e consistente no início de um vídeo.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `latent` | A representação latente do vídeo a ser processada. | LATENT | Sim | - |
| `start_frame_count` | Número de quadros latentes a normalizar, contados a partir do início (padrão: 4). | INT | Sim | 1 a 16384 |
| `reference_frame_count` | Número de quadros latentes após os quadros iniciais a serem usados como referência (padrão: 5). | INT | Sim | 1 a 16384 |

**Observação:** O `reference_frame_count` é automaticamente limitado ao número de quadros disponíveis após os quadros iniciais. Se o vídeo latente tiver apenas 1 quadro, nenhuma normalização é realizada e o latente original é retornado inalterado.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `latent` | O vídeo latente processado com os quadros iniciais normalizados. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/NormalizeVideoLatentStart/pt-BR.md)

---
**Source fingerprint (SHA-256):** `64844f3bf1735952334dcca3a829e8f666fd89e817ab66cf3c2dc04ecbbdff56`

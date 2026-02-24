> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/NormalizeVideoLatentStart/pt-BR.md)

Este nó ajusta os primeiros quadros de um latente de vídeo para que se pareçam mais com os quadros subsequentes. Ele calcula a média e a variação a partir de um conjunto de quadros de referência mais adiante no vídeo e aplica essas mesmas características aos quadros iniciais. Isso ajuda a criar uma transição visual mais suave e consistente no início de um vídeo.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `latent` | LATENT | Sim | - | A representação latente do vídeo a ser processada. |
| `start_frame_count` | INT | Não | 1 a 16384 | Número de quadros latentes a normalizar, contados a partir do início (padrão: 4). |
| `reference_frame_count` | INT | Não | 1 a 16384 | Número de quadros latentes após os quadros iniciais a serem usados como referência (padrão: 5). |

**Observação:** O `reference_frame_count` é automaticamente limitado ao número de quadros disponíveis após os quadros iniciais. Se o latente de vídeo tiver apenas 1 quadro, nenhuma normalização é realizada e o latente original é retornado inalterado.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `latent` | LATENT | O latente de vídeo processado, com os quadros iniciais normalizados. |

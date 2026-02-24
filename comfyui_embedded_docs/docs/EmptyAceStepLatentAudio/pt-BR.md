> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyAceStepLatentAudio/pt-BR.md)

O nó EmptyAceStepLatentAudio cria amostras latentes de áudio vazias de uma duração especificada. Ele gera um lote de áudios latentes silenciosos com valores zero, onde o comprimento é calculado com base nos segundos de entrada e nos parâmetros de processamento de áudio. Este nó é útil para inicializar fluxos de trabalho de processamento de áudio que requerem representações latentes.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `seconds` | FLOAT | Não | 1.0 - 1000.0 | A duração do áudio em segundos (padrão: 120.0) |
| `batch_size` | INT | Não | 1 - 4096 | O número de imagens latentes no lote (padrão: 1) |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `output` | LATENT | Retorna amostras latentes de áudio vazias com valores zero |

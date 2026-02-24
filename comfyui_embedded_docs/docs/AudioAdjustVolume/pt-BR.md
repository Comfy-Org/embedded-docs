> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioAdjustVolume/pt-BR.md)

O nó AudioAdjustVolume modifica a intensidade sonora do áudio aplicando ajustes de volume em decibéis. Ele recebe uma entrada de áudio e aplica um fator de ganho baseado no nível de volume especificado, onde valores positivos aumentam o volume e valores negativos o diminuem. O nó retorna o áudio modificado com a mesma taxa de amostragem do original.

## Entradas

| Parâmetro | Tipo de Dados | Tipo de Entrada | Padrão | Intervalo | Descrição |
|-----------|-----------|------------|---------|-------|-------------|
| `audio` | AUDIO | obrigatório | - | - | A entrada de áudio a ser processada |
| `volume` | INT | obrigatório | 1.0 | -100 a 100 | Ajuste de volume em decibéis (dB). 0 = sem alteração, +6 = dobrar, -6 = reduzir pela metade, etc |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `audio` | AUDIO | O áudio processado com o nível de volume ajustado |

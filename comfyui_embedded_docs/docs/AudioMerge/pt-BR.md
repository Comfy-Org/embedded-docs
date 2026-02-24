> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioMerge/pt-BR.md)

O nó AudioMerge combina duas faixas de áudio sobrepondo suas formas de onda. Ele automaticamente iguala as taxas de amostragem de ambas as entradas de áudio e ajusta seus comprimentos para que sejam iguais antes da mesclagem. O nó oferece vários métodos matemáticos para combinar os sinais de áudio e garante que a saída permaneça dentro de níveis de volume aceitáveis.

## Entradas

| Parâmetro | Tipo de Dados | Tipo de Entrada | Padrão | Intervalo | Descrição |
|-----------|-----------|------------|---------|-------|-------------|
| `audio1` | AUDIO | obrigatória | - | - | Primeira entrada de áudio a ser mesclada |
| `audio2` | AUDIO | obrigatória | - | - | Segunda entrada de áudio a ser mesclada |
| `merge_method` | COMBO | obrigatória | - | ["add", "mean", "subtract", "multiply"] | O método usado para combinar as formas de onda de áudio. |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `AUDIO` | AUDIO | A saída de áudio mesclada contendo a forma de onda combinada e a taxa de amostragem |

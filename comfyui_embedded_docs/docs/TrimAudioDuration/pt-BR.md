> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TrimAudioDuration/pt-BR.md)

O nó TrimAudioDuration permite que você corte um segmento de tempo específico de um arquivo de áudio. Você pode especificar quando iniciar o corte e quanto tempo o clipe de áudio resultante deve ter. O nó funciona convertendo valores de tempo em posições de quadro de áudio e extraindo a porção correspondente da forma de onda de áudio.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `audio` | AUDIO | Sim | - | A entrada de áudio a ser cortada |
| `start_index` | FLOAT | Sim | -0xffffffffffffffff a 0xffffffffffffffff | Tempo de início em segundos, pode ser negativo para contar a partir do final (suporta subsegundos). Padrão: 0.0 |
| `duration` | FLOAT | Sim | 0.0 a 0xffffffffffffffff | Duração em segundos. Padrão: 60.0 |

**Observação:** O tempo de início deve ser menor que o tempo final e estar dentro do comprimento do áudio. Valores de início negativos contam para trás a partir do final do áudio.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `audio` | AUDIO | O segmento de áudio cortado com o tempo de início e a duração especificados |

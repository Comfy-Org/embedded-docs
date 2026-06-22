# Cortar Duração do Áudio

O nó TrimAudioDuration permite cortar um segmento de tempo específico de um arquivo de áudio. Você pode especificar quando iniciar o corte e por quanto tempo o clipe de áudio resultante deve durar. O nó funciona convertendo valores de tempo em posições de quadro de áudio e extraindo a porção correspondente da forma de onda do áudio.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `áudio` | A entrada de áudio a ser cortada | AUDIO | Sim | - |
| `índice_inicial` | Tempo inicial em segundos, pode ser negativo para contar a partir do final (suporta subsegundos). Padrão: 0.0 | FLOAT | Sim | -0xffffffffffffffff a 0xffffffffffffffff |
| `duração` | Duração em segundos. Padrão: 60.0 | FLOAT | Sim | 0.0 a 0xffffffffffffffff |

**Observação:** O tempo inicial deve ser menor que o tempo final e estar dentro da duração do áudio. Valores iniciais negativos contam regressivamente a partir do final do áudio. Se o tempo inicial for negativo, ele é convertido em uma posição de quadro contando a partir do final do áudio. Os quadros inicial e final são limitados aos limites do áudio.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `áudio` | O segmento de áudio cortado com o tempo inicial e duração especificados | AUDIO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TrimAudioDuration/pt-BR.md)

---
**Source fingerprint (SHA-256):** `695a9fe11fa086a317f94823e066688705e9f911cd6cfc5857596ff31dd539ed`

# GenerateTracks

O nó `GenerateTracks` cria múltiplos caminhos de movimento paralelos (trilhas) para geração de vídeo. Ele define um caminho principal de uma posição inicial até uma posição final e, em seguida, gera um conjunto de trilhas paralelas a esse caminho, espaçadas uniformemente. Você pode controlar a forma do caminho (linha reta ou curva Bezier), a velocidade do movimento ao longo dele e em quais quadros as trilhas ficam visíveis.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `largura` | A largura do quadro de vídeo em pixels. O valor padrão é 832. | INT | Sim | 16 - 4096 |
| `altura` | A altura do quadro de vídeo em pixels. O valor padrão é 480. | INT | Sim | 16 - 4096 |
| `início_x` | Coordenada X normalizada (0-1) para a posição inicial. O valor padrão é 0.0. | FLOAT | Sim | 0.0 - 1.0 |
| `início_y` | Coordenada Y normalizada (0-1) para a posição inicial. O valor padrão é 0.0. | FLOAT | Sim | 0.0 - 1.0 |
| `fim_x` | Coordenada X normalizada (0-1) para a posição final. O valor padrão é 1.0. | FLOAT | Sim | 0.0 - 1.0 |
| `fim_y` | Coordenada Y normalizada (0-1) para a posição final. O valor padrão é 1.0. | FLOAT | Sim | 0.0 - 1.0 |
| `número_de_quadros` | O número total de quadros para os quais gerar posições de trilhas. O valor padrão é 81. | INT | Sim | 1 - 1024 |
| `número_de_trilhas` | O número de trilhas paralelas a gerar. O valor padrão é 5. | INT | Sim | 1 - 100 |
| `dispersão_de_trilhas` | Distância normalizada entre trilhas. As trilhas são distribuídas perpendicularmente à direção do movimento. O valor padrão é 0.025. | FLOAT | Sim | 0.0 - 1.0 |
| `bezier` | Ativa o caminho de curva Bezier usando o ponto médio como ponto de controle. O valor padrão é False. | BOOLEAN | Sim | True / False |
| `meio_x` | Ponto de controle X normalizado para a curva Bezier. Usado somente quando 'bezier' está ativado. O valor padrão é 0.5. | FLOAT | Sim | 0.0 - 1.0 |
| `meio_y` | Ponto de controle Y normalizado para a curva Bezier. Usado somente quando 'bezier' está ativado. O valor padrão é 0.5. | FLOAT | Sim | 0.0 - 1.0 |
| `interpolação` | Controla o tempo/velocidade do movimento ao longo do caminho (padrão: "linear"):<br>"linear" - velocidade constante<br>"ease_in" - começa lento e acelera<br>"ease_out" - começa rápido e desacelera<br>"ease_in_out" - aceleração e desaceleração suaves<br>"constant" - mantém todas as posições no ponto inicial | COMBO | Sim | `"linear"`<br>`"ease_in"`<br>`"ease_out"`<br>`"ease_in_out"`<br>`"constant"` |
| `máscara_de_trilha` | Máscara opcional para indicar quadros visíveis. Se for fornecida, os quadros em que a máscara tiver qualquer pixel diferente de zero são marcados como visíveis para todas as trilhas. | MASK | Não | - |

**Nota:** Os parâmetros `mid_x` e `mid_y` são usados somente quando o parâmetro `bezier` está definido como `True`. Quando `bezier` é `False`, o caminho é uma linha reta do ponto inicial ao ponto final.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `TRACKS` | Um objeto TRACKS contendo as coordenadas do caminho gerado e as informações de visibilidade para todas as trilhas em todos os quadros. | TRACKS |
| `comprimento_da_trilha` | O número de quadros para os quais as trilhas foram geradas, correspondendo ao `num_frames` de entrada. | INT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GenerateTracks/pt-BR.md)

---
**Source fingerprint (SHA-256):** `4bd4d03a84f4b7ea260555b43f217af0b90dd4ca5196aca94e8f3886875ab912`

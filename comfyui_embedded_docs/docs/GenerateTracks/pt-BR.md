# GenerateTracks

O nó `GenerateTracks` cria múltiplas trajetórias de movimento paralelas para geração de vídeo. Ele define um caminho principal de um ponto inicial a um ponto final e, em seguida, gera um conjunto de trajetórias paralelas a esse caminho, espaçadas uniformemente. Você pode controlar a forma do caminho (linha reta ou curva de Bézier), a velocidade do movimento ao longo dele e em quais quadros as trajetórias ficam visíveis.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `width` | A largura do quadro de vídeo em pixels. O valor padrão é 832. | INT | Sim | 16 - 4096 |
| `height` | A altura do quadro de vídeo em pixels. O valor padrão é 480. | INT | Sim | 16 - 4096 |
| `start_x` | Coordenada X normalizada (0-1) para a posição inicial. O valor padrão é 0.0. | FLOAT | Sim | 0.0 - 1.0 |
| `start_y` | Coordenada Y normalizada (0-1) para a posição inicial. O valor padrão é 0.0. | FLOAT | Sim | 0.0 - 1.0 |
| `end_x` | Coordenada X normalizada (0-1) para a posição final. O valor padrão é 1.0. | FLOAT | Sim | 0.0 - 1.0 |
| `end_y` | Coordenada Y normalizada (0-1) para a posição final. O valor padrão é 1.0. | FLOAT | Sim | 0.0 - 1.0 |
| `num_frames` | O número total de quadros para os quais gerar as posições das trajetórias. O valor padrão é 81. | INT | Sim | 1 - 1024 |
| `num_tracks` | O número de trajetórias paralelas a serem geradas. O valor padrão é 5. | INT | Sim | 1 - 100 |
| `track_spread` | Distância normalizada entre as trajetórias. As trajetórias são distribuídas perpendicularmente à direção do movimento. O valor padrão é 0.025. | FLOAT | Sim | 0.0 - 1.0 |
| `bezier` | Ativa o caminho da curva de Bézier usando o ponto médio como ponto de controle. O valor padrão é False. | BOOLEAN | Sim | True / False |
| `mid_x` | Ponto de controle X normalizado para a curva de Bézier. Usado apenas quando `bezier` está ativado. O valor padrão é 0.5. | FLOAT | Sim | 0.0 - 1.0 |
| `mid_y` | Ponto de controle Y normalizado para a curva de Bézier. Usado apenas quando `bezier` está ativado. O valor padrão é 0.5. | FLOAT | Sim | 0.0 - 1.0 |
| `interpolation` | Controla o ritmo/velocidade do movimento ao longo do caminho. O valor padrão é "linear". Com "constant", todos os pontos permanecem na posição inicial. | COMBO | Sim | `"linear"`<br>`"ease_in"`<br>`"ease_out"`<br>`"ease_in_out"`<br>`"constant"` |
| `track_mask` | Máscara opcional para indicar quadros visíveis. | MASK | Não | - |

**Nota:** Os parâmetros `mid_x` e `mid_y` são usados apenas quando o parâmetro `bezier` está definido como `True`. Quando `bezier` é `False`, o caminho é uma linha reta do ponto inicial ao ponto final.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `TRACKS` | Um objeto do tipo `TRACKS` contendo as coordenadas do caminho gerado e as informações de visibilidade para todas as trajetórias em todos os quadros. | TRACKS |
| `track_length` | O número de quadros para os quais as trajetórias foram geradas, correspondendo ao `num_frames` de entrada. | INT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GenerateTracks/pt-BR.md)

---
**Source fingerprint (SHA-256):** `4bd4d03a84f4b7ea260555b43f217af0b90dd4ca5196aca94e8f3886875ab912`

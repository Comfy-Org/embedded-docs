> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GenerateTracks/pt-BR.md)

O nó `GenerateTracks` cria múltiplos caminhos de movimento paralelos para geração de vídeo. Ele define um caminho principal de um ponto inicial a um ponto final e, em seguida, gera um conjunto de trilhas paralelas a esse caminho, espaçadas uniformemente. Você pode controlar a forma do caminho (linha reta ou curva Bezier), a velocidade do movimento ao longo dele e em quais quadros as trilhas ficam visíveis.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|-----------|----------|-------|-------------|
| `width` | INT | Sim | 16 - 4096 | A largura do quadro de vídeo em pixels. O valor padrão é 832. |
| `height` | INT | Sim | 16 - 4096 | A altura do quadro de vídeo em pixels. O valor padrão é 480. |
| `start_x` | FLOAT | Sim | 0.0 - 1.0 | Coordenada X normalizada (0-1) para a posição inicial. O valor padrão é 0.0. |
| `start_y` | FLOAT | Sim | 0.0 - 1.0 | Coordenada Y normalizada (0-1) para a posição inicial. O valor padrão é 0.0. |
| `end_x` | FLOAT | Sim | 0.0 - 1.0 | Coordenada X normalizada (0-1) para a posição final. O valor padrão é 1.0. |
| `end_y` | FLOAT | Sim | 0.0 - 1.0 | Coordenada Y normalizada (0-1) para a posição final. O valor padrão é 1.0. |
| `num_frames` | INT | Sim | 1 - 1024 | O número total de quadros para os quais gerar posições de trilha. O valor padrão é 81. |
| `num_tracks` | INT | Sim | 1 - 100 | O número de trilhas paralelas a serem geradas. O valor padrão é 5. |
| `track_spread` | FLOAT | Sim | 0.0 - 1.0 | Distância normalizada entre as trilhas. As trilhas são distribuídas perpendicularmente à direção do movimento. O valor padrão é 0.025. |
| `bezier` | BOOLEAN | Sim | Verdadeiro / Falso | Ativa o caminho de curva Bezier usando o ponto médio como ponto de controle. O valor padrão é Falso. |
| `mid_x` | FLOAT | Sim | 0.0 - 1.0 | Ponto de controle X normalizado para a curva Bezier. Usado apenas quando 'bezier' está ativado. O valor padrão é 0.5. |
| `mid_y` | FLOAT | Sim | 0.0 - 1.0 | Ponto de controle Y normalizado para a curva Bezier. Usado apenas quando 'bezier' está ativado. O valor padrão é 0.5. |
| `interpolation` | COMBO | Sim | `"linear"`<br>`"ease_in"`<br>`"ease_out"`<br>`"ease_in_out"`<br>`"constant"` | Controla o tempo/velocidade do movimento ao longo do caminho. O valor padrão é "linear". |
| `track_mask` | MASK | Não | - | Máscara opcional para indicar quadros visíveis. |

**Nota:** Os parâmetros `mid_x` e `mid_y` são usados apenas quando o parâmetro `bezier` está definido como `True`. Quando `bezier` é `False`, o caminho é uma linha reta do ponto inicial ao ponto final.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `TRACKS` | TRACKS | Um objeto de trilhas contendo as coordenadas do caminho gerado e informações de visibilidade para todas as trilhas em todos os quadros. |
| `track_length` | INT | O número de quadros para os quais as trilhas foram geradas, correspondendo ao `num_frames` de entrada. |

---
**Source fingerprint (SHA-256):** `3dca1cabaee8738e2a68acafed47ad347019d03c9b7f0d1392b3fdf97d0e8add`

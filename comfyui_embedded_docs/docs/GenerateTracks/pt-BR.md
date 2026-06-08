O nó `GenerateTracks` cria múltiplos caminhos de movimento paralelos para geração de vídeo. Ele define um caminho principal de um ponto inicial a um ponto final e, em seguida, gera um conjunto de trilhas paralelas a esse caminho, espaçadas uniformemente. Você pode controlar a forma do caminho (linha reta ou curva Bezier), a velocidade do movimento ao longo dele e em quais quadros as trilhas ficam visíveis.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `largura` | A largura do quadro de vídeo em pixels. O valor padrão é 832. | INT | Sim | 16 - 4096 |
| `altura` | A altura do quadro de vídeo em pixels. O valor padrão é 480. | INT | Sim | 16 - 4096 |
| `início_x` | Coordenada X normalizada (0-1) para a posição inicial. O valor padrão é 0.0. | FLOAT | Sim | 0.0 - 1.0 |
| `início_y` | Coordenada Y normalizada (0-1) para a posição inicial. O valor padrão é 0.0. | FLOAT | Sim | 0.0 - 1.0 |
| `fim_x` | Coordenada X normalizada (0-1) para a posição final. O valor padrão é 1.0. | FLOAT | Sim | 0.0 - 1.0 |
| `fim_y` | Coordenada Y normalizada (0-1) para a posição final. O valor padrão é 1.0. | FLOAT | Sim | 0.0 - 1.0 |
| `número_de_quadros` | O número total de quadros para os quais gerar posições de trilha. O valor padrão é 81. | INT | Sim | 1 - 1024 |
| `número_de_trilhas` | O número de trilhas paralelas a serem geradas. O valor padrão é 5. | INT | Sim | 1 - 100 |
| `dispersão_de_trilhas` | Distância normalizada entre as trilhas. As trilhas são distribuídas perpendicularmente à direção do movimento. O valor padrão é 0.025. | FLOAT | Sim | 0.0 - 1.0 |
| `bezier` | Ativa o caminho de curva Bezier usando o ponto médio como ponto de controle. O valor padrão é Falso. | BOOLEAN | Sim | Verdadeiro / Falso |
| `meio_x` | Ponto de controle X normalizado para a curva Bezier. Usado apenas quando 'bezier' está ativado. O valor padrão é 0.5. | FLOAT | Sim | 0.0 - 1.0 |
| `meio_y` | Ponto de controle Y normalizado para a curva Bezier. Usado apenas quando 'bezier' está ativado. O valor padrão é 0.5. | FLOAT | Sim | 0.0 - 1.0 |
| `interpolação` | Controla o tempo/velocidade do movimento ao longo do caminho. O valor padrão é "linear". | COMBO | Sim | `"linear"`<br>`"ease_in"`<br>`"ease_out"`<br>`"ease_in_out"`<br>`"constant"` |
| `máscara_de_trilha` | Máscara opcional para indicar quadros visíveis. | MASK | Não | - |

**Nota:** Os parâmetros `mid_x` e `mid_y` são usados apenas quando o parâmetro `bezier` está definido como `True`. Quando `bezier` é `False`, o caminho é uma linha reta do ponto inicial ao ponto final.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `TRACKS` | Um objeto de trilhas contendo as coordenadas do caminho gerado e informações de visibilidade para todas as trilhas em todos os quadros. | TRACKS |
| `track_length` | O número de quadros para os quais as trilhas foram geradas, correspondendo ao `número_de_quadros` de entrada. | INT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GenerateTracks/pt-BR.md)

---
**Source fingerprint (SHA-256):** `3dca1cabaee8738e2a68acafed47ad347019d03c9b7f0d1392b3fdf97d0e8add`

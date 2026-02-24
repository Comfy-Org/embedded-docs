> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioEqualizer3Band/pt-BR.md)

O nó Audio Equalizer (3-Band) permite ajustar as frequências de graves, médios e agudos de uma forma de onda de áudio. Ele aplica três filtros separados: uma prateleira baixa (low shelf) para os graves, um filtro de pico (peaking) para os médios e uma prateleira alta (high shelf) para os agudos. Cada banda pode ser controlada independentemente com configurações de ganho, frequência e largura de banda.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `audio` | AUDIO | Sim | - | Os dados de áudio de entrada contendo a forma de onda e a taxa de amostragem. |
| `low_gain_dB` | FLOAT | Não | -24.0 a 24.0 | Ganho para as frequências baixas (Graves). Valores positivos realçam, valores negativos atenuam. (padrão: 0.0) |
| `low_freq` | INT | Não | 20 a 500 | Frequência de corte para o filtro de prateleira baixa (Low shelf) em Hertz (Hz). (padrão: 100) |
| `mid_gain_dB` | FLOAT | Não | -24.0 a 24.0 | Ganho para as frequências médias. Valores positivos realçam, valores negativos atenuam. (padrão: 0.0) |
| `mid_freq` | INT | Não | 200 a 4000 | Frequência central para o filtro de pico (Mid peaking) em Hertz (Hz). (padrão: 1000) |
| `mid_q` | FLOAT | Não | 0.1 a 10.0 | Fator Q (largura de banda) para o filtro de pico (Mid peaking). Valores mais baixos criam uma banda mais larga, valores mais altos criam uma banda mais estreita. (padrão: 0.707) |
| `high_gain_dB` | FLOAT | Não | -24.0 a 24.0 | Ganho para as frequências altas (Agudos). Valores positivos realçam, valores negativos atenuam. (padrão: 0.0) |
| `high_freq` | INT | Não | 1000 a 15000 | Frequência de corte para o filtro de prateleira alta (High shelf) em Hertz (Hz). (padrão: 5000) |

**Observação:** Os parâmetros `low_gain_dB`, `mid_gain_dB` e `high_gain_dB` só são aplicados quando seu valor não é zero. Se um ganho for definido como 0.0, o estágio do filtro correspondente é ignorado.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `audio` | AUDIO | Os dados de áudio processados com a equalização aplicada, contendo a forma de onda modificada e a taxa de amostragem original. |

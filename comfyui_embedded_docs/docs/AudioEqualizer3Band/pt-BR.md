> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioEqualizer3Band/pt-BR.md)

O nó Equalizador de Áudio (3 Bandas) permite ajustar as frequências graves, médias e agudas de uma forma de onda de áudio. Ele aplica três filtros separados: um filtro *low shelf* para graves, um filtro *peaking* para médios e um filtro *high shelf* para agudos. Cada banda pode ser controlada independentemente com ajustes de ganho, frequência e largura de banda.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `áudio` | AUDIO | Sim | - | Os dados de áudio de entrada contendo a forma de onda e a taxa de amostragem. |
| `ganho_baixo_dB` | FLOAT | Não | -24.0 a 24.0 | Ganho para frequências Baixas (Graves). Valores positivos aumentam, valores negativos cortam. (padrão: 0.0) |
| `freq_baixa` | INT | Não | 20 a 500 | Frequência de corte para o filtro *low shelf* em Hertz (Hz). (padrão: 100) |
| `ganho_médio_dB` | FLOAT | Não | -24.0 a 24.0 | Ganho para frequências Médias. Valores positivos aumentam, valores negativos cortam. (padrão: 0.0) |
| `freq_média` | INT | Não | 200 a 4000 | Frequência central para o filtro *peaking* de médios em Hertz (Hz). (padrão: 1000) |
| `q_médio` | FLOAT | Não | 0.1 a 10.0 | Fator Q (largura de banda) para o filtro *peaking* de médios. Valores menores criam uma banda mais larga, valores maiores criam uma banda mais estreita. (padrão: 0.707) |
| `ganho_agudo_dB` | FLOAT | Não | -24.0 a 24.0 | Ganho para frequências Altas (Agudos). Valores positivos aumentam, valores negativos cortam. (padrão: 0.0) |
| `freq_aguda` | INT | Não | 1000 a 15000 | Frequência de corte para o filtro *high shelf* em Hertz (Hz). (padrão: 5000) |

**Nota:** Os parâmetros `low_gain_dB`, `mid_gain_dB` e `high_gain_dB` são aplicados apenas quando seus valores são diferentes de zero. Se um ganho for definido como 0.0, o estágio do filtro correspondente é ignorado.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `áudio` | AUDIO | Os dados de áudio processados com a equalização aplicada, contendo a forma de onda modificada e a taxa de amostragem original. |

---
**Source fingerprint (SHA-256):** `7aeaec2959f1af6144e46d8e6c558a16193669846923df1db23ae9d47e5cc173`

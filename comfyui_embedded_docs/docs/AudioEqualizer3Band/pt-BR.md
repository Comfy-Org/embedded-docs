O nó Equalizador de Áudio (3 Bandas) permite ajustar as frequências graves, médias e agudas de uma forma de onda de áudio. Ele aplica três filtros separados: um filtro *low shelf* para graves, um filtro *peaking* para médios e um filtro *high shelf* para agudos. Cada banda pode ser controlada independentemente com ajustes de ganho, frequência e largura de banda.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `áudio` | Os dados de áudio de entrada contendo a forma de onda e a taxa de amostragem. | AUDIO | Sim | - |
| `ganho_baixo_dB` | Ganho para frequências Baixas (Graves). Valores positivos aumentam, valores negativos cortam. (padrão: 0.0) | FLOAT | Não | -24.0 a 24.0 |
| `freq_baixa` | Frequência de corte para o filtro *low shelf* em Hertz (Hz). (padrão: 100) | INT | Não | 20 a 500 |
| `ganho_médio_dB` | Ganho para frequências Médias. Valores positivos aumentam, valores negativos cortam. (padrão: 0.0) | FLOAT | Não | -24.0 a 24.0 |
| `freq_média` | Frequência central para o filtro *peaking* de médios em Hertz (Hz). (padrão: 1000) | INT | Não | 200 a 4000 |
| `q_médio` | Fator Q (largura de banda) para o filtro *peaking* de médios. Valores menores criam uma banda mais larga, valores maiores criam uma banda mais estreita. (padrão: 0.707) | FLOAT | Não | 0.1 a 10.0 |
| `ganho_agudo_dB` | Ganho para frequências Altas (Agudos). Valores positivos aumentam, valores negativos cortam. (padrão: 0.0) | FLOAT | Não | -24.0 a 24.0 |
| `freq_aguda` | Frequência de corte para o filtro *high shelf* em Hertz (Hz). (padrão: 5000) | INT | Não | 1000 a 15000 |

**Nota:** Os parâmetros `low_gain_dB`, `mid_gain_dB` e `high_gain_dB` são aplicados apenas quando seus valores são diferentes de zero. Se um ganho for definido como 0.0, o estágio do filtro correspondente é ignorado.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `áudio` | Os dados de áudio processados com a equalização aplicada, contendo a forma de onda modificada e a taxa de amostragem original. | AUDIO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioEqualizer3Band/pt-BR.md)

---
**Source fingerprint (SHA-256):** `7aeaec2959f1af6144e46d8e6c558a16193669846923df1db23ae9d47e5cc173`

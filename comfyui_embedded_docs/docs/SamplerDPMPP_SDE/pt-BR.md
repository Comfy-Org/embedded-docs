> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_SDE/pt-BR.md)

O nó SamplerDPMPP_SDE cria um amostrador DPM++ SDE (Equação Diferencial Estocástica) para uso no processo de amostragem. Este amostrador fornece um método de amostragem estocástico com parâmetros de ruído configuráveis e seleção de dispositivo. Ele retorna um objeto amostrador que pode ser usado no pipeline de amostragem.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `eta` | FLOAT | Sim | 0.0 - 100.0 | Controla a estocasticidade do processo de amostragem (padrão: 1.0) |
| `s_noise` | FLOAT | Sim | 0.0 - 100.0 | Controla a quantidade de ruído adicionada durante a amostragem (padrão: 1.0) |
| `r` | FLOAT | Sim | 0.0 - 100.0 | Um parâmetro que influencia o comportamento da amostragem (padrão: 0.5) |
| `noise_device` | COMBO | Sim | "gpu"<br>"cpu" | Seleciona o dispositivo onde os cálculos de ruído são realizados |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `sampler` | SAMPLER | Retorna um objeto amostrador DPM++ SDE configurado para uso em pipelines de amostragem |

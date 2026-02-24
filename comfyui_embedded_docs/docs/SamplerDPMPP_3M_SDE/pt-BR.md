> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_3M_SDE/pt-BR.md)

O nó SamplerDPMPP_3M_SDE cria um amostrador DPM++ 3M SDE para uso no processo de amostragem. Este amostrador utiliza um método de equação diferencial estocástica de múltiplos passos de terceira ordem com parâmetros de ruído configuráveis. O nó permite que você escolha se os cálculos de ruído são realizados na GPU ou na CPU.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `eta` | FLOAT | Sim | 0.0 - 100.0 | Controla a estocasticidade do processo de amostragem (padrão: 1.0) |
| `s_noise` | FLOAT | Sim | 0.0 - 100.0 | Controla a quantidade de ruído adicionada durante a amostragem (padrão: 1.0) |
| `noise_device` | COMBO | Sim | "gpu"<br>"cpu" | Seleciona o dispositivo para os cálculos de ruído, seja GPU ou CPU |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `sampler` | SAMPLER | Retorna um objeto amostrador configurado para uso em fluxos de trabalho de amostragem |

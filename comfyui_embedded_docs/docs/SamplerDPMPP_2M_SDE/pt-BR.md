> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_2M_SDE/pt-BR.md)

O nó SamplerDPMPP_2M_SDE cria um amostrador DPM++ 2M SDE para modelos de difusão. Este amostrador utiliza solucionadores de equações diferenciais de segunda ordem com equações diferenciais estocásticas para gerar amostras. Ele oferece diferentes tipos de solucionador e opções de manipulação de ruído para controlar o processo de amostragem.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `solver_type` | STRING | Sim | `"midpoint"`<br>`"heun"` | O tipo de solucionador de equação diferencial a ser usado no processo de amostragem |
| `eta` | FLOAT | Sim | 0.0 - 100.0 | Controla a estocasticidade do processo de amostragem (padrão: 1.0) |
| `s_noise` | FLOAT | Sim | 0.0 - 100.0 | Controla a quantidade de ruído adicionada durante a amostragem (padrão: 1.0) |
| `noise_device` | STRING | Sim | `"gpu"`<br>`"cpu"` | O dispositivo onde os cálculos de ruído são realizados |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `sampler` | SAMPLER | Um objeto amostrador configurado e pronto para uso no pipeline de amostragem |

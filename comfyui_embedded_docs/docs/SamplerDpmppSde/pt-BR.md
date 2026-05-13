> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDpmppSde/pt-BR.md)

Este nó foi projetado para gerar um amostrador para o modelo DPM++ SDE (Equação Diferencial Estocástica). Ele se adapta tanto a ambientes de execução em CPU quanto em GPU, otimizando a implementação do amostrador com base no hardware disponível.

## Entradas

| Parâmetro       | Tipo de Dado | Descrição |
|-----------------|--------------|-----------|
| `eta`           | FLOAT        | Especifica o tamanho do passo para o solucionador SDE, influenciando a granularidade do processo de amostragem. |
| `s_noise`       | FLOAT        | Determina o nível de ruído a ser aplicado durante o processo de amostragem, afetando a diversidade das amostras geradas. |
| `r`             | FLOAT        | Controla a proporção de redução de ruído no processo de amostragem, impactando a clareza e a qualidade das amostras geradas. |
| `noise_device`  | COMBO[STRING]| Seleciona o ambiente de execução (CPU ou GPU) para o amostrador, otimizando o desempenho com base no hardware disponível. |

## Saídas

| Parâmetro   | Tipo de Dado | Descrição |
|-------------|--------------|-----------|
| `sampler`   | SAMPLER      | O amostrador gerado, configurado com os parâmetros especificados, pronto para uso em operações de amostragem. |
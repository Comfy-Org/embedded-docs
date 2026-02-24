> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RescaleCFG/pt-BR.md)

O nó RescaleCFG foi projetado para ajustar as escalas de condicionamento e não condicionamento da saída de um modelo com base em um multiplicador especificado, visando alcançar um processo de geração mais equilibrado e controlado. Ele opera reescalonando a saída do modelo para modificar a influência dos componentes condicionados e não condicionados, potencialmente melhorando assim o desempenho ou a qualidade da saída do modelo.

## Entradas

| Parâmetro | Tipo de Dado | Descrição |
|-----------|-------------|-------------|
| `model`   | MODEL     | O parâmetro `model` representa o modelo generativo a ser ajustado. É crucial, pois o nó aplica uma função de reescalonamento à saída do modelo, influenciando diretamente o processo de geração. |
| `multiplier` | `FLOAT` | O parâmetro `multiplier` controla a extensão do reescalonamento aplicado à saída do modelo. Ele determina o equilíbrio entre os componentes originais e reescalonados, afetando as características da saída final. |

## Saídas

| Parâmetro | Tipo de Dado | Descrição |
|-----------|-------------|-------------|
| `model`   | MODEL     | O modelo modificado com as escalas de condicionamento e não condicionamento ajustadas. Espera-se que este modelo produza saídas com características potencialmente aprimoradas devido ao reescalonamento aplicado. |

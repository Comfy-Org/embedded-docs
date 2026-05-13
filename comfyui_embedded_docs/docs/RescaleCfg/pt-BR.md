> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RescaleCFG/pt-BR.md)

O nó RescaleCFG foi projetado para ajustar as escalas de condicionamento e não condicionamento da saída de um modelo com base em um multiplicador especificado, visando alcançar um processo de geração mais equilibrado e controlado. Ele opera redimensionando a saída do modelo para modificar a influência dos componentes condicionados e não condicionados, potencialmente melhorando o desempenho do modelo ou a qualidade da saída.

## Entradas

| Parâmetro | Tipo de Dados | Descrição |
|-----------|-------------|-------------|
| `modelo`   | MODEL     | O parâmetro do modelo representa o modelo generativo a ser ajustado. Ele é crucial, pois o nó aplica uma função de redimensionamento à saída do modelo, influenciando diretamente o processo de geração. |
| `multiplicador` | `FLOAT` | O parâmetro multiplicador controla a extensão do redimensionamento aplicado à saída do modelo. Ele determina o equilíbrio entre os componentes original e redimensionado, afetando as características da saída final. |

## Saídas

| Parâmetro | Tipo de Dados | Descrição |
|-----------|-------------|-------------|
| `modelo`   | MODEL     | O modelo modificado com escalas de condicionamento e não condicionamento ajustadas. Espera-se que este modelo produza saídas com características potencialmente aprimoradas devido ao redimensionamento aplicado. |
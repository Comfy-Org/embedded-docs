> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PolyexponentialScheduler/pt-BR.md)

O nó PolyexponentialScheduler é projetado para gerar uma sequência de níveis de ruído (sigmas) com base em um cronograma de ruído poli-exponencial. Este cronograma é uma função polinomial no logaritmo do sigma, permitindo uma progressão flexível e personalizável dos níveis de ruído ao longo do processo de difusão.

## Entradas

| Parâmetro   | Tipo de Dado | Descrição                                                                                                                                                                                                                                                                                                                                                      |
|-------------|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `steps`     | INT         | Especifica o número de etapas no processo de difusão, afetando a granularidade dos níveis de ruído gerados.                                                                                                                                                                                                                                                                        |
| `sigma_max` | FLOAT       | O nível máximo de ruído, que define o limite superior do cronograma de ruído.                                                                                                                                                                                                                                                                                                                                 |
| `sigma_min` | FLOAT       | O nível mínimo de ruído, que define o limite inferior do cronograma de ruído.                                                                                                                                                                                                                                                                                                                                 |
| `rho`       | FLOAT       | Um parâmetro que controla a forma do cronograma de ruído poli-exponencial, influenciando como os níveis de ruído progridem entre os valores mínimo e máximo.                                                                                                                                                                                                               |

## Saídas

| Parâmetro | Tipo de Dado | Descrição                                                                 |
|-----------|-------------|-----------------------------------------------------------------------------|
| `sigmas`  | SIGMAS      | A saída é uma sequência de níveis de ruído (sigmas) adaptada ao cronograma de ruído poli-exponencial especificado. |

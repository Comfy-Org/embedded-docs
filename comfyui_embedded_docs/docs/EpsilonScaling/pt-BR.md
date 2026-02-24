> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EpsilonScaling/pt-BR.md)

Implementa o método Epsilon Scaling do artigo de pesquisa "Elucidating the Exposure Bias in Diffusion Models". Este método melhora a qualidade da amostra ao escalar o ruído previsto durante o processo de amostragem. Ele usa um cronograma uniforme para mitigar o viés de exposição em modelos de difusão.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sim | - | O modelo ao qual aplicar o escalonamento epsilon |
| `scaling_factor` | FLOAT | Não | 0.5 - 1.5 | O fator usado para escalar o ruído previsto (padrão: 1.005) |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `model` | MODEL | O modelo com o escalonamento epsilon aplicado |

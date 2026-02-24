> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentOperationTonemapReinhard/pt-BR.md)

O nó LatentOperationTonemapReinhard aplica o mapeamento de tons (tonemapping) Reinhard a vetores latentes. Esta técnica normaliza os vetores latentes e ajusta sua magnitude usando uma abordagem estatística baseada na média e no desvio padrão, com a intensidade controlada por um parâmetro multiplicador.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `multiplier` | FLOAT | Não | 0.0 a 100.0 | Controla a intensidade do efeito de mapeamento de tons (padrão: 1.0) |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `operation` | LATENT_OPERATION | Retorna uma operação de mapeamento de tons que pode ser aplicada a vetores latentes |

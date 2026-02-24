> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoTriangleCFGGuidance/pt-BR.md)

O nó VideoTriangleCFGGuidance aplica um padrão de escala de orientação (guidance) triangular sem classificador (CFG) a modelos de vídeo. Ele modifica a escala de condicionamento ao longo do tempo usando uma função de onda triangular que oscila entre o valor mínimo de CFG e a escala de condicionamento original. Isso cria um padrão de orientação dinâmico que pode ajudar a melhorar a consistência e a qualidade da geração de vídeo.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sim | - | O modelo de vídeo ao qual aplicar a orientação triangular CFG |
| `min_cfg` | FLOAT | Sim | 0.0 - 100.0 | O valor mínimo da escala CFG para o padrão triangular (padrão: 1.0) |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `model` | MODEL | O modelo modificado com a orientação triangular CFG aplicada |

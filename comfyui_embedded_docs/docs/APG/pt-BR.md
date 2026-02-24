> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/APG/pt-BR.md)

O nó APG (Adaptive Projected Guidance, ou Orientação por Projeção Adaptativa) modifica o processo de amostragem ajustando a forma como a orientação (guidance) é aplicada durante a difusão. Ele separa o vetor de orientação em componentes paralelos e ortogonais em relação à saída condicional, permitindo uma geração de imagem mais controlada. O nó fornece parâmetros para dimensionar a orientação, normalizar sua magnitude e aplicar momentum para transições mais suaves entre os passos de difusão.

## Entradas

| Parâmetro | Tipo de Dado | Tipo de Entrada | Padrão | Intervalo | Descrição |
|-----------|-----------|------------|---------|-------|-------------|
| `model` | MODEL | Obrigatório | - | - | O modelo de difusão ao qual aplicar a orientação por projeção adaptativa |
| `eta` | FLOAT | Obrigatório | 1.0 | -10.0 a 10.0 | Controla a escala do vetor de orientação paralela. O comportamento padrão do CFG ocorre com o valor 1. |
| `norm_threshold` | FLOAT | Obrigatório | 5.0 | 0.0 a 50.0 | Normaliza o vetor de orientação para este valor. A normalização é desativada com o valor 0. |
| `momentum` | FLOAT | Obrigatório | 0.0 | -5.0 a 1.0 | Controla uma média móvel da orientação durante a difusão, desativada com o valor 0. |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `model` | MODEL | Retorna o modelo modificado com a orientação por projeção adaptativa aplicada ao seu processo de amostragem |

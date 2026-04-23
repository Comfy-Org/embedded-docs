> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FrameInterpolate/pt-BR.md)

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FrameInterpolate/en.md)

## Visão Geral

O nó Frame Interpolate cria novos quadros entre os existentes em uma sequência de imagens, aumentando efetivamente a taxa de quadros. Ele utiliza um modelo de IA para prever como devem ser os quadros intermediários, o que pode ser usado para criar efeitos de câmera lenta suaves ou para aumentar a suavidade de um vídeo.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `interp_model` | MODEL | Sim | - | O modelo de interpolação de quadros a ser usado para gerar os quadros intermediários |
| `images` | IMAGE | Sim | - | Um lote de imagens consecutivas (quadros) para interpolar. Requer pelo menos 2 imagens. |
| `multiplier` | INT | Sim | 2 a 16 | O número de vezes para multiplicar a contagem de quadros. Por exemplo, um multiplicador de 2 dobra o número de quadros. (padrão: 2) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `IMAGE` | IMAGE | Um novo lote de imagens com os quadros interpolados inseridos entre os quadros originais, resultando em uma sequência mais suave. O número total de quadros de saída é `(número de quadros de entrada - 1) * multiplicador + 1`. |
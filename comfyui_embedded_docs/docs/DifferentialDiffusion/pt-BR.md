> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DifferentialDiffusion/pt-BR.md)

O nó Differential Diffusion modifica o processo de remoção de ruído aplicando uma máscara binária baseada em limiares de timestep. Ele cria uma máscara que mescla entre a máscara de remoção de ruído original e uma máscara binária baseada em limiares, permitindo um ajuste controlado da força do processo de difusão.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sim | - | O modelo de difusão a ser modificado |
| `strength` | FLOAT | Não | 0.0 - 1.0 | Controla a força da mesclagem entre a máscara de remoção de ruído original e a máscara binária de limiar (padrão: 1.0) |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `model` | MODEL | O modelo de difusão modificado com a função de máscara de remoção de ruído atualizada |

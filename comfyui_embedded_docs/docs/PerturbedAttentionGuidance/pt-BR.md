> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PerturbedAttentionGuidance/pt-BR.md)

O nó PerturbedAttentionGuidance aplica a orientação de atenção perturbada a um modelo de difusão para melhorar a qualidade da geração. Ele modifica o mecanismo de auto-atenção do modelo durante a amostragem, substituindo-o por uma versão simplificada que se concentra nas projeções de valor. Essa técnica ajuda a melhorar a coerência e a qualidade das imagens geradas ajustando o processo de remoção de ruído condicional.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sim | - | O modelo de difusão ao qual aplicar a orientação de atenção perturbada |
| `scale` | FLOAT | Não | 0.0 - 100.0 | A intensidade do efeito de orientação de atenção perturbada (padrão: 3.0) |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `model` | MODEL | O modelo modificado com a orientação de atenção perturbada aplicada |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DisableNoise/pt-BR.md)

O nó DisableNoise fornece uma configuração de ruído vazia que pode ser usada para desativar a geração de ruído em processos de amostragem. Ele retorna um objeto de ruído especial que não contém dados de ruído, permitindo que outros nós ignorem operações relacionadas a ruído quando conectados a esta saída.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| *Sem parâmetros de entrada* | - | - | - | Este nó não requer nenhum parâmetro de entrada. |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `NOISE` | NOISE | Retorna uma configuração de ruído vazia que pode ser usada para desativar a geração de ruído em processos de amostragem. |

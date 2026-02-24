> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVScheduler/pt-BR.md)

O nó LTXVScheduler gera valores sigma para processos de amostragem personalizados. Ele calcula parâmetros de programação de ruído com base no número de tokens no latente de entrada e aplica uma transformação sigmoide para criar a programação de amostragem. O nó pode, opcionalmente, esticar os sigmas resultantes para corresponder a um valor terminal especificado.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `steps` | INT | Sim | 1-10000 | Número de etapas de amostragem (padrão: 20) |
| `max_shift` | FLOAT | Sim | 0.0-100.0 | Valor de deslocamento máximo para o cálculo do sigma (padrão: 2.05) |
| `base_shift` | FLOAT | Sim | 0.0-100.0 | Valor de deslocamento base para o cálculo do sigma (padrão: 0.95) |
| `stretch` | BOOLEAN | Sim | Verdadeiro/Falso | Esticar os sigmas para ficarem no intervalo [terminal, 1] (padrão: Verdadeiro) |
| `terminal` | FLOAT | Sim | 0.0-0.99 | O valor terminal dos sigmas após o estiramento (padrão: 0.1) |
| `latent` | LATENT | Não | - | Entrada latente opcional usada para calcular a contagem de tokens para ajuste do sigma |

**Observação:** O parâmetro `latent` é opcional. Quando não fornecido, o nó usa uma contagem de tokens padrão de 4096 para os cálculos.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `sigmas` | SIGMAS | Valores sigma gerados para o processo de amostragem |

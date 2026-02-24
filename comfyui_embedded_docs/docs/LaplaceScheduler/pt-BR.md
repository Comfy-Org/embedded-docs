> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LaplaceScheduler/pt-BR.md)

O nó LaplaceScheduler gera uma sequência de valores sigma seguindo uma distribuição de Laplace para uso na amostragem de difusão. Ele cria um cronograma de níveis de ruído que diminuem gradualmente de um valor máximo para um mínimo, utilizando parâmetros da distribuição de Laplace para controlar a progressão. Este agendador é comumente usado em fluxos de trabalho de amostragem personalizados para definir o cronograma de ruído para modelos de difusão.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `steps` | INT | Sim | 1 a 10000 | Número de etapas de amostragem no cronograma (padrão: 20) |
| `sigma_max` | FLOAT | Sim | 0.0 a 5000.0 | Valor sigma máximo no início do cronograma (padrão: 14.614642) |
| `sigma_min` | FLOAT | Sim | 0.0 a 5000.0 | Valor sigma mínimo no final do cronograma (padrão: 0.0291675) |
| `mu` | FLOAT | Sim | -10.0 a 10.0 | Parâmetro de média para a distribuição de Laplace (padrão: 0.0) |
| `beta` | FLOAT | Sim | 0.0 a 10.0 | Parâmetro de escala para a distribuição de Laplace (padrão: 0.5) |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `SIGMAS` | SIGMAS | Uma sequência de valores sigma seguindo um cronograma de distribuição de Laplace |

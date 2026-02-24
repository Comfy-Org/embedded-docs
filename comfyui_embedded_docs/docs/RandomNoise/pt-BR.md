> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RandomNoise/pt-BR.md)

O nó RandomNoise gera padrões de ruído aleatório com base em um valor de semente. Ele cria ruído reproduzível que pode ser usado para várias tarefas de processamento e geração de imagens. A mesma semente sempre produzirá o mesmo padrão de ruído, permitindo resultados consistentes em múltiplas execuções.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `noise_seed` | INT | Sim | 0 a 18446744073709551615 | O valor da semente usado para gerar o padrão de ruído aleatório (padrão: 0). A mesma semente sempre produzirá a mesma saída de ruído. |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `noise` | NOISE | O padrão de ruído aleatório gerado com base no valor de semente fornecido. |

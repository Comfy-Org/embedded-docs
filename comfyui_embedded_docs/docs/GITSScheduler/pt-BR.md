# GITSScheduler

O nó GITSScheduler gera a programação de sigma (nível de ruído) usada pelo método de amostragem GITS. Ele seleciona uma tabela de níveis de ruído predefinida com base no parâmetro `coeff` e no número de `steps`, opcionalmente reduzindo a programação quando um valor de `denoise` inferior a 1.0 é usado.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `coeff` | O coeficiente que seleciona qual tabela de níveis de ruído predefinida é usada para construir a programação. O valor é arredondado para 2 casas decimais (padrão: 1.20) | FLOAT | Sim | 0.80 - 1.50 |
| `steps` | O número total de passos de amostragem para gerar sigmas (padrão: 10) | INT | Sim | 2 - 1000 |
| `denoise` | Fator de denoising que reduz o número de passos usados (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |

**Nota:** Quando `denoise` é definido como 0.0, o nó retorna um tensor vazio. Quando `denoise` é menor que 1.0, o número real de passos usados é calculado como `round(steps * denoise)`. Para passos até 20, o nó usa níveis de ruído predefinidos diretamente; para passos maiores que 20, ele usa interpolação log-linear para estender os níveis de ruído predefinidos ao número desejado de passos.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `sigmas` | Os valores de sigma gerados para a programação de ruído | SIGMAS |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GITSScheduler/pt-BR.md)

---
**Source fingerprint (SHA-256):** `f46681970fece985f6a4b62d0817d1ea306f1ca9a20189f937512dd5717f458b`

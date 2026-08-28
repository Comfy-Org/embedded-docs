# LaplaceScheduler

O nó LaplaceScheduler gera uma sequência de valores sigma seguindo uma distribuição de Laplace para uso em amostragem de difusão. Ele cria uma programação de níveis de ruído que diminuem gradualmente de um valor máximo para um mínimo, usando parâmetros da distribuição de Laplace para controlar a progressão. Este agendador é comumente usado em fluxos de trabalho de amostragem personalizados para definir a programação de ruído para modelos de difusão.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `passos` | Número de passos de amostragem na programação (padrão: 20) | INT | Sim | 1 a 10000 |
| `sigma_max` | Valor máximo de sigma no início da programação (padrão: 14.614642) | FLOAT | Sim | 0.0 a 5000.0 |
| `sigma_min` | Valor mínimo de sigma no final da programação (padrão: 0.0291675) | FLOAT | Sim | 0.0 a 5000.0 |
| `mu` | Parâmetro de média para a distribuição de Laplace (padrão: 0.0) | FLOAT | Sim | -10.0 a 10.0 |
| `beta` | Parâmetro de escala para a distribuição de Laplace (padrão: 0.5) | FLOAT | Sim | 0.0 a 10.0 |

Nota: `sigma_max`, `sigma_min`, `mu` e `beta` são parâmetros avançados.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `SIGMAS` | Uma sequência de valores sigma seguindo uma programação de distribuição de Laplace | SIGMAS |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LaplaceScheduler/pt-BR.md)

---
**Source fingerprint (SHA-256):** `8e5ca00f4797f863a2cf8b9b115ec27beb7f65981cbb04eb036150402fc19389`

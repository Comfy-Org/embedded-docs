# LaplaceScheduler

O nó LaplaceScheduler gera uma sequência de valores sigma seguindo uma distribuição de Laplace para uso na amostragem por difusão. Ele cria um cronograma de níveis de ruído que diminuem gradualmente de um valor máximo para um mínimo, usando parâmetros da distribuição de Laplace para controlar a progressão. Este agendador é comumente usado em fluxos de trabalho de amostragem personalizados para definir o cronograma de ruído para modelos de difusão.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `passos` | Número de etapas de amostragem no cronograma (padrão: 20) | INT | Sim | 1 a 10000 |
| `sigma_max` | Valor sigma máximo no início do cronograma (padrão: 14.614642) | FLOAT | Sim | 0.0 a 5000.0 |
| `sigma_min` | Valor sigma mínimo no final do cronograma (padrão: 0.0291675) | FLOAT | Sim | 0.0 a 5000.0 |
| `mu` | Parâmetro de média para a distribuição de Laplace (padrão: 0.0) | FLOAT | Sim | -10.0 a 10.0 |
| `beta` | Parâmetro de escala para a distribuição de Laplace (padrão: 0.5) | FLOAT | Sim | 0.0 a 10.0 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `SIGMAS` | Uma sequência de valores sigma seguindo um cronograma de distribuição de Laplace | SIGMAS |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LaplaceScheduler/pt-BR.md)

---
**Source fingerprint (SHA-256):** `9d8cacb93d0bb1872a368821fd3cad5d6d373817a923436af9f62a7648d5d735`

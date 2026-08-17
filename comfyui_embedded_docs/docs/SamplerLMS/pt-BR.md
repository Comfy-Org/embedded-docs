# SamplerLMS

O nó SamplerLMS cria um amostrador de Mínimos Quadrados Médios (LMS) para uso em modelos de difusão. Ele gera um objeto de amostrador que pode ser usado no processo de amostragem, permitindo controlar a ordem do algoritmo LMS para estabilidade e precisão numéricas.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `order` | O parâmetro de ordem para o algoritmo do amostrador LMS, que controla a precisão e a estabilidade do método numérico (padrão: 4; parâmetro avançado) | INT | Sim | 1 a 100 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `sampler` | Um objeto de amostrador LMS configurado que pode ser usado no pipeline de amostragem | SAMPLER |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerLMS/pt-BR.md)

---
**Source fingerprint (SHA-256):** `3d59fbbd5b9b0bfa2ee3b384aca08855988d0b7a2a94d805f978b9dd7caa0f39`

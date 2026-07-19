# SamplerLMS

O nó SamplerLMS cria um amostrador de Mínimos Quadrados Médios (LMS) para uso em modelos de difusão. Ele gera um objeto amostrador que pode ser utilizado no processo de amostragem, permitindo controlar a ordem do algoritmo LMS para estabilidade e precisão numérica.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `ordem` | O parâmetro de ordem para o algoritmo do amostrador LMS, que controla a precisão e estabilidade do método numérico (padrão: 4) | INT | Sim | 1 a 100 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `sampler` | Um objeto amostrador LMS configurado que pode ser usado no pipeline de amostragem | SAMPLER |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerLMS/pt-BR.md)

---
**Source fingerprint (SHA-256):** `0c045ef15890fe611dc0b9d455bafa313d28373a29c881a0c8bf5d80e69bc114`

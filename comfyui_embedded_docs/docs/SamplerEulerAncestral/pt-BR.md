# SamplerEulerAncestral

O nó SamplerEulerAncestral cria um amostrador Euler Ancestral para gerar imagens. Este amostrador utiliza uma abordagem matemática específica que combina integração Euler com técnicas de amostragem ancestral para produzir variações de imagem. O nó permite configurar o comportamento da amostragem ajustando parâmetros que controlam a aleatoriedade e o tamanho do passo durante o processo de geração.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `eta` | Controla o tamanho do passo e a estocasticidade do processo de amostragem (padrão: 1.0). Este é um parâmetro avançado. | FLOAT | Não | 0.0 - 100.0 |
| `s_noise` | Controla a quantidade de ruído adicionada durante a amostragem (padrão: 1.0). Este é um parâmetro avançado. | FLOAT | Não | 0.0 - 100.0 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `sampler` | Retorna um amostrador Euler Ancestral configurado que pode ser usado no pipeline de amostragem. | SAMPLER |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerEulerAncestral/pt-BR.md)

---
**Source fingerprint (SHA-256):** `4d167de55f003383ccbb4a53daa14496bd931589781d56b62bf282a811669670`

# SamplerEulerAncestral

O nó SamplerEulerAncestral cria um sampler Euler Ancestral que pode ser usado durante a geração de imagens. Este sampler combina integração de Euler com amostragem ancestral, o que adiciona um grau de aleatoriedade a cada passo para produzir resultados variados. O nó permite ajustar quanta aleatoriedade é aplicada por meio de suas configurações.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `eta` | Controla o tamanho do passo e a estocasticidade do processo de amostragem (padrão: 1.0). Este é um parâmetro avançado. | FLOAT | Sim | 0.0 - 100.0 |
| `s_noise` | Controla a quantidade de ruído adicionada durante a amostragem (padrão: 1.0). Este é um parâmetro avançado. | FLOAT | Sim | 0.0 - 100.0 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `sampler` | Retorna um sampler Euler Ancestral configurado que pode ser usado no pipeline de amostragem. | SAMPLER |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerEulerAncestral/pt-BR.md)

---
**Source fingerprint (SHA-256):** `0d3c1f0ffe01eb6cc17fd53e743713f659218ec19001c670440472ae7d0d3887`

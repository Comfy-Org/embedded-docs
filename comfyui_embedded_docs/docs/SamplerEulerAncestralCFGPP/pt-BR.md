O nó SamplerEulerAncestralCFGPP cria um amostrador que utiliza o método Euler Ancestral com orientação livre de classificador (CFG++) para geração de imagens. Este amostrador combina técnicas de amostragem ancestral com condicionamento de orientação para produzir variações diversas de imagens, mantendo a coerência, e permite ajustes finos por meio de parâmetros que controlam o ruído e os ajustes de tamanho do passo.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `eta` | Controla o tamanho do passo durante a amostragem, com valores maiores resultando em atualizações mais agressivas (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `s_noise` | Ajusta a quantidade de ruído adicionada durante o processo de amostragem (padrão: 1.0) | FLOAT | Sim | 0.0 - 10.0 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `sampler` | Retorna um objeto amostrador configurado que pode ser usado no pipeline de geração de imagens | SAMPLER |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerEulerAncestralCFGPP/pt-BR.md)

---
**Source fingerprint (SHA-256):** `7eceec539a6a045db4d9953214add17011ef9d17e663dbbbbbb2bae0cbe40aa2`

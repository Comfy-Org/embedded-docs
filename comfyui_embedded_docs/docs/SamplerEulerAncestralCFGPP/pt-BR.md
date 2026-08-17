# SamplerEulerAncestralCFG++

O nó SamplerEulerAncestralCFGPP cria um amostrador que utiliza o método Euler Ancestral com orientação livre de classificador (CFG++) para geração de imagens. Este amostrador combina técnicas de amostragem ancestral com condicionamento por orientação para produzir variações diversas de imagens, mantendo a coerência, e permite ajuste fino por meio de parâmetros que controlam o ruído e ajustes de tamanho do passo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `eta` | Controla o tamanho do passo durante a amostragem, com valores maiores resultando em atualizações mais agressivas (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `s_noise` | Ajusta a quantidade de ruído adicionada durante o processo de amostragem (padrão: 1.0) | FLOAT | Sim | 0.0 - 10.0 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `sampler` | Retorna um objeto de amostrador configurado que pode ser usado no pipeline de geração de imagens | SAMPLER |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerEulerAncestralCFGPP/pt-BR.md)

---
**Source fingerprint (SHA-256):** `de83cb4c3e9aeee60f1554ad1af8181adb4fa62e3d23cec02a6f4396b96500c1`

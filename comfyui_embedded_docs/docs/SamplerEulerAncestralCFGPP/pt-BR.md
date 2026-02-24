> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerEulerAncestralCFGPP/pt-BR.md)

O nó SamplerEulerAncestralCFGPP cria um amostrador especializado para gerar imagens usando o método Euler Ancestral com orientação livre de classificador. Este amostrador combina técnicas de amostragem ancestral com condicionamento de orientação para produzir variações de imagem diversas, mantendo a coerência. Ele permite o ajuste fino do processo de amostragem por meio de parâmetros que controlam o ruído e os ajustes do tamanho do passo.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `eta` | FLOAT | Sim | 0.0 - 1.0 | Controla o tamanho do passo durante a amostragem, com valores mais altos resultando em atualizações mais agressivas (padrão: 1.0) |
| `s_noise` | FLOAT | Sim | 0.0 - 10.0 | Ajusta a quantidade de ruído adicionada durante o processo de amostragem (padrão: 1.0) |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `sampler` | SAMPLER | Retorna um objeto amostrador configurado que pode ser usado no pipeline de geração de imagens |

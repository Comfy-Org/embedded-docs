> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerEulerAncestral/pt-BR.md)

O nó SamplerEulerAncestral cria um amostrador Euler Ancestral para gerar imagens. Este amostrador utiliza uma abordagem matemática específica que combina a integração de Euler com técnicas de amostragem ancestral para produzir variações de imagem. O nó permite configurar o comportamento da amostragem ajustando parâmetros que controlam a aleatoriedade e o tamanho do passo durante o processo de geração.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `eta` | FLOAT | Sim | 0.0 - 100.0 | Controla o tamanho do passo e a estocasticidade do processo de amostragem (padrão: 1.0) |
| `s_noise` | FLOAT | Sim | 0.0 - 100.0 | Controla a quantidade de ruído adicionada durante a amostragem (padrão: 1.0) |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `sampler` | SAMPLER | Retorna um amostrador Euler Ancestral configurado que pode ser usado no pipeline de amostragem |

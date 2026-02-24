> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeSDXLRefiner/pt-BR.md)

Este nó foi projetado especificamente para o modelo SDXL Refiner para converter prompts de texto em informações de condicionamento, incorporando pontuações estéticas e informações dimensionais para aprimorar as condições das tarefas de geração, melhorando assim o efeito final de refinamento. Ele atua como um diretor de arte profissional, não apenas transmitindo sua intenção criativa, mas também injetando padrões estéticos precisos e requisitos de especificação no trabalho.

## Sobre o SDXL Refiner

O SDXL Refiner é um modelo de refinamento especializado que se concentra em aprimorar detalhes e a qualidade da imagem com base no modelo base SDXL. Este processo é como ter um retocador de arte:

1. Primeiro, ele recebe imagens preliminares ou descrições de texto geradas pelo modelo base
2. Em seguida, ele orienta o processo de refinamento por meio de pontuações estéticas precisas e parâmetros dimensionais
3. Por fim, ele se concentra no processamento de detalhes de imagem de alta frequência para melhorar a qualidade geral

O Refiner pode ser usado de duas maneiras:

- Como uma etapa de refinamento autônoma para pós-processar imagens geradas pelo modelo base
- Como parte de um sistema de integração especializada, assumindo o processamento durante a fase de baixo ruído da geração

## Entradas

| Nome do Parâmetro | Tipo de Dados | Tipo de Entrada | Valor Padrão | Faixa de Valores | Descrição |
|----------------|-----------|------------|---------------|-------------|-------------|
| `clip` | CLIP | Obrigatório | - | - | Instância do modelo CLIP usada para tokenização e codificação de texto, o componente central para converter texto em um formato compreensível pelo modelo |
| `ascore` | FLOAT | Opcional | 6.0 | 0.0-1000.0 | Controla a qualidade visual e a estética das imagens geradas, semelhante a definir padrões de qualidade para uma obra de arte:<br/>- Pontuações altas (7.5-8.5): Busca efeitos mais refinados e ricos em detalhes<br/>- Pontuações médias (6.0-7.0): Controle de qualidade equilibrado<br/>- Pontuações baixas (2.0-3.0): Adequado para prompts negativos |
| `width` | INT | Obrigatório | 1024 | 64-16384 | Especifica a largura da imagem de saída (pixels), deve ser múltiplo de 8. O SDXL tem melhor desempenho quando a contagem total de pixels está próxima de 1024×1024 (cerca de 1M de pixels) |
| `height` | INT | Obrigatório | 1024 | 64-16384 | Especifica a altura da imagem de saída (pixels), deve ser múltiplo de 8. O SDXL tem melhor desempenho quando a contagem total de pixels está próxima de 1024×1024 (cerca de 1M de pixels) |
| `text` | STRING | Obrigatório | - | - | Descrição do prompt de texto, suporta entrada de múltiplas linhas e sintaxe de prompt dinâmico. No Refiner, os prompts de texto devem se concentrar mais em descrever a qualidade visual desejada e as características dos detalhes |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | Saída condicional refinada contendo a codificação integrada da semântica do texto, padrões estéticos e informações dimensionais, especificamente para orientar o modelo SDXL Refiner no refinamento preciso da imagem |

## Observações

1. Este nó é especificamente otimizado para o modelo SDXL Refiner e difere dos nós CLIPTextEncode regulares
2. Uma pontuação estética de 7.5 é recomendada como linha de base, que é a configuração padrão usada no treinamento do SDXL
3. Todos os parâmetros dimensionais devem ser múltiplos de 8, e recomenda-se que a contagem total de pixels esteja próxima de 1024×1024 (cerca de 1M de pixels)
4. O modelo Refiner foca em aprimorar detalhes e qualidade da imagem, portanto, os prompts de texto devem enfatizar os efeitos visuais desejados em vez do conteúdo da cena
5. No uso prático, o Refiner é tipicamente usado nos estágios finais da geração (aproximadamente os últimos 20% dos passos), focando na otimização de detalhes

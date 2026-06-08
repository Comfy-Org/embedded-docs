O nó KSamplerAdvanced foi projetado para aprimorar o processo de amostragem, oferecendo configurações e técnicas avançadas. Seu objetivo é fornecer opções mais sofisticadas para gerar amostras a partir de um modelo, melhorando as funcionalidades básicas do KSampler.

## Entradas

| Parâmetro | Descrição | Tipo de Dado |
| --- | --- | --- |
| `modelo` | Especifica o modelo a partir do qual as amostras serão geradas, desempenhando um papel crucial no processo de amostragem. | MODEL |
| `adicionar_ruído` | Determina se ruído deve ser adicionado ao processo de amostragem, afetando a diversidade e a qualidade das amostras geradas. | COMBO[STRING] |
| `semente_do_ruído` | Define a semente para a geração de ruído, garantindo reprodutibilidade no processo de amostragem. | INT |
| `passos` | Define o número de etapas a serem executadas no processo de amostragem, impactando o detalhamento e a qualidade da saída. | INT |
| `cfg` | Controla o fator de condicionamento, influenciando a direção e o espaço do processo de amostragem. | FLOAT |
| `nome_do_sampler` | Seleciona o amostrador específico a ser utilizado, permitindo a personalização da técnica de amostragem. | COMBO[STRING] |
| `agendador` | Escolhe o agendador para controlar o processo de amostragem, afetando a progressão e a qualidade das amostras. | COMBO[STRING] |
| `positivo` | Especifica o condicionamento positivo para guiar a amostragem em direção a atributos desejados. | CONDITIONING |
| `negativo` | Especifica o condicionamento negativo para desviar a amostragem de certos atributos. | CONDITIONING |
| `imagem_latente` | Fornece a imagem latente inicial a ser usada no processo de amostragem, servindo como ponto de partida. | LATENT |
| `iniciar_no_passo` | Determina a etapa inicial do processo de amostragem, permitindo controle sobre a progressão da amostragem. | INT |
| `terminar_no_passo` | Define a etapa final do processo de amostragem, delimitando o escopo da amostragem. | INT |
| `retornar_com_ruído_restante` | Indica se a amostra deve ser retornada com ruído residual, afetando a aparência da saída final. | COMBO[STRING] |

## Saídas

| Parâmetro | Descrição | Tipo de Dado |
| --- | --- | --- |
| `latent` | A saída representa a imagem latente gerada a partir do modelo, refletindo as configurações e técnicas aplicadas. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KSamplerAdvanced/pt-BR.md)

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KSamplerAdvanced/pt-BR.md)

O nó KSamplerAdvanced foi projetado para aprimorar o processo de amostragem, fornecendo configurações e técnicas avançadas. Seu objetivo é oferecer opções mais sofisticadas para gerar ames de um modelo, melhorando as funcionalidades básicas do KSampler.

## Entradas

| Parâmetro | Tipo de Dados | Descrição |
|---|---|---|
| `model` | MODEL | Especifica o modelo a partir do qual as amostras serão geradas, desempenhando um papel crucial no processo de amostragem. |
| `add_noise` | COMBO[STRING] | Determina se o ruído deve ser adicionado ao processo de amostragem, afetando a diversidade e a qualidade das amostras geradas. |
| `noise_seed` | INT | Define a semente para a geração de ruído, garantindo a reprodutibilidade no processo de amostragem. |
| `steps` | INT | Define o número de etapas a serem executadas no processo de amostragem, impactando o detalhe e a qualidade da saída. |
| `cfg` | FLOAT | Controla o fator de condicionamento, influenciando a direção e o espaço do processo de amostragem. |
| `sampler_name` | COMBO[STRING] | Seleciona o amostrador específico a ser usado, permitindo a personalização da técnica de amostragem. |
| `scheduler` | COMBO[STRING] | Escolhe o agendador para controlar o processo de amostragem, afetando a progressão e a qualidade das amostras. |
| `positive` | CONDITIONING | Especifica o condicionamento positivo para orientar a amostragem em direção aos atributos desejados. |
| `negative` | CONDITIONING | Especifica o condicionamento negativo para afastar a amostragem de certos atributos. |
| `latent_image` | LATENT | Fornece a imagem latente inicial a ser usada no processo de amostragem, servindo como ponto de partida. |
| `start_at_step` | INT | Determina a etapa inicial do processo de amostragem, permitindo o controle sobre a progressão da amostragem. |
| `end_at_step` | INT | Define a etapa final do processo de amostragem, estabelecendo o escopo da amostragem. |
| `return_with_leftover_noise` | COMBO[STRING] | Indica se a amostra deve ser retornada com ruído residual, afetando a aparência da saída final. |

## Saídas

| Parâmetro | Tipo de Dados | Descrição |
|---|---|---|
| `latent` | LATENT | A saída representa a imagem latente gerada a partir do modelo, refletindo as configurações e técnicas aplicadas. |

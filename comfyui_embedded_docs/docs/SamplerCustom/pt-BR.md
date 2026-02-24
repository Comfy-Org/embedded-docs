> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerCustom/pt-BR.md)

O nó SamplerCustom é projetado para fornecer um mecanismo de amostragem flexível e personalizável para diversas aplicações. Ele permite que os usuários selecionem e configurem diferentes estratégias de amostragem adaptadas às suas necessidades específicas, aumentando a adaptabilidade e a eficiência do processo de amostragem.

## Entradas

| Parâmetro | Tipo de Dado | Descrição |
|-----------|--------------|-------------|
| `model`   | `MODEL`      | A entrada 'model' especifica o modelo a ser usado para a amostragem, desempenhando um papel crucial na determinação do comportamento e da saída da amostragem. |
| `add_noise` | `BOOLEAN`    | A entrada 'add_noise' permite que os usuários especifiquem se o ruído deve ser adicionado ao processo de amostragem, influenciando a diversidade e as características das amostras geradas. |
| `noise_seed` | `INT`        | A entrada 'noise_seed' fornece uma semente para a geração de ruído, garantindo reprodutibilidade e consistência no processo de amostragem ao adicionar ruído. |
| `cfg`     | `FLOAT`      | A entrada 'cfg' define a configuração para o processo de amostragem, permitindo o ajuste fino dos parâmetros e do comportamento da amostragem. |
| `positive` | `CONDITIONING` | A entrada 'positive' representa informações de condicionamento positivo, orientando o processo de amostragem para gerar amostras que se alinhem com atributos positivos especificados. |
| `negative` | `CONDITIONING` | A entrada 'negative' representa informações de condicionamento negativo, direcionando o processo de amostragem para longe da geração de amostras que exibam atributos negativos especificados. |
| `sampler` | `SAMPLER`    | A entrada 'sampler' seleciona a estratégia de amostragem específica a ser empregada, impactando diretamente a natureza e a qualidade das amostras geradas. |
| `sigmas`  | `SIGMAS`     | A entrada 'sigmas' define os níveis de ruído a serem usados no processo de amostragem, afetando a exploração do espaço de amostras e a diversidade da saída. |
| `latent_image` | `LATENT` | A entrada 'latent_image' fornece uma imagem latente inicial para o processo de amostragem, servindo como ponto de partida para a geração de amostras. |

## Saídas

| Parâmetro | Tipo de Dado | Descrição |
|-----------|--------------|-------------|
| `output`  | `LATENT`     | A saída 'output' representa o resultado principal do processo de amostragem, contendo as amostras geradas. |
| `denoised_output` | `LATENT` | A saída 'denoised_output' representa as amostras após a aplicação de um processo de remoção de ruído, potencialmente melhorando a clareza e a qualidade das amostras geradas. |

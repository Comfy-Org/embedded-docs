# SamplerCustom

O nó SamplerCustom foi projetado para fornecer um mecanismo de amostragem flexível e personalizável para diversas aplicações. Ele permite que os usuários selecionem e configurem diferentes estratégias de amostragem adaptadas às suas necessidades específicas, aumentando a adaptabilidade e eficiência do processo de amostragem.

## Entradas

| Parâmetro | Descrição | Tipo de Dados |
| --- | --- | --- |
| `modelo` | A entrada 'model' especifica o modelo a ser usado para amostragem, desempenhando um papel crucial na determinação do comportamento e do resultado da amostragem. | `MODEL` |
| `adicionar_ruído` | A entrada 'add_noise' permite que os usuários especifiquem se ruído deve ser adicionado ao processo de amostragem, influenciando a diversidade e as características das amostras geradas. | `BOOLEAN` |
| `semente_de_ruído` | A entrada 'noise_seed' fornece uma semente para a geração de ruído, garantindo reprodutibilidade e consistência no processo de amostragem ao adicionar ruído. | `INT` |
| `cfg` | A entrada 'cfg' define a configuração para o processo de amostragem, permitindo o ajuste fino dos parâmetros e do comportamento da amostragem. | `FLOAT` |
| `positivo` | A entrada 'positive' representa informações de condicionamento positivo, guiando o processo de amostragem para gerar amostras que estejam alinhadas com atributos positivos especificados. | `CONDITIONING` |
| `negativo` | A entrada 'negative' representa informações de condicionamento negativo, direcionando o processo de amostragem para longe da geração de amostras que exibam atributos negativos especificados. | `CONDITIONING` |
| `amostrador` | A entrada 'sampler' seleciona a estratégia de amostragem específica a ser empregada, impactando diretamente a natureza e a qualidade das amostras geradas. | `SAMPLER` |
| `sigmas` | A entrada 'sigmas' define os níveis de ruído a serem usados no processo de amostragem, afetando a exploração do espaço amostral e a diversidade da saída. | `SIGMAS` |
| `imagem_latente` | A entrada 'latent_image' fornece uma imagem latente inicial para o processo de amostragem, servindo como ponto de partida para a geração de amostras. | `LATENT` |

## Saídas

| Parâmetro | Descrição | Tipo de Dados |
| --- | --- | --- |
| `output` | A saída 'output' representa o resultado principal do processo de amostragem, contendo as amostras geradas. | `LATENT` |
| `denoised_output` | A saída 'denoised_output' representa as amostras após a aplicação de um processo de remoção de ruído, potencialmente melhorando a clareza e a qualidade das amostras geradas. | `LATENT` |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerCustom/pt-BR.md)

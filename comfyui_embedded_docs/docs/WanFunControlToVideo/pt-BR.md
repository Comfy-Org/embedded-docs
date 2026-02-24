> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanFunControlToVideo/pt-BR.md)

Este nó foi adicionado para dar suporte ao modelo de controle Alibaba Wan Fun para geração de vídeo, e foi incluído após [este commit](https://github.com/comfyanonymous/ComfyUI/commit/3661c833bcc41b788a7c9f0e7bc48524f8ee5f82).

- **Propósito:** Preparar as informações de condicionamento necessárias para a geração de vídeo, utilizando o modelo Wan 2.1 Fun Control.

O nó WanFunControlToVideo é uma adição ao ComfyUI projetada para dar suporte aos modelos Wan Fun Control para geração de vídeo, com o objetivo de utilizar o controle WanFun para a criação de vídeos.

Este nó serve como um ponto de preparação para informações essenciais de condicionamento e inicializa o ponto central do espaço latente, orientando o processo subsequente de geração de vídeo usando o modelo Wan 2.1 Fun. O nome do nó indica claramente sua função: ele aceita várias entradas e as converte em um formato adequado para controlar a geração de vídeo dentro da estrutura WanFun.

A posição do nó na hierarquia de nós do ComfyUI indica que ele opera nos estágios iniciais do pipeline de geração de vídeo, focando na manipulação de sinais de condicionamento antes da amostragem ou decodificação real dos quadros de vídeo.

## Entradas

| Nome do Parâmetro   | Obrigatório | Tipo de Dados      | Descrição                                                  | Valor Padrão |
|:-------------------|:-----------|:-------------------|:-----------------------------------------------------------|:-------------|
| `positive`         | Sim        | CONDITIONING       | Dados de condicionamento positivo padrão do ComfyUI, tipicamente de um nó "CLIP Text Encode". O *prompt* positivo descreve o conteúdo, assunto e estilo artístico que o usuário imagina para o vídeo gerado. | N/A  |
| `negative`         | Sim        | CONDITIONING       | Dados de condicionamento negativo padrão do ComfyUI, tipicamente gerados por um nó "CLIP Text Encode". O *prompt* negativo especifica elementos, estilos ou artefatos que o usuário deseja evitar no vídeo gerado. | N/A  |
| `vae`              | Sim        | VAE                | Requer um modelo VAE (*Variational Autoencoder*) compatível com a família de modelos Wan 2.1 Fun, usado para codificar e decodificar dados de imagem/vídeo. | N/A  |
| `width`            | Sim        | INT                | A largura desejada dos quadros de vídeo de saída em pixels, com um valor padrão de 832, valor mínimo de 16, valor máximo determinado por `nodes.MAX_RESOLUTION`, e um tamanho de passo de 16. | 832  |
| `height`           | Sim        | INT                | A altura desejada dos quadros de vídeo de saída em pixels, com um valor padrão de 480, valor mínimo de 16, valor máximo determinado por `nodes.MAX_RESOLUTION`, e um tamanho de passo de 16. | 480  |
| `length`           | Sim        | INT                | O número total de quadros no vídeo gerado, com um valor padrão de 81, valor mínimo de 1, valor máximo determinado por `nodes.MAX_RESOLUTION`, e um tamanho de passo de 4. | 81   |
| `batch_size`       | Sim        | INT                | O número de vídeos gerados em um único lote, com um valor padrão de 1, valor mínimo de 1 e valor máximo de 4096. | 1    |
| `clip_vision_output` | Não     | CLIP_VISION_OUTPUT | (Opcional) Características visuais extraídas por um modelo de visão CLIP, permitindo orientação de estilo e conteúdo visual. | None |
| `start_image`      | Não        | IMAGE              | (Opcional) Uma imagem inicial que influencia o início do vídeo gerado. | None |
| `control_video`    | Não        | IMAGE              | (Opcional) Permite que os usuários forneçam um vídeo de referência do ControlNet pré-processado que orientará o movimento e a estrutura potencial do vídeo gerado. | None |

## Saídas

| Nome do Parâmetro   | Tipo de Dados      | Descrição                                                  |
|:-------------------|:-------------------|:-----------------------------------------------------------|
| `positive`         | CONDITIONING       | Fornece dados de condicionamento positivo aprimorados, incluindo a `start_image` e o `control_video` codificados. |
| `negative`         | CONDITIONING       | Fornece dados de condicionamento negativo que também foram aprimorados, contendo o mesmo `concat_latent_image`. |
| `latent`           | LATENT             | Um dicionário contendo um tensor latente vazio com a chave "samples". |

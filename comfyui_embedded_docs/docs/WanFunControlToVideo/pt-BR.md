# WanFunControlToVideo

Este nó foi adicionado para suportar o modelo Alibaba Wan Fun Control para geração de vídeo, e foi adicionado após [este commit](https://github.com/comfyanonymous/ComfyUI/commit/3661c833bcc41b788a7c9f0e7bc48524f8ee5f82).

- **Propósito:** Preparar as informações de condicionamento necessárias para a geração de vídeo, utilizando o modelo Wan 2.1 Fun Control.

O nó WanFunControlToVideo é uma adição ao ComfyUI projetada para suportar modelos Wan Fun Control para geração de vídeo, visando utilizar o controle WanFun para criação de vídeos.

Este nó serve como um ponto de preparação para informações essenciais de condicionamento e inicializa o ponto central do espaço latente, guiando o processo subsequente de geração de vídeo usando o modelo Wan 2.1 Fun. O nome do nó indica claramente sua função: ele aceita várias entradas e as converte em um formato adequado para controlar a geração de vídeo dentro da estrutura WanFun.

A posição do nó na hierarquia de nós do ComfyUI indica que ele opera nos estágios iniciais do pipeline de geração de vídeo, focando na manipulação dos sinais de condicionamento antes da amostragem ou decodificação real dos quadros de vídeo.

## Entradas

| Nome do Parâmetro | Descrição | Obrigatório | Tipo de Dado | Valor Padrão |
| --- | --- | --- | --- | --- |
| positive | Dados de condicionamento positivo padrão do ComfyUI, normalmente de um nó "CLIP Text Encode". O prompt positivo descreve o conteúdo, assunto e estilo artístico que o usuário imagina para o vídeo gerado. | Sim | CONDITIONING | N/A |
| negative | Dados de condicionamento negativo padrão do ComfyUI, normalmente gerados por um nó "CLIP Text Encode". O prompt negativo especifica elementos, estilos ou artefatos que o usuário deseja evitar no vídeo gerado. | Sim | CONDITIONING | N/A |
| vae | Requer um modelo VAE (Autoencoder Variacional) compatível com a família de modelos Wan 2.1 Fun, usado para codificar e decodificar dados de imagem/vídeo. | Sim | VAE | N/A |
| width | A largura desejada dos quadros de vídeo de saída em pixels, com um valor padrão de 832, valor mínimo de 16, valor máximo determinado por nodes.MAX_RESOLUTION e um incremento de 16. | Sim | INT | 832 |
| height | A altura desejada dos quadros de vídeo de saída em pixels, com um valor padrão de 480, valor mínimo de 16, valor máximo determinado por nodes.MAX_RESOLUTION e um incremento de 16. | Sim | INT | 480 |
| length | O número total de quadros no vídeo gerado, com um valor padrão de 81, valor mínimo de 1, valor máximo determinado por nodes.MAX_RESOLUTION e um incremento de 4. | Sim | INT | 81 |
| batch_size | O número de vídeos gerados em um único lote, com um valor padrão de 1, valor mínimo de 1 e valor máximo de 4096. | Sim | INT | 1 |
| clip_vision_output | (Opcional) Características visuais extraídas por um modelo de visão CLIP, permitindo orientação visual de estilo e conteúdo. | Não | CLIP_VISION_OUTPUT | Nenhum |
| start_image | (Opcional) Uma imagem inicial que influencia o início do vídeo gerado. | Não | IMAGE | Nenhum |
| control_video | (Opcional) Permite que os usuários forneçam um vídeo de referência ControlNet pré-processado que guiará o movimento e a estrutura potencial do vídeo gerado. | Não | IMAGE | Nenhum |

## Saídas

| Nome do Parâmetro | Descrição | Tipo de Dado |
| --- | --- | --- |
| positive | Fornece dados de condicionamento positivo aprimorados, incluindo start_image e control_video codificados. | CONDITIONING |
| negative | Fornece dados de condicionamento negativo que também foram aprimorados, contendo o mesmo concat_latent_image. | CONDITIONING |
| latent | Um dicionário contendo um tensor latente vazio com a chave "samples". | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanFunControlToVideo/pt-BR.md)

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SvdImg2vidConditioning/pt-BR.md)

Este nó é projetado para gerar dados de condicionamento para tarefas de geração de vídeo, especificamente adaptado para uso com modelos SVD_img2vid. Ele recebe várias entradas, incluindo imagens iniciais, parâmetros de vídeo e um modelo VAE, para produzir dados de condicionamento que podem ser usados para orientar a geração de quadros de vídeo.

## Entradas

| Parâmetro             | Tipo Comfy         | Descrição |
|----------------------|--------------------|-------------|
| `clip_vision`         | `CLIP_VISION`      | Representa o modelo de visão CLIP usado para codificar características visuais da imagem inicial, desempenhando um papel crucial na compreensão do conteúdo e contexto da imagem para a geração de vídeo. |
| `init_image`          | `IMAGE`            | A imagem inicial a partir da qual o vídeo será gerado, servindo como ponto de partida para o processo de geração de vídeo. |
| `vae`                 | `VAE`              | Um modelo de Autoencoder Variacional (VAE) usado para codificar a imagem inicial em um espaço latente, facilitando a geração de quadros de vídeo coerentes e contínuos. |
| `width`               | `INT`              | A largura desejada dos quadros de vídeo a serem gerados, permitindo a personalização da resolução do vídeo. |
| `height`              | `INT`              | A altura desejada dos quadros de vídeo, permitindo o controle da proporção e resolução do vídeo. |
| `video_frames`        | `INT`              | Especifica o número de quadros a serem gerados para o vídeo, determinando a duração do vídeo. |
| `motion_bucket_id`    | `INT`              | Um identificador para categorizar o tipo de movimento a ser aplicado na geração do vídeo, auxiliando na criação de vídeos dinâmicos e envolventes. |
| `fps`                 | `INT`              | A taxa de quadros por segundo (fps) para o vídeo, influenciando a suavidade e o realismo do vídeo gerado. |
| `augmentation_level`  | `FLOAT`            | Um parâmetro que controla o nível de aumento aplicado à imagem inicial, afetando a diversidade e variabilidade dos quadros de vídeo gerados. |

## Saídas

| Parâmetro     | Tipo Comfy         | Descrição |
|---------------|--------------------|-------------|
| `positive`    | `CONDITIONING`     | Os dados de condicionamento positivo, consistindo em características codificadas e parâmetros para orientar o processo de geração de vídeo em uma direção desejada. |
| `negative`    | `CONDITIONING`     | Os dados de condicionamento negativo, fornecendo um contraste ao condicionamento positivo, que pode ser usado para evitar certos padrões ou características no vídeo gerado. |
| `latent`      | `LATENT`           | Representações latentes geradas para cada quadro do vídeo, servindo como um componente fundamental para o processo de geração de vídeo. |

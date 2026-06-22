# SVD_img2vid_Conditioning

O nó SVD_img2vid_Conditioning prepara dados de condicionamento para geração de vídeo usando o Stable Video Diffusion. Ele recebe uma imagem inicial e a processa através dos codificadores CLIP vision e VAE para criar pares de condicionamento positivo e negativo, juntamente com um espaço latente vazio para geração de vídeo. Este nó configura os parâmetros necessários para controlar movimento, taxa de quadros e níveis de aumento na geração do vídeo.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `clip_vision` | Modelo de visão CLIP para codificar a imagem de entrada | CLIP_VISION | Sim | - |
| `imagem_inicial` | Imagem inicial a ser usada como ponto de partida para a geração do vídeo | IMAGE | Sim | - |
| `vae` | Modelo VAE para codificar a imagem no espaço latente | VAE | Sim | - |
| `largura` | Largura do vídeo de saída (padrão: 1024, passo: 8) | INT | Sim | 16 a MAX_RESOLUTION |
| `altura` | Altura do vídeo de saída (padrão: 576, passo: 8) | INT | Sim | 16 a MAX_RESOLUTION |
| `quadros_de_vídeo` | Número de quadros a serem gerados no vídeo (padrão: 14) | INT | Sim | 1 a 4096 |
| `id_bucket_movimento` | Controla a quantidade de movimento no vídeo gerado (padrão: 127) | INT | Sim | 1 a 1023 |
| `fps` | Quadros por segundo para o vídeo gerado (padrão: 6) | INT | Sim | 1 a 1024 |
| `nível_de_aumento` | Nível de aumento de ruído a ser aplicado à imagem de entrada (padrão: 0.0, passo: 0.01) | FLOAT | Sim | 0.0 a 10.0 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `positive` | Dados de condicionamento positivo contendo embeddings de imagem e parâmetros de vídeo | CONDITIONING |
| `negative` | Dados de condicionamento negativo com embeddings zerados e parâmetros de vídeo | CONDITIONING |
| `latent` | Tensor de espaço latente vazio pronto para geração de vídeo | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SVD_img2vid_Conditioning/pt-BR.md)

---
**Source fingerprint (SHA-256):** `33b295b6f2e459852aaa95d9dca26c724aa2e9ad0f884a1c7760766530a00a09`

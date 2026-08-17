# HunyuanImageToVideo

O nó HunyuanImageToVideo converte imagens em representações latentes de vídeo usando o modelo de vídeo Hunyuan. Ele recebe entradas de condicionamento e imagens iniciais opcionais para gerar latentes de vídeo que podem ser processados posteriormente por modelos de geração de vídeo. O nó suporta diferentes tipos de orientação para controlar como a imagem inicial influencia o processo de geração de vídeo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `positive` | Entrada de condicionamento positiva para orientar a geração de vídeo | CONDITIONING | Sim | - |
| `vae` | Modelo VAE usado para codificar imagens no espaço latente | VAE | Sim | - |
| `width` | Largura do vídeo de saída em pixels (padrão: 848, passo: 16) | INT | Sim | 16 a MAX_RESOLUTION |
| `height` | Altura do vídeo de saída em pixels (padrão: 480, passo: 16) | INT | Sim | 16 a MAX_RESOLUTION |
| `length` | Número de quadros no vídeo de saída (padrão: 53, passo: 4) | INT | Sim | 1 a MAX_RESOLUTION |
| `batch_size` | Número de vídeos a serem gerados simultaneamente (padrão: 1) | INT | Sim | 1 a 4096 |
| `guidance_type` | Método para incorporar a imagem inicial na geração de vídeo (padrão: "v1 (concat)") | COMBO | Sim | "v1 (concat)"<br>"v2 (replace)"<br>"custom" |
| `start_image` | Imagem inicial opcional para inicializar a geração de vídeo | IMAGE | Não | - |

**Nota:** Quando `start_image` é fornecido, o nó usa diferentes métodos de orientação com base no `guidance_type` selecionado:

- "v1 (concat)": Concatena o latente da imagem com o latente do vídeo e aplica uma máscara para mesclar a imagem no vídeo
- "v2 (replace)": Substitui os quadros iniciais do vídeo pelo latente da imagem e aplica uma máscara de ruído
- "custom": Usa a imagem como latente de referência para orientação

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `positive` | Condicionamento positivo modificado com orientação de imagem aplicada quando `start_image` é fornecido | CONDITIONING |
| `latent` | Representação latente de vídeo pronta para processamento adicional por modelos de geração de vídeo | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanImageToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `0ed00d59513492f31760a18ce3b0edf10b64cad848ba52c4e47d5f61fae9accc`

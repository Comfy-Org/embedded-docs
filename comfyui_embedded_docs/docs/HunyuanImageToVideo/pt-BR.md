> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanImageToVideo/pt-BR.md)

O nó HunyuanImageToVideo converte imagens em representações latentes de vídeo usando o modelo de vídeo Hunyuan. Ele recebe entradas de condicionamento e imagens iniciais opcionais para gerar latentes de vídeo que podem ser processados posteriormente por modelos de geração de vídeo. O nó suporta diferentes tipos de orientação para controlar como a imagem inicial influencia o processo de geração de vídeo.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `positive` | CONDITIONING | Sim | - | Entrada de condicionamento positivo para orientar a geração do vídeo |
| `vae` | VAE | Sim | - | Modelo VAE usado para codificar imagens no espaço latente |
| `width` | INT | Sim | 16 a MAX_RESOLUTION | Largura do vídeo de saída em pixels (padrão: 848, passo: 16) |
| `height` | INT | Sim | 16 a MAX_RESOLUTION | Altura do vídeo de saída em pixels (padrão: 480, passo: 16) |
| `length` | INT | Sim | 1 a MAX_RESOLUTION | Número de quadros no vídeo de saída (padrão: 53, passo: 4) |
| `batch_size` | INT | Sim | 1 a 4096 | Número de vídeos a serem gerados simultaneamente (padrão: 1) |
| `guidance_type` | COMBO | Sim | "v1 (concat)"<br>"v2 (replace)"<br>"custom" | Método para incorporar a imagem inicial na geração do vídeo (padrão: "v1 (concat)") |
| `start_image` | IMAGE | Não | - | Imagem inicial opcional para inicializar a geração do vídeo |

**Observação:** Quando `start_image` é fornecida, o nó utiliza diferentes métodos de orientação com base no `guidance_type` selecionado:

- "v1 (concat)": Concatena o latente da imagem com o latente do vídeo e aplica uma máscara para mesclar a imagem no vídeo
- "v2 (replace)": Substitui os quadros iniciais do vídeo pelo latente da imagem e aplica uma máscara de ruído
- "custom": Usa a imagem como um latente de referência para orientação

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `positive` | CONDITIONING | Condicionamento positivo modificado com orientação de imagem aplicada quando start_image é fornecida |
| `latent` | LATENT | Representação latente do vídeo pronta para processamento adicional por modelos de geração de vídeo |

---
**Source fingerprint (SHA-256):** `e55e935b7955b28b04014359c544a230c51ee91e21170be1ae4f50705d3e7bba`

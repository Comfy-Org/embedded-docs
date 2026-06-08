O nó HunyuanImageToVideo converte imagens em representações latentes de vídeo usando o modelo de vídeo Hunyuan. Ele recebe entradas de condicionamento e imagens iniciais opcionais para gerar latentes de vídeo que podem ser processados posteriormente por modelos de geração de vídeo. O nó suporta diferentes tipos de orientação para controlar como a imagem inicial influencia o processo de geração de vídeo.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `positivo` | Entrada de condicionamento positivo para orientar a geração do vídeo | CONDITIONING | Sim | - |
| `vae` | Modelo VAE usado para codificar imagens no espaço latente | VAE | Sim | - |
| `largura` | Largura do vídeo de saída em pixels (padrão: 848, passo: 16) | INT | Sim | 16 a MAX_RESOLUTION |
| `altura` | Altura do vídeo de saída em pixels (padrão: 480, passo: 16) | INT | Sim | 16 a MAX_RESOLUTION |
| `duração` | Número de quadros no vídeo de saída (padrão: 53, passo: 4) | INT | Sim | 1 a MAX_RESOLUTION |
| `tamanho_do_lote` | Número de vídeos a serem gerados simultaneamente (padrão: 1) | INT | Sim | 1 a 4096 |
| `tipo_de_guia` | Método para incorporar a imagem inicial na geração do vídeo (padrão: "v1 (concat)") | COMBO | Sim | "v1 (concat)"<br>"v2 (replace)"<br>"custom" |
| `imagem_inicial` | Imagem inicial opcional para inicializar a geração do vídeo | IMAGE | Não | - |

**Observação:** Quando `start_image` é fornecida, o nó utiliza diferentes métodos de orientação com base no `guidance_type` selecionado:

- "v1 (concat)": Concatena o latente da imagem com o latente do vídeo e aplica uma máscara para mesclar a imagem no vídeo
- "v2 (replace)": Substitui os quadros iniciais do vídeo pelo latente da imagem e aplica uma máscara de ruído
- "custom": Usa a imagem como um latente de referência para orientação

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `positivo` | Condicionamento positivo modificado com orientação de imagem aplicada quando start_image é fornecida | CONDITIONING |
| `latent` | Representação latente do vídeo pronta para processamento adicional por modelos de geração de vídeo | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanImageToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `e55e935b7955b28b04014359c544a230c51ee91e21170be1ae4f50705d3e7bba`

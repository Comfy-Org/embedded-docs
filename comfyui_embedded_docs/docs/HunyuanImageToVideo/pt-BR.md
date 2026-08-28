# HunyuanImageToVideo

O nó HunyuanImageToVideo converte imagens em representações latentes de vídeo usando o modelo de vídeo Hunyuan. Ele recebe entradas de condicionamento e imagens iniciais opcionais para gerar latentes de vídeo que podem ser processados posteriormente por modelos de geração de vídeo. O nó suporta diferentes tipos de orientação para controlar como a imagem inicial influencia o processo de geração de vídeo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `positivo` | Entrada de condicionamento positivo para orientar a geração de vídeo | CONDITIONING | Sim | - |
| `vae` | Modelo VAE usado para codificar imagens no espaço latente | VAE | Sim | - |
| `largura` | Largura do vídeo de saída em pixels (padrão: 848, passo: 16) | INT | Sim | 16 a MAX_RESOLUTION |
| `altura` | Altura do vídeo de saída em pixels (padrão: 480, passo: 16) | INT | Sim | 16 a MAX_RESOLUTION |
| `duração` | Número de quadros no vídeo de saída (padrão: 53, passo: 4) | INT | Sim | 1 a MAX_RESOLUTION |
| `tamanho_do_lote` | Número de vídeos a serem gerados simultaneamente (padrão: 1) | INT | Sim | 1 a 4096 |
| `tipo_de_guia` | Método para incorporar a imagem inicial na geração de vídeo (padrão: "v1 (concat)"). Opção avançada | COMBO | Sim | "v1 (concat)"<br>"v2 (replace)"<br>"custom" |
| `imagem_inicial` | Imagem inicial opcional (ou sequência de imagens) para inicializar a geração de vídeo. Apenas os primeiros `length` quadros e os primeiros 3 canais de cor são usados | IMAGE | Não | - |

**Nota:** Quando `start_image` é fornecido, o nó usa diferentes métodos de orientação com base no `guidance_type` selecionado:

- "v1 (concat)": Concatena o latente da imagem com o latente do vídeo e aplica uma máscara para mesclar a imagem no vídeo
- "v2 (replace)": Substitui os quadros iniciais do vídeo pelo latente da imagem e aplica uma máscara de ruído
- "custom": Usa a imagem como latente de referência para orientação

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `positivo` | Condicionamento positivo modificado com orientação de imagem aplicada quando `start_image` é fornecido | CONDITIONING |
| `latente` | Representação latente de vídeo pronta para processamento posterior por modelos de geração de vídeo | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanImageToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `0ed00d59513492f31760a18ce3b0edf10b64cad848ba52c4e47d5f61fae9accc`

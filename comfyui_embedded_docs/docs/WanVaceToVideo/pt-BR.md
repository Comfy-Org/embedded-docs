O nó WanVaceToVideo processa dados de condicionamento de vídeo para modelos de geração de vídeo. Ele recebe entradas de condicionamento positivo e negativo, juntamente com dados de controle de vídeo, e prepara representações latentes para a geração de vídeo. O nó lida com redimensionamento de vídeo, mascaramento e codificação VAE para criar a estrutura de condicionamento apropriada para modelos de vídeo.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `positivo` | Entrada de condicionamento positivo para guiar a geração | CONDITIONING | Sim | - |
| `negativo` | Entrada de condicionamento negativo para guiar a geração | CONDITIONING | Sim | - |
| `vae` | Modelo VAE usado para codificar imagens e quadros de vídeo | VAE | Sim | - |
| `largura` | Largura do vídeo de saída em pixels (padrão: 832, passo: 16) | INT | Sim | 16 a MAX_RESOLUTION |
| `altura` | Altura do vídeo de saída em pixels (padrão: 480, passo: 16) | INT | Sim | 16 a MAX_RESOLUTION |
| `duração` | Número de quadros no vídeo (padrão: 81, passo: 4) | INT | Sim | 1 a MAX_RESOLUTION |
| `tamanho_do_lote` | Número de vídeos a serem gerados simultaneamente (padrão: 1) | INT | Sim | 1 a 4096 |
| `força` | Intensidade de controle para o condicionamento de vídeo (padrão: 1.0, passo: 0.01) | FLOAT | Sim | 0.0 a 1000.0 |
| `control_video` | Vídeo de entrada opcional para condicionamento de controle | IMAGE | Não | - |
| `máscaras_de_controle` | Máscaras opcionais para controlar quais partes do vídeo modificar | MASK | Não | - |
| `imagem_de_referência` | Imagem de referência opcional para condicionamento adicional | IMAGE | Não | - |

**Observação:** Quando `control_video` é fornecido, ele será redimensionado para corresponder à largura e altura especificadas. Se `control_masks` forem fornecidas, elas devem corresponder às dimensões do vídeo de controle. A `reference_image` é codificada através do VAE e anexada ao início da sequência latente quando fornecida.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `positivo` | Condicionamento positivo com dados de controle de vídeo aplicados | CONDITIONING |
| `negativo` | Condicionamento negativo com dados de controle de vídeo aplicados | CONDITIONING |
| `latent` | Tensor latente vazio pronto para geração de vídeo | LATENT |
| `trim_latent` | Número de quadros latentes a serem cortados quando a imagem de referência é usada | INT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanVaceToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `66e50a360dc99ac49cac8f3f1c8649bf4298da2934c1bd9a0bc7cfbec620b291`

# Wan22FunControlToVideo

O nó Wan22FunControlToVideo prepara representações de condicionamento e latentes para geração de vídeo usando a arquitetura do modelo de vídeo Wan. Ele processa entradas de condicionamento positivo e negativo, juntamente com imagens de referência opcionais e vídeos de controle, para criar as representações de espaço latente necessárias para a síntese de vídeo. O nó lida com o escalonamento espacial e as dimensões temporais para gerar dados de condicionamento apropriados para modelos de vídeo.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `positivo` | Entrada de condicionamento positivo para guiar a geração do vídeo | CONDITIONING | Sim | - |
| `negativo` | Entrada de condicionamento negativo para guiar a geração do vídeo | CONDITIONING | Sim | - |
| `vae` | Modelo VAE usado para codificar imagens para o espaço latente | VAE | Sim | - |
| `largura` | Largura do vídeo de saída em pixels (padrão: 832, passo: 16) | INT | Sim | 16 a MAX_RESOLUTION |
| `altura` | Altura do vídeo de saída em pixels (padrão: 480, passo: 16) | INT | Sim | 16 a MAX_RESOLUTION |
| `duração` | Número de quadros na sequência de vídeo (padrão: 81, passo: 4) | INT | Sim | 1 a MAX_RESOLUTION |
| `tamanho_do_lote` | Número de sequências de vídeo a serem geradas (padrão: 1) | INT | Sim | 1 a 4096 |
| `imagem_de_referência` | Imagem de referência opcional para fornecer orientação visual | IMAGE | Não | - |
| `vídeo_de_controle` | Vídeo de controle opcional para guiar o processo de geração | IMAGE | Não | - |

**Nota:** O parâmetro `length` é processado em blocos de 4 quadros, e o nó lida automaticamente com o escalonamento temporal para o espaço latente. Quando `ref_image` é fornecido, ele influencia o condicionamento por meio de latentes de referência. Quando `control_video` é fornecido, ele afeta diretamente a representação latente de concatenação usada no condicionamento. O parâmetro `start_image` não é exposto como uma entrada neste esquema de nó, mas é referenciado na lógica de execução.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `positivo` | Condicionamento positivo modificado com dados latentes específicos de vídeo, incluindo latente de concatenação, máscara e latentes de referência opcionais | CONDITIONING |
| `negativo` | Condicionamento negativo modificado com dados latentes específicos de vídeo, incluindo latente de concatenação, máscara e latentes de referência opcionais | CONDITIONING |
| `latent` | Tensor latente vazio com dimensões apropriadas para geração de vídeo com base no tamanho do lote, canais latentes e escalonamento espacial/temporal | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan22FunControlToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `8b24058f06aa9f779371a402c41cffc95d13ad0131d23d1438067d77755c73e2`

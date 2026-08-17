# LTXVImgToVideo

O nó LTXVImgToVideo prepara uma representação latente para gerar um vídeo a partir de uma imagem de entrada. A imagem é redimensionada para a largura e altura solicitadas, codificada com o VAE e colocada nos primeiros quadros latentes. Uma máscara de ruído é criada usando `strength` para controlar quanto do conteúdo da imagem original é preservado ou modificado, e os condicionamentos positivo e negativo são repassados inalterados.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `positive` | Dados de condicionamento positivo fornecidos como entrada e retornados inalterados. | CONDITIONING | Sim | - |
| `negative` | Dados de condicionamento negativo fornecidos como entrada e retornados inalterados. | CONDITIONING | Sim | - |
| `vae` | Modelo VAE usado para codificar a imagem de entrada no espaço latente. | VAE | Sim | - |
| `image` | Imagem de entrada que é redimensionada e codificada para formar o início do latente do vídeo. | IMAGE | Sim | - |
| `width` | Largura do vídeo de saída em pixels (padrão: 768, passo: 32). | INT | Sim | 64 a MAX_RESOLUTION |
| `height` | Altura do vídeo de saída em pixels (padrão: 512, passo: 32). | INT | Sim | 64 a MAX_RESOLUTION |
| `length` | Número de quadros no vídeo gerado (padrão: 97, passo: 8). | INT | Sim | 9 a MAX_RESOLUTION |
| `batch_size` | Número de vídeos a serem gerados em um lote latente (padrão: 1). | INT | Sim | 1 a 4096 |
| `strength` | Controla quanto do conteúdo da imagem codificada é preservado nos primeiros quadros latentes. Um valor de 1.0 preserva a imagem original completamente, enquanto 0.0 permite modificação máxima (padrão: 1.0). | FLOAT | Sim | 0.0 a 1.0 |

Nota: `MAX_RESOLUTION` é a resolução máxima permitida pela instalação do ComfyUI.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `positive` | Condicionamento positivo repassado sem modificação. | CONDITIONING |
| `negative` | Condicionamento negativo repassado sem modificação. | CONDITIONING |
| `latent` | Latente de vídeo contendo a imagem de entrada codificada no início da sequência, juntamente com uma máscara de ruído baseada em `strength`. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVImgToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `4ebc7f80b4d9ac3329e3349c7048885de22b827b5bdd102976687afd7e07a16b`

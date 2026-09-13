# LTXVCropGuides

O nó LTXVCropGuides remove dados de orientação de keyframe de um fluxo de trabalho de geração de vídeo. Ele conta os keyframes registrados no condicionamento positivo, recorta essa quantidade de quadros do final das amostras latentes e da máscara de ruído, e limpa o índice de keyframe e as entradas de atenção de orientação de ambas as entradas de condicionamento. Quando nenhum keyframe é encontrado, as entradas de condicionamento são retornadas sem alterações e o latent é repassado com um tensor de amostra clonado e sua máscara de ruído.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `positive` | A entrada de condicionamento positivo contendo informações de orientação para a geração. O número de keyframes que ela contém determina quantos quadros são recortados do latent. | CONDITIONING | Sim | - |
| `negative` | A entrada de condicionamento negativo contendo informações de orientação sobre o que evitar na geração. Seus dados de keyframe são limpos junto com o condicionamento positivo. | CONDITIONING | Sim | - |
| `latent` | A representação latente contendo amostras de imagem e dados de máscara de ruído. Quando keyframes estão presentes, os quadros do keyframe final são removidos tanto das amostras quanto da máscara de ruído. | LATENT | Sim | - |

Nota: O recorte só ocorre quando índices de keyframe são detectados no condicionamento positivo. Se nenhum keyframe for detectado, os condicionamentos positivo e negativo são retornados sem alterações, enquanto o latent ainda é retornado com um tensor de amostra clonado e uma máscara de ruído explícita (uma máscara preenchida com uns é criada se o latent de entrada não tiver nenhuma).

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `positive` | O condicionamento positivo processado com índices de keyframe e entradas de atenção de orientação limpos | CONDITIONING |
| `negative` | O condicionamento negativo processado com índices de keyframe e entradas de atenção de orientação limpos | CONDITIONING |
| `latent` | A representação latente recortada com amostras e máscara de ruído ajustadas, onde seções de keyframe foram removidas | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVCropGuides/pt-BR.md)

---
**Source fingerprint (SHA-256):** `83e08bad281902e765ec18e06144b6a5fa730be2533932daa1d4076e6390b1e1`

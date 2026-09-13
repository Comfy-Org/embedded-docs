# SamplerLCMUpscale

Este nó fornece um método de amostragem especializado que combina amostragem do Latent Consistency Model (LCM) com aumento progressivo de escala da imagem. Durante a amostragem, a imagem é ampliada passo a passo em direção a uma proporção de escala alvo usando um método de interpolação escolhido, permitindo resultados de resolução mais alta em uma única passagem de amostragem. O nó gera um objeto sampler configurado que pode ser conectado a um nó de amostragem.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `proporção_de_escala` | O fator de escala total a aplicar durante o aumento de escala. Um valor de 1.0 mantém a resolução original (padrão: 1.0) | FLOAT | Sim | 0.1 - 20.0 |
| `etapas_de_escala` | O número de etapas a usar para o processo de aumento de escala. Use -1 para cálculo automático com base no cronograma de amostragem (padrão: -1) | INT | Sim | -1 - 1000 |
| `método_de_upscale` | O método de interpolação usado para aumentar a escala da imagem em cada etapa de aumento de escala (padrão: "bislerp") | COMBO | Sim | "bislerp"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bicubic" |

`scale_ratio` e `scale_steps` são parâmetros avançados. A imagem é ampliada gradualmente do seu tamanho original até a `scale_ratio` alvo ao longo das etapas de aumento de escala. Quando `scale_steps` é -1, o número de etapas de aumento de escala é calculado automaticamente como cerca de metade do número de etapas de amostragem, com um mínimo de 2; quando um valor positivo é fornecido, o nó o ajusta internamente e o limita com base no número total de etapas de amostragem.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `sampler` | Um objeto sampler configurado que executa amostragem LCM com aumento progressivo de escala, pronto para ser usado no pipeline de amostragem | SAMPLER |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerLCMUpscale/pt-BR.md)

---
**Source fingerprint (SHA-256):** `5d6f6472fbb4d2c66a8a8b9d6dc34dcc52ac8272589fd6c29e4084d6cab3141b`

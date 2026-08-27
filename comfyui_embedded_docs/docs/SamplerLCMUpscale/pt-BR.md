# SamplerLCMUpscale

O nó SamplerLCMUpscale fornece um método de amostragem especializado que combina a amostragem do Modelo de Consistência Latente (LCM) com recursos de ampliação de imagem. Ele amplia a imagem progressivamente durante o processo de amostragem usando vários métodos de interpolação, permitindo que saídas de maior resolução sejam geradas em uma única passagem de amostragem. A saída é um objeto de amostrador configurado que pode ser conectado a um nó de amostragem.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `proporção_de_escala` | O fator de escala total a ser aplicado durante a ampliação. Um valor de 1.0 mantém a resolução original (padrão: 1.0) | FLOAT | Sim | 0.1 - 20.0 |
| `etapas_de_escala` | O número de passos a serem usados no processo de ampliação. Use -1 para cálculo automático com base no cronograma de amostragem (padrão: -1) | INT | Sim | -1 - 1000 |
| `método_de_upscale` | O método de interpolação usado para ampliar a imagem em cada passo de ampliação (padrão: "bislerp") | COMBO | Sim | "bislerp"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bicubic" |

`scale_ratio` e `scale_steps` são parâmetros avançados. A imagem é ampliada gradualmente de seu tamanho original até o `scale_ratio` alvo ao longo dos passos de ampliação. Quando `scale_steps` é -1, o número de passos de ampliação é calculado automaticamente como cerca de metade do número de passos de amostragem, com um mínimo de 2; quando um valor positivo é fornecido, o nó o ajusta internamente e o limita com base no número total de passos de amostragem.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `sampler` | Um objeto de amostrador configurado que executa a amostragem LCM com ampliação progressiva, pronto para ser usado no pipeline de amostragem | SAMPLER |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerLCMUpscale/pt-BR.md)

---
**Source fingerprint (SHA-256):** `5d6f6472fbb4d2c66a8a8b9d6dc34dcc52ac8272589fd6c29e4084d6cab3141b`

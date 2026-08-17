# SamplerLCMUpscale

O nó SamplerLCMUpscale fornece um método de amostragem especializado que combina a amostragem do Modelo de Consistência Latente (LCM) com recursos de ampliação de imagem. Ele permite ampliar imagens durante o processo de amostragem usando vários métodos de interpolação, sendo útil para gerar saídas de maior resolução mantendo a qualidade da imagem. A ampliação é aplicada gradualmente ao longo das etapas de amostragem até que o `scale_ratio` alvo seja atingido.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `scale_ratio` | O fator de escala a ser aplicado durante a ampliação (padrão: 1.0) | FLOAT | Não | 0.1 - 20.0 |
| `scale_steps` | O número de etapas a serem usadas no processo de ampliação. Use -1 para cálculo automático (padrão: -1) | INT | Não | -1 - 1000 |
| `upscale_method` | O método de interpolação usado para ampliar a imagem (padrão: bislerp) | COMBO | Sim | "bislerp"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bicubic" |

Nota: Quando `scale_steps` é definido com um valor positivo, o número efetivo de etapas de ampliação é limitado pelo número total de etapas de amostragem do amostrador.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `sampler` | Retorna um objeto sampler configurado que pode ser usado no pipeline de amostragem | SAMPLER |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerLCMUpscale/pt-BR.md)

---
**Source fingerprint (SHA-256):** `5d6f6472fbb4d2c66a8a8b9d6dc34dcc52ac8272589fd6c29e4084d6cab3141b`

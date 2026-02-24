> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerLCMUpscale/pt-BR.md)

O nó SamplerLCMUpscale fornece um método de amostragem especializado que combina a amostragem do Modelo de Consistência Latente (LCM) com capacidades de aumento de escala de imagem. Ele permite que você aumente a escala de imagens durante o processo de amostragem usando vários métodos de interpolação, sendo útil para gerar saídas de maior resolução enquanto mantém a qualidade da imagem.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `scale_ratio` | FLOAT | Não | 0.1 - 20.0 | O fator de escala a ser aplicado durante o aumento de resolução (padrão: 1.0) |
| `scale_steps` | INT | Não | -1 - 1000 | O número de etapas a ser usado para o processo de aumento de escala. Use -1 para cálculo automático (padrão: -1) |
| `upscale_method` | COMBO | Sim | "bislerp"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bicubic" | O método de interpolação usado para aumentar a escala da imagem |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `sampler` | SAMPLER | Retorna um objeto amostrador configurado que pode ser usado no pipeline de amostragem |

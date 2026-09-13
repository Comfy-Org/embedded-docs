# Comfy Cloud Z-Image Turbo Texto para Imagem [BETA]

Este nó gera uma imagem a partir de um prompt de texto usando o modelo Z-Image Turbo, que é concluído em apenas 8 etapas. A geração é executada remotamente em GPUs do Comfy Cloud e é cobrada pelo tempo de execução, o que faz desta uma das opções mais rápidas e mais baratas disponíveis aqui para iterar em ideias de imagem. Quando a geração termina, o nó baixa a imagem finalizada para uso no seu fluxo de trabalho. Este nó faz parte do conjunto de nós do Comfy Cloud, marcado como BETA: opções podem ser adicionadas ou removidas, e um fluxo de trabalho pode ser descontinuado.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt de texto descrevendo a imagem a ser gerada. Aceita entrada multilinha e é aparado antes do envio. Não pode estar vazio após a remoção de espaços. Padrão: "" (vazio). | STRING | Sim | 1 - 4096 caracteres |
| `seed` | Semente aleatória usada para controlar a reprodutibilidade da geração. Alterá-la produz uma variação diferente. Inclui uma opção de controle após a geração. Padrão: 42. | INT | Não | 0 - 18446744073709551615 |
| `aspect_ratio` | Proporção da imagem gerada. Padrão: "1:1". | COMBO | Não | "1:1"<br>"3:4"<br>"2:3"<br>"3:2"<br>"4:3"<br>"16:9"<br>"9:16"<br>"21:9" |
| `megapixels` | Orçamento total de pixels. 1.0 equivale a aproximadamente 1024x1024 em proporção quadrada. Padrão: 1.0. | FLOAT | Não | 0.1 - 16.0<br>(passo de 0.1) |

Nota: Os valores de entrada são validados antes do envio da geração. O `prompt` deve conter entre 1 e 4.096 caracteres após a remoção de espaços em branco, `aspect_ratio` deve ser uma das opções listadas, e `megapixels` deve ser informado em incrementos de 0.1.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `IMAGE` | A imagem gerada retornada como um tensor de imagem, pronta para nós adicionais de processamento ou salvamento de imagem. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyCloudZImageTurboNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `9c78bf9aca5800212d1c5a8f9581dc6c154a82220cd60a8b55ebe74111d2f542`

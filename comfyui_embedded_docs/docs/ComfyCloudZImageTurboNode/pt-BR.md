# ComfyCloudZImageTurboNode

Este nó gera uma imagem a partir de um prompt de texto usando o modelo Z-Image Turbo, que é concluído em apenas 8 etapas. A geração é executada remotamente em GPUs da Comfy Cloud e é cobrada por tempo de GPU, tornando esta uma das opções mais rápidas e baratas aqui para iterar sobre ideias de imagens. Assim que a geração é concluída, o nó baixa a imagem finalizada para uso no seu fluxo de trabalho.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
|-----------|-------------|--------------|--------------|-----------|
| `prompt` | Prompt de texto que descreve a imagem a ser gerada. Aceita entrada de múltiplas linhas e tem os espaços em branco removidos antes do envio. Não deve ficar vazio após essa remoção. | STRING | Sim | 1 - 4096 caracteres |
| `seed` | Semente aleatória usada para controlar a reprodutibilidade da geração. Alterá-la produz uma variação diferente. Inclui uma opção de controle após a geração. Padrão: 42. | INT | Não | 0 - 18446744073709551615 |
| `aspect_ratio` | Proporção de aspecto da imagem gerada. Padrão: "1:1". | COMBO | Não | "1:1"<br>"3:4"<br>"2:3"<br>"3:2"<br>"4:3"<br>"16:9"<br>"9:16"<br>"21:9" |
| `megapixels` | Orçamento total de pixels. 1.0 corresponde a cerca de 1024x1024 em uma proporção quadrada. Padrão: 1.0. | FLOAT | Não | 0.1 - 16.0<br>(incremento de 0.1) |

Nota: Os valores de entrada são validados antes de a geração ser enviada. O `prompt` deve conter entre 1 e 4096 caracteres após a remoção de espaços em branco, `aspect_ratio` deve ser uma das opções listadas e `megapixels` deve ser inserido em incrementos de 0.1.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|---------------|-------------|--------------|
| `IMAGE` | A imagem gerada retornada como um tensor de imagem, pronta para processamento adicional ou para nós de salvamento. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyCloudZImageTurboNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `9c78bf9aca5800212d1c5a8f9581dc6c154a82220cd60a8b55ebe74111d2f542`

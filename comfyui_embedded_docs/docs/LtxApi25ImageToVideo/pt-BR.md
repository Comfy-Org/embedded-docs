# LTX 2.5 Imagem para Vídeo

Este nó gera um vídeo de qualidade profissional a partir de uma imagem inicial usando um modelo LTX 2.5. Você descreve o conteúdo do vídeo com um prompt de texto, seleciona uma variante do modelo e ajusta duração, resolução, taxa de quadros e geração de áudio. Um quadro final opcional pode ser fornecido para definir o fim do vídeo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `imagem` | Primeiro quadro a ser usado no vídeo. | IMAGE | Sim | Exatamente uma imagem |
| `modelo` | Grupo de configurações do modelo. Seleciona a variante do modelo LTX 2.5 a ser usada. | COMBO | Sim | "LTX-2.5 (Fast)"<br>"LTX-2.5 (Pro)" |
| `duração` | Duração do vídeo gerado em segundos. | INT | Sim | Inteiro |
| `resolução` | Resolução do vídeo gerado. As opções disponíveis podem depender do modelo selecionado. | COMBO | Sim | "1280x720"<br>"720x1280"<br>"1920x1080"<br>"1080x1920"<br>"2560x1440"<br>"1440x2560"<br>"3840x2160"<br>"2160x3840" |
| `fps` | Taxa de quadros do vídeo gerado. | INT | Sim | Inteiro (padrão: 25) |
| `gerar_áudio` | Se deve gerar áudio para o vídeo. | BOOLEAN | Sim | True<br>False (padrão: True) |
| `prompt` | Descrição textual do conteúdo do vídeo a ser gerado. Deve ter entre 1 e 10000 caracteres. | STRING | Sim | 1 a 10000 caracteres |
| `semente` | Valor de semente para geração reproduzível. Usar a mesma semente com as mesmas configurações produz o mesmo resultado. | INT | Sim | Inteiro (padrão: 42) |
| `último_quadro` | Último quadro a ser usado no vídeo. | IMAGE | Não | Exatamente uma imagem |

**Observação:** Apenas uma imagem é suportada para `image`. Se `last_frame` for fornecido, ele também deve conter exatamente uma imagem. As opções disponíveis de `model.resolution` podem variar dependendo da variante `model` selecionada.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `video` | O vídeo gerado a partir da imagem inicial fornecida e das configurações de geração. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxApi25ImageToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `13db42e5e0d4237424b30b960ec12f5dd16808d21b85e100e5861c095b351c79`

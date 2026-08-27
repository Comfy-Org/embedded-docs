# LtxApi25ImageToVideo

Este nó gera um vídeo de qualidade profissional com base em uma imagem inicial. Você pode escolher a variante do modelo LTX 2.5, descrever o vídeo com um prompt de texto, ajustar duração, resolução, taxa de quadros e geração de áudio e, opcionalmente, fornecer um quadro final. A saída é um vídeo que começa a partir da imagem fornecida.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `imagem` | Primeiro quadro a ser usado para o vídeo. | IMAGE | Sim | Exatamente uma imagem |
| `modelo` | Grupo de configurações do modelo. Seleciona a variante do modelo LTX 2.5 a ser usada. | COMBO | Sim | "LTX-2.5 (Fast)"<br>"LTX-2.5 (Pro)" |
| `duração` | Duração do vídeo gerado em segundos. | INT | Sim | Inteiro |
| `resolução` | Resolução do vídeo gerado. As opções disponíveis podem depender do modelo selecionado. | COMBO | Sim | "1280x720"<br>"720x1280"<br>"1920x1080"<br>"1080x1920"<br>"2560x1440"<br>"1440x2560"<br>"3840x2160"<br>"2160x3840" |
| `fps` | Taxa de quadros do vídeo gerado. | INT | Sim | Inteiro (padrão: 25) |
| `gerar_áudio` | Se deve gerar áudio para o vídeo. | BOOLEAN | Sim | True<br>False |
| `prompt` | Descrição textual do conteúdo do vídeo a ser gerado. Deve ter entre 1 e 10000 caracteres. | STRING | Sim | 1 a 10000 caracteres |
| `semente` | Valor da semente para geração reproduzível. Usar a mesma semente com as mesmas configurações produz o mesmo resultado. | INT | Sim | Inteiro (padrão: 42) |
| `último_quadro` | Último quadro a ser usado para o vídeo. | IMAGE | Não | Exatamente uma imagem |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `video` | O vídeo gerado com base na imagem inicial fornecida e nas configurações de geração. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxApi25ImageToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `13db42e5e0d4237424b30b960ec12f5dd16808d21b85e100e5861c095b351c79`

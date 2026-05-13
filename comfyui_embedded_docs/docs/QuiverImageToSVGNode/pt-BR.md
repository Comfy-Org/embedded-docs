> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QuiverImageToSVGNode/pt-BR.md)

Este nó converte uma imagem raster em um gráfico vetorial escalável (SVG) usando os modelos de vetorização da Quiver AI. Ele envia a imagem para uma API externa que a processa e retorna o resultado vetorizado.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Faixa | Descrição |
|-----------|---------------|-------------|-------|-----------|
| `image` | IMAGE | Sim | N/A | Imagem de entrada para vetorizar. |
| `auto_crop` | BOOLEAN | Não | `True`<br>`False` | Cortar automaticamente para o assunto dominante. Este é um parâmetro avançado (padrão: `False`). |
| `model` | DYNAMICCOMBO | Sim | Múltiplas opções disponíveis | Modelo a ser usado para vetorização SVG. Selecionar um modelo revela parâmetros adicionais específicos para aquele modelo: `target_size` (redimensionamento quadrado alvo em pixels, padrão: 1024, faixa: 128-4096), `temperature`, `top_p` e `presence_penalty`. |
| `seed` | INT | Não | 0 a 2147483647 | Semente para determinar se o nó deve ser executado novamente; os resultados reais são não determinísticos independentemente do valor da semente. Este parâmetro possui funcionalidade "controle após gerar" (padrão: 0). |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|---------------|---------------|-----------|
| `SVG` | SVG | A saída SVG vetorizada. |

---
**Source fingerprint (SHA-256):** `4539277fd6c23aef149c44eeafca4d373cad658d85872de0883245eb4f2479e8`

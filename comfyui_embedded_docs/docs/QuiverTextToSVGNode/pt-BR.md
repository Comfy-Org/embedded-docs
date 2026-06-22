# Quiver Texto para SVG

O nó Quiver Text to SVG gera uma imagem de Vetor Gráfico Escalável (SVG) a partir de uma descrição textual usando os modelos da Quiver AI. Opcionalmente, você pode fornecer imagens de referência e instruções de estilo para orientar o processo de geração.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `prompt` | Descrição textual da saída SVG desejada. Esta é a instrução principal para o que deve ser gerado. | STRING | Sim | N/A |
| `instruções` | Orientação adicional de estilo ou formatação. Este é um parâmetro avançado e opcional. | STRING | Não | N/A |
| `imagens_de_referência` | Até 4 imagens de referência para orientar a geração. Esta é uma entrada opcional. | IMAGE | Não | 0 a 4 imagens |
| `modelo` | Modelo a ser usado para a geração do SVG. As opções disponíveis são determinadas pela API Quiver. | COMBO | Sim | `"Quiver SVG v1"`<br>`"Quiver SVG v1 Max"`<br>`"Quiver SVG v1 Preview"` |
| `semente` | Semente para determinar se o nó deve ser executado novamente; os resultados reais são não determinísticos independentemente da semente. Padrão: 0. | INT | Sim | 0 a 2147483647 |

**Nota:** A entrada `reference_images` aceita no máximo 4 imagens. Se mais forem fornecidas, o nó gerará um erro.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `SVG` | A imagem de Vetor Gráfico Escalável (SVG) gerada. | SVG |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QuiverTextToSVGNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `634758797a59e5a409424deee808e1d8b5b5852a86eac4bccd7f2634a19fb743`

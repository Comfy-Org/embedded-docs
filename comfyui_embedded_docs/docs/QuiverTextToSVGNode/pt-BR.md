# Quiver Texto para SVG

O nó Quiver Text to SVG gera uma imagem SVG (Scalable Vector Graphic) a partir de uma descrição textual usando os modelos da Quiver AI. Opcionalmente, você pode fornecer imagens de referência e instruções de estilo para orientar o processo de geração.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Descrição textual da saída SVG desejada. Esta é a instrução principal sobre o que gerar. | STRING | Sim | N/A |
| `instruções` | Orientação adicional de estilo ou formatação. Este é um parâmetro opcional e avançado. | STRING | Não | N/A |
| `imagens_de_referência` | Até 4 imagens de referência para orientar a geração. Esta é uma entrada opcional. | IMAGE | Não | 0 a 4 imagens |
| `modelo` | Modelo a ser usado para geração de SVG. Selecionar um modelo revela parâmetros adicionais específicos desse modelo: `temperature`, `top_p` e `presence_penalty`. | DYNAMIC_COMBO | Sim | `"arrow-2"`<br>`"arrow-2-telos"`<br>`"arrow-1.1"`<br>`"arrow-1.1-max"`<br>`"arrow-preview"` |
| `semente` | Semente para determinar se o nó deve ser executado novamente; os resultados reais são não determinísticos independentemente da semente. Padrão: 0. | INT | Sim | 0 a 2147483647 |
| `reasoning_effort` | Quanto raciocínio o modelo usa antes de desenhar. Níveis mais altos melhoram o detalhe e consomem mais tokens. Usado apenas pelos modelos Arrow 2 (padrão: "high"). | COMBO | Não | `"low"`<br>`"medium"`<br>`"high"`<br>`"xhigh"` |

**Nota:** A entrada `reference_images` aceita no máximo 4 imagens.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `SVG` | A imagem SVG (Scalable Vector Graphic) gerada. | SVG |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QuiverTextToSVGNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `8b6f21c26748f48eddf2eddaed785a2331a29364744edf30e86e420b0c117e49`

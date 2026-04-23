> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QuiverTextToSVGNode/pt-BR.md)

O nó Quiver Text to SVG gera uma imagem de Vetor Gráfico Escalável (SVG) a partir de uma descrição textual usando os modelos da Quiver AI. Opcionalmente, você pode fornecer imagens de referência e instruções de estilo para orientar o processo de geração.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `prompt` | STRING | Sim | N/A | Descrição textual da saída SVG desejada. Esta é a instrução principal para o que deve ser gerado. |
| `instructions` | STRING | Não | N/A | Orientação adicional de estilo ou formatação. Este é um parâmetro avançado e opcional. |
| `reference_images` | IMAGE | Não | N/A | Até 4 imagens de referência para orientar a geração. Esta é uma entrada opcional. |
| `model` | COMBO | Sim | Múltiplas opções disponíveis | Modelo a ser usado para a geração do SVG. As opções disponíveis são determinadas pela API Quiver. |
| `seed` | INT | Sim | 0 a 2147483647 | Semente para determinar se o nó deve ser executado novamente; os resultados reais são não determinísticos independentemente da semente. Padrão: 0. |

**Observação:** A entrada `reference_images` aceita no máximo 4 imagens. Se mais forem fornecidas, o nó gerará um erro.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `SVG` | SVG | A imagem de Vetor Gráfico Escalável (SVG) gerada. |
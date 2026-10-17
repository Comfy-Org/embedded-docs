# Quiver Imagem para SVG (Legado)

Este nó converte uma imagem raster em um gráfico vetorial escalável (SVG) usando os modelos de vetorização da Quiver AI. Ele envia a imagem para uma API externa, que a processa e retorna o resultado vetorizado.

**Nota:** Este nó está marcado como obsoleto no código-fonte.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `imagem` | Imagem de entrada a ser vetorizada. | IMAGE | Sim | N/A |
| `corte_automático` | Recorta automaticamente para o assunto dominante (padrão: False). | BOOLEAN | Sim | True<br>False |
| `modelo` | Modelo a ser usado para vetorização SVG. Selecionar um modelo revela parâmetros adicionais específicos desse modelo: `target_size` (destino de redimensionamento quadrado em pixels; 0 mantém o tamanho da imagem de origem, caso contrário, 128 a 4096), `temperature`, `top_p` e `presence_penalty`. | DYNAMIC_COMBO | Sim | `"arrow-2"`<br>`"arrow-2-telos"` |
| `semente` | Semente para determinar se o nó deve ser executado novamente; os resultados reais são não determinísticos independentemente do valor da semente. Este parâmetro tem a funcionalidade de "controle após gerar" (padrão: 0). | INT | Sim | 0 a 2147483647 |
| `reasoning_effort` | Quanto raciocínio o modelo gasta antes de desenhar. Níveis mais altos melhoram o detalhe e custam mais tokens. Usado apenas pelos modelos Arrow 2 (padrão: "high"). | COMBO | Não | `"low"`<br>`"medium"`<br>`"high"`<br>`"xhigh"` |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `SVG` | A saída SVG vetorizada. | SVG |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QuiverImageToSVGNode/pt-BR.md)

---
---
**Source fingerprint (SHA-256):** `196b0693328478bff21b11da87c52608e8bb57abb9bf482052782231f6d81c30`

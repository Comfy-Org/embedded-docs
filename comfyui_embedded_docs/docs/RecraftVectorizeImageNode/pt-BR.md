# Recraft Vetorizar Imagem

Gera gráficos vetoriais SVG a partir de uma imagem de entrada. Este nó converte imagens raster em formato vetorial escalável enviando cada imagem para a API Recraft e combinando os resultados em uma única saída SVG.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `image` | A imagem de entrada a ser convertida para o formato SVG. Suporta processamento em lote de várias imagens. | IMAGE | Sim | - |
| `version` | A versão do vetorizador: `v1` é a versão padrão, e `v1_pro` (Vectorizer Pro) gera SVGs mais limpos com curvas suaves, linhas retas e cantos nítidos, ideal para letras e formas intrincadas (padrão: "v1"). | COMBO | Não | "v1"<br>"v1_pro" |
| `shape_stacking` | Como as formas são empilhadas no SVG: `hierarchical` coloca as formas em camadas umas sobre as outras; `cut_out` cria formas que nunca se sobrepõem, para plotters, cortadores de vinil e serigrafia (padrão: "hierarchical"). | COMBO | Não | "hierarchical"<br>"cut_out" |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `SVG` | A saída de gráficos vetoriais gerada, combinando todas as imagens processadas em um único documento SVG. | SVG |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftVectorizeImageNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b7f8245de0597e8d3ceeef5a15b378e0903965a7e15c1825cacdf2387b278c7e`

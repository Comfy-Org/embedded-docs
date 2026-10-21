# Mirelo Text to SFX

Gere um efeito sonoro a partir de uma descrição textual com o Mirelo SFX. Descreva o som em si, não a imagem à qual ele pertence, e o nó retorna uma única faixa de áudio com a duração solicitada. Use-o para foley, ambiência, impactos e texturas musicais curtas sem filmar ou enviar vídeo.

## Entradas

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model` | Modelo a usar. Selecionar um modelo revela os parâmetros específicos dele: `prompt`, `negative_prompt`, `duration` e `seed`. | DYNAMIC_COMBO | Sim | `"sfx-2.0"` |
| `prompt` | Descreva o som, não a imagem. De 1 a 2000 caracteres. | STRING | Sim | 1 a 2000 caracteres |
| `negative_prompt` | Sons a evitar, como uma lista curta separada por vírgulas. Pode ser deixado vazio (padrão: vazio). Máximo de 1000 caracteres. | STRING | Sim | Até 1000 caracteres |
| `duration` | Duração do som em segundos. (padrão: 5.0) | FLOAT | Sim | 0.1 a 600.0 (passo 0.1) |
| `seed` | A semente para a solicitação. Os resultados são não determinísticos, portanto a mesma seed não repete um som. (padrão: 42) | INT | Sim | 0 a 4294967295 |

O nó para com um erro quando `prompt` está vazio ou tem mais de 2000 caracteres, e quando `negative_prompt` tem mais de 1000 caracteres.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
| --- | --- | --- |
| `AUDIO` | O efeito sonoro gerado, com a duração de `duration`. | AUDIO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MireloTextToSFX/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b09a9562cea636702acd9fc50feb38b272a558f8b8509da21f5fada2abd9fd48`

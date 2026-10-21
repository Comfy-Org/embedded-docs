# Krea 3 Image

Krea 3 Image edita imagens com o Krea 3, ou gera uma nova imagem a partir de um prompt de texto quando nenhuma imagem está conectada. Conecte até 8 imagens e descreva o que alterar e o que manter, referindo-se a elas no prompt como @Image1, @Image2, e assim por diante. A proporção de aspecto e a resolução definem o tamanho de saída, e o modo de raciocínio troca velocidade por um plano mais detalhado.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model` | O modelo Krea 3 a ser usado. Selecionar um modelo revela os parâmetros que ele aceita. | DYNAMIC_COMBO | Sim | `"Krea 3"` |

### Entradas do Krea 3

Estas entradas aparecem quando `model` está definido como `Krea 3`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model.images` | As imagens a serem editadas, numeradas na ordem de conexão. Cada imagem conectada conta para o limite de 8. Deixe vazio para gerar apenas a partir do texto. | IMAGE | Não | 0 a 8 imagens |
| `model.prompt` | O que alterar e o que manter. Refira-se às imagens como `@Image1`, `@Image2`, e assim por diante, ou como imagem 1, imagem 2, ... O prompt não pode ficar vazio. | STRING | Sim | - |
| `model.aspect_ratio` | A proporção de aspecto do resultado. `"auto"` segue a primeira imagem, ou o prompt quando nenhuma imagem está conectada. (padrão: `"auto"`) | COMBO | Sim | `"auto"`<br>`"1:1"`<br>`"4:5"`<br>`"3:4"`<br>`"2:3"`<br>`"9:16"`<br>`"5:4"`<br>`"4:3"`<br>`"3:2"`<br>`"16:9"`<br>`"21:9"` |
| `model.resolution` | A resolução de saída. `"2K"` leva mais tempo e produz uma imagem maior que `"1K"`. (padrão: `"2K"`) | COMBO | Sim | `"1K"`<br>`"2K"` |
| `model.thinking_mode` | Quanto trabalho o Krea 3 dedica ao planejamento da edição. `"fast"` é recomendado, enquanto `"high"` planeja edições complexas com mais detalhes e leva mais tempo. `"ultra"` gera vários candidatos e retorna o melhor; exige pelo menos uma imagem, sempre gera em 2K e não aceita `precise_edit`. (padrão: `"fast"`) | COMBO | Sim | `"fast"`<br>`"high"`<br>`"ultra"` |
| `model.precise_edit` | Mantenha tudo fora da área editada inalterado. Requer pelo menos uma imagem conectada. (padrão: False) | BOOLEAN | Sim | false<br>true |
| `model.seed` | A seed da requisição (padrão: 42). O Krea reescreve o prompt antes de gerar, então a mesma seed não repete uma imagem. | INT | Sim | 0 a 2147483647 |

Uma referência como `@Image3` só é aceita quando pelo menos três imagens estão conectadas; caso contrário, o nó gera um erro. As imagens de referência são carregadas antes de a requisição ser enviada.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `image` | A imagem gerada ou editada. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Krea3ImageNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `9e8d036f1ebca81b85e6ef42a015e7e2925bf467fa32e82180ee1b76dcc91c0b`

# MOSS-Image Layout Prompt

Constrói o prompt de layout que o MOSS-Image lê. Ele recebe os elementos desenhados no nó Create Bounding Boxes e emite um layout JSON com uma entrada por caixa: seu rótulo, sua legenda e seu retângulo no espaço de pixels da tela de destino. Defina `width` e `height` com o tamanho da imagem que você planeja gerar e, em seguida, conecte a saída à entrada de prompt do codificador de texto. Quando nenhum elemento estiver conectado, o texto do prompt é retornado sem alterações.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `prompt` | Descrição da imagem inteira. Ela se torna a legenda do layout. | STRING | Sim | - |
| `element` | Os elementos a posicionar, obtidos do nó Create Bounding Boxes. Cada caixa contribui com sua legenda; caixas de texto também contribuem com seu texto, e caixas que carregam uma paleta de cores a mantêm. | ARRAY | Sim | - |
| `width` | Largura da imagem gerada em pixels. As caixas são convertidas para essa grade de pixels, então use o tamanho da imagem que você planeja gerar (padrão: 1024). | INT | Sim | 16 a 16384 (passo 16) |
| `height` | Altura da imagem gerada em pixels. As caixas são convertidas para essa grade de pixels, então use o tamanho da imagem que você planeja gerar (padrão: 1024). | INT | Sim | 16 a 16384 (passo 16) |
| `character_boxes` | Números das caixas a rotular como personagens em vez de objetos, conforme marcado na pré-visualização do Create Bounding Boxes, por exemplo, "1, 3". Todos os números na string são lidos, então qualquer separador funciona (padrão: vazio). | STRING | Sim | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `prompt` | O prompt de layout: um objeto JSON que contém a legenda, uma entrada por caixa e o formato de coordenadas das caixas. O texto de entrada é repassado quando nenhum elemento está conectado. | STRING |

## Notas

Os retângulos das caixas chegam do Create Bounding Boxes como coordenadas normalizadas entre 0 e 1000 e são gravados no layout em pixels relativos ao centro da tela, na ordem `yxyx`. Portanto, os valores de `width` e `height` precisam corresponder à imagem que você gera; caso contrário, as caixas ficam no lugar errado.

Uma caixa que contém texto é sempre rotulada como texto, uma caixa cujo número está listado em `character_boxes` é rotulada como personagem, e todas as outras caixas são rotuladas como objeto.

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MOSSImageLayoutPrompt/pt-BR.md)

---
**Source fingerprint (SHA-256):** `da012a8d0dceaf6391110c90bd677d7929920d60fe961c00e5011b037206aa9a`

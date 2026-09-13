# Meta Muse Image Edit

Edita ou combina até 10 imagens de referência usando um prompt de texto e o modelo Muse Image da Meta. Descreva a edição desejada no prompt e, quando necessário, consulte as imagens de referência como `@Image1`, `@Image2` e assim por diante. O nó faz upload das imagens de referência, chama a API do Meta Muse Image e retorna o resultado editado como uma imagem.

## Entradas

O nó é controlado por um seletor `model`. As entradas específicas do modelo descritas abaixo aparecem quando um modelo é selecionado, e as imagens de referência que você conectar podem ser aumentadas ou reduzidas conforme necessário.

### Entradas comuns

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | Modelo a usar. | DYNAMIC_COMBO | Sim | "muse-image-1.0" |

### Entradas do muse-image-1.0

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Instruções de edição. Suporta referências no estilo `@Image1` para as imagens de entrada. Padrão: string vazia. O prompt deve conter pelo menos um caractere. | STRING | Sim | Qualquer texto com comprimento mínimo de 1 caractere |
| `aspect_ratio` | Proporção da saída. As imagens são renderizadas com cerca de 2,5 megapixels (1:1 é 1600x1600, 16:9 é 2048x1152); "auto" mantém a proporção da entrada. | COMBO | Sim | "auto"<br>"1:1"<br>"3:2"<br>"2:3"<br>"4:3"<br>"3:4"<br>"5:4"<br>"4:5"<br>"16:9"<br>"9:16"<br>"21:9"<br>"9:21"<br>"2:1"<br>"1:2" |
| `reasoning_strength` | O quanto o modelo pensa, planeja e se autorrefina antes de renderizar. | COMBO | Sim | "high"<br>"low" |
| `enable_web_search` | Permite que o modelo pesquise na web por fatos e informações em tempo real ao planejar a imagem. Padrão: true. | BOOLEAN | Sim | true ou false (padrão: true) |
| `enable_image_search` | Permite que o modelo pesquise imagens de referência ao planejar a imagem. Padrão: true. | BOOLEAN | Sim | true ou false (padrão: true) |
| `enable_shell` | Permite que o modelo execute código durante o planejamento, para layouts, gráficos e diagramas precisos; quando desativado, quantidades e alinhamento são aproximados. Padrão: true. | BOOLEAN | Sim | true ou false (padrão: true) |
| `seed` | Semente para determinar se o nó deve ser reexecutado; a API não tem semente, então os resultados reais são não determinísticos independentemente deste valor. Padrão: 42. | INT | Sim | 0 a 2147483647 (passo 1) |

### Entradas de referência

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `images` | Slot expansível: conecte de 1 a 10 imagens de referência (`image_1` a `image_10`) para editar ou combinar. Consulte-as no prompt como `@Image1`, `@Image2`, ..., numeradas na ordem de entrada; uma entrada em lote conta uma vez por imagem. | IMAGE | Sim | 1 a 10 imagens de referência |

Nota: o prompt não pode estar vazio, e cada referência `@ImageN` contida nele deve corresponder a uma das imagens conectadas na ordem de entrada (por exemplo, `@Image1` é a primeira imagem de referência conectada). Se o prompt fizer referência a um número de imagem que não está conectado, ou se mais de 10 imagens de referência forem conectadas, o nó gera um erro.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|-------------|-------------|-----------|
| `image` | A imagem editada ou combinada retornada pelo modelo Muse Image. Se a API retornar várias imagens, elas serão retornadas como um lote. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MetaMuseImageEditApi/pt-BR.md)

---
**Source fingerprint (SHA-256):** `5c009ca45199f9c70465f12d48a46b685abebd0194c3d437121b9df0636dbea7`

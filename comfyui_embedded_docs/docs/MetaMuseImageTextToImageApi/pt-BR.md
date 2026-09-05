# MetaMuseImageTextToImageApi

Meta Muse Image Text to Image gera imagens a partir de um prompt de texto usando o modelo Muse Image da Meta. O modelo raciocina sobre o prompt antes de renderizar e pode usar pesquisa na web, pesquisa de imagens e execução de código enquanto planeja a imagem. O nó chama a API Muse Image e retorna a imagem ou as imagens resultantes.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | Modelo a ser usado. | DYNAMIC_COMBO | Sim | `"muse-image-1.0"` |

Selecionar um modelo na lista mostra as configurações compatíveis com esse modelo. O único modelo disponível é `muse-image-1.0`; as configurações dele estão listadas abaixo.

### Entradas do muse-image-1.0

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt que descreve a imagem. O modelo raciocina sobre o prompt e pode usar a pesquisa integrada na web e de imagens antes de renderizar. | STRING | Sim | Texto multilinha, mínimo de 1 caractere |
| `aspect_ratio` | Proporção de aspecto da saída. As imagens são renderizadas com cerca de 2,5 megapixels (1:1 é 1600x1600, 16:9 é 2048x1152); "auto" permite que o modelo escolha a partir do prompt. | COMBO | Sim | `"auto"`<br>`"1:1"`<br>`"3:2"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"5:4"`<br>`"4:5"`<br>`"16:9"`<br>`"9:16"`<br>`"21:9"`<br>`"9:21"`<br>`"2:1"`<br>`"1:2"` |
| `reasoning_strength` | O quanto o modelo pensa, planeja e se refina antes de renderizar. | COMBO | Sim | `"high"`<br>`"low"` |
| `enable_web_search` | Permite que o modelo pesquise na web por fatos e informações em tempo real enquanto planeja a imagem. | BOOLEAN | Não | True<br>False (padrão: True) |
| `enable_image_search` | Permite que o modelo pesquise imagens de referência enquanto planeja a imagem. | BOOLEAN | Não | True<br>False (padrão: True) |
| `enable_shell` | Permite que o modelo execute código durante o planejamento, para layouts, gráficos e diagramas precisos; quando desativado, quantidades e alinhamento são aproximados. | BOOLEAN | Não | True<br>False (padrão: True) |
| `seed` | Semente para determinar se o nó deve ser executado novamente; a API não tem semente, portanto os resultados reais são não determinísticos independentemente desse valor. | INT | Sim | 0 – 2147483647 (padrão: 42) |

Nota: o prompt deve conter pelo menos um caractere. Quando `aspect_ratio` está definido como "auto", nenhum tamanho explícito é enviado à API e o modelo decide o tamanho da saída a partir do prompt. O parâmetro `seed` apenas controla quando o nó é executado novamente; ele não é enviado à API, portanto os resultados gerados são não determinísticos.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `image` | A imagem gerada retornada pela API, decodificada e fornecida como uma imagem em lote. Se a resposta da API contiver várias imagens, elas são combinadas em um único lote. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MetaMuseImageTextToImageApi/pt-BR.md)

---
**Source fingerprint (SHA-256):** `59ebd72fab3db44a35ceac723606de4eabb5fe2b690d0b701db50e0e22a9e699`

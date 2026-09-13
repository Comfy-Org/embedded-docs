# Imagem OpenRouter

Este nó gera ou edita imagens por meio do OpenRouter usando os modelos MAI-Image-2.6 da Microsoft. Ele oferece suporte à geração de imagem a partir de texto, bem como à edição guiada por imagem com até cinco imagens de referência, em sete proporções de aspecto, com resolução de 1K ou 1.5K.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | O modelo de imagem do OpenRouter usado para gerar a imagem. Selecionar um modelo revela as opções específicas do modelo listadas abaixo. | DYNAMIC_COMBO | Sim | `microsoft/mai-image-2.6`<br>`microsoft/mai-image-2.6-flash` |

### Entradas do Mai Image 2.6 e do Mai Image 2.6 Flash

Compartilhado por ambas as opções de modelo (`microsoft/mai-image-2.6` e `microsoft/mai-image-2.6-flash`), que expõem o mesmo conjunto de parâmetros.

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Descreve a imagem a ser gerada ou a edição a ser aplicada às imagens de referência. Até 20000 caracteres. Padrão: `""` (vazio). Pelo menos 1 caractere é necessário após remover espaços em branco ao redor. | STRING | Sim | 1 a 20000 caracteres |
| `aspect_ratio` | Proporção de aspecto da imagem gerada, também aplicada quando imagens de referência estão conectadas. Padrão: `"1:1"`. `"auto"` permite que o modelo escolha a proporção para geração de imagem a partir de texto (renderizada no tamanho 1.5K) e mantém a proporção de aspecto da primeira imagem de referência ao editar. | COMBO | Sim | `"1:1"`<br>`"16:9"`<br>`"9:16"`<br>`"3:2"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"auto"` |
| `resolution` | Nível de tamanho da saída. 1K tem cerca de 1 megapixel (1:1 é 1024x1024, 16:9 é 1360x768); 1.5K tem cerca de 2,3 megapixels (1:1 é 1536x1536, 16:9 é 2048x1152). Padrão: `"1K"`. Ignorado quando `aspect_ratio` é `"auto"`. | COMBO | Sim | `"1K"`<br>`"1.5K"` |
| `seed` | Semente para determinar se o nó deve ser executado novamente; a API não tem semente, então os resultados reais são não determinísticos independentemente deste valor. Padrão: `42`. | INT | Sim | 0 a 2147483647 |

### Entradas de referência

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `image_1` ... `image_5` | Slot expansível: conecte de 1 a 5 imagens de referência para edição guiada por imagem; uma entrada em lote conta uma vez por imagem. Os slots são opcionais e podem ser deixados vazios (mínimo de 0 conectados). | IMAGE | Não | 0 a 5 imagens |

**Notas:**

- No total, é suportado um máximo de 5 imagens de referência em todos os slots conectados; uma entrada em lote conta uma vez por imagem.
- O `prompt` deve conter pelo menos 1 caractere após remover espaços em branco ao redor e não pode exceder 20000 caracteres.
- As imagens de referência são enviadas como dados PNG e são limitadas a um total de 2048 x 2048 pixels.
- A configuração `aspect_ratio` é aplicada à saída mesmo quando imagens de referência estão conectadas.
- Quando `aspect_ratio` é `"auto"`, a configuração `resolution` é ignorada. Sem imagens de referência, o modelo escolhe a proporção para geração de imagem a partir de texto e renderiza no tamanho 1.5K; com imagens de referência conectadas, a proporção de aspecto da primeira imagem de referência é mantida.
- O valor de `seed` não afeta o resultado da API; ele apenas determina se o nó será executado novamente.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|-------------|-------------|-----------|
| `IMAGE` | A imagem gerada ou editada. Se o serviço retornar várias imagens, elas são combinadas em uma única saída IMAGE em lote. Um erro é gerado se nenhuma imagem for retornada ou se uma imagem retornada não puder ser decodificada. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenRouterImageNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `d201c18deccd2523041a24427996f51127ca201dfe10fad60c6f768ab79bf852`

# Grok Image Edit

O nó Grok Image Edit modifica uma imagem existente com base em um prompt de texto. Ele usa a API Grok para gerar uma ou mais imagens novas que são variações da entrada, guiadas pela sua descrição. Este nó está marcado como obsoleto.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | O modelo de IA específico a ser usado para edição de imagens. | COMBO | Sim | `"grok-imagine-image-quality"`<br>`"grok-imagine-image-pro"`<br>`"grok-imagine-image"` |
| `image` | A(s) imagem(ns) de entrada a ser(em) editada(s). | IMAGE | Sim |  |
| `prompt` | O prompt de texto usado para gerar a imagem. Texto de múltiplas linhas; deve conter pelo menos um caractere que não seja espaço em branco. | STRING | Sim |  |
| `resolution` | A resolução da imagem de saída. | COMBO | Sim | `"1K"`<br>`"2K"` |
| `number_of_images` | Número de imagens editadas a serem geradas (padrão: 1). | INT | Sim | 1 a 10 |
| `seed` | Semente para determinar se o nó deve ser executado novamente; os resultados reais são não determinísticos independentemente da semente (padrão: 0). | INT | Sim | 0 a 2147483647 |
| `proporção` | A proporção de aspecto para a imagem de saída. Permitida apenas quando várias imagens estão conectadas à entrada de imagem (padrão: "auto"). | COMBO | Não | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"9:16"`<br>`"16:9"`<br>`"9:19.5"`<br>`"19.5:9"`<br>`"9:20"`<br>`"20:9"`<br>`"1:2"`<br>`"2:1"` |

**Restrições importantes:**
- A entrada `image` suporta até 3 imagens, exceto quando se utiliza o modelo `grok-imagine-image-pro`, que suporta apenas 1 imagem de entrada.
- O parâmetro `aspect_ratio` só pode ser definido com um valor personalizado (diferente de "auto") quando várias imagens estão conectadas à entrada `image`. Definir uma proporção de aspecto personalizada com uma única imagem de entrada causará um erro.
- O `prompt` deve conter pelo menos um caractere que não seja espaço em branco.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `output` | A(s) imagem(ns) editada(s) gerada(s) pelo nó. Se mais de uma imagem for gerada, as imagens são concatenadas em um único lote. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokImageEditNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `e2ace07d10901c4e57086da8e3294a5d04e379103e9740131f5355cd4b07625d`

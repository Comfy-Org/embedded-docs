> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BeebleSwitchXImageEdit/pt-BR.md)

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BeebleSwitchXImageEdit/en.md)

## Visão Geral

Edite uma única imagem com o Beeble SwitchX. Este nó pode trocar qualquer elemento da cena (fundo, iluminação, vestuário) preservando os pixels originais do objeto. Forneça uma imagem de referência e/ou um prompt de texto para descrever a nova aparência. A resolução máxima é de aproximadamente 2,77 megapixels.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `imagem` | IMAGE | Sim | - | A imagem de origem a ser editada. |
| `prompt` | STRING | Sim | - | Uma descrição textual da nova aparência desejada (ex.: "um cavaleiro com armadura reluzente"). |
| `alpha_mode` | COMBO | Sim | `"select"`<br>`"fill"`<br>`"custom"` | Como lidar com o canal alfa. "select" usa um quadro-chave para selecionar o objeto, "fill" substitui a imagem inteira sem um canal alfa separado, "custom" usa uma máscara fornecida pelo usuário. |
| `resolução_máxima` | COMBO | Sim | `"1080p"`<br>`"720p"` | A resolução máxima para a imagem de saída. Resoluções mais altas consomem mais créditos. |
| `seed` | INT | Sim | - | Um valor de semente para reprodutibilidade. |
| `imagem_de_referência` | IMAGE | Não | - | Uma imagem de referência opcional para guiar o estilo ou a aparência dos novos elementos da cena. |

**Nota sobre `alpha_mode`:** Quando `alpha_mode` estiver definido como `"select"`, você também deve fornecer um `alpha_keyframe` (uma imagem de quadro-chave usada para selecionar o objeto). Quando definido como `"custom"`, você deve fornecer um `alpha_mask` (uma máscara criada pelo usuário). Quando definido como `"fill"`, nenhuma entrada alfa é necessária.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `imagem` | IMAGE | A imagem editada com os elementos da cena trocados. |
| `alpha` | MASK | O canal alfa usado pelo Beeble. Vazio para o modo "fill", que não possui canal alfa separado. |

---
**Source fingerprint (SHA-256):** `41f23435686626e3ade28708fcb1da192ded347b210080ee9b17834ea8b727fb`

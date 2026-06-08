Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BeebleSwitchXImageEdit/en.md)

## Visão Geral

Edite uma única imagem com o Beeble SwitchX. Este nó pode trocar qualquer elemento da cena (fundo, iluminação, vestuário) preservando os pixels originais do objeto. Forneça uma imagem de referência e/ou um prompt de texto para descrever a nova aparência. A resolução máxima é de aproximadamente 2,77 megapixels.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `imagem` | A imagem de origem a ser editada. | IMAGE | Sim | - |
| `prompt` | Uma descrição textual da nova aparência desejada (ex.: "um cavaleiro com armadura reluzente"). | STRING | Sim | - |
| `alpha_mode` | Como lidar com o canal alfa. "select" usa um quadro-chave para selecionar o objeto, "fill" substitui a imagem inteira sem um canal alfa separado, "custom" usa uma máscara fornecida pelo usuário. | COMBO | Sim | `"select"`<br>`"fill"`<br>`"custom"` |
| `resolução_máxima` | A resolução máxima para a imagem de saída. Resoluções mais altas consomem mais créditos. | COMBO | Sim | `"1080p"`<br>`"720p"` |
| `seed` | Um valor de semente para reprodutibilidade. | INT | Sim | - |
| `imagem_de_referência` | Uma imagem de referência opcional para guiar o estilo ou a aparência dos novos elementos da cena. | IMAGE | Não | - |

**Nota sobre `alpha_mode`:** Quando `alpha_mode` estiver definido como `"select"`, você também deve fornecer um `alpha_keyframe` (uma imagem de quadro-chave usada para selecionar o objeto). Quando definido como `"custom"`, você deve fornecer um `alpha_mask` (uma máscara criada pelo usuário). Quando definido como `"fill"`, nenhuma entrada alfa é necessária.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `imagem` | A imagem editada com os elementos da cena trocados. | IMAGE |
| `alpha` | O canal alfa usado pelo Beeble. Vazio para o modo "fill", que não possui canal alfa separado. | MASK |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BeebleSwitchXImageEdit/pt-BR.md)

---
**Source fingerprint (SHA-256):** `41f23435686626e3ade28708fcb1da192ded347b210080ee9b17834ea8b727fb`

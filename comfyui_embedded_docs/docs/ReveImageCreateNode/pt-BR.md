Esta documentação foi gerada por IA. Caso encontre erros ou tenha sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReveImageCreateNode/en.md)

O nó Reve Image Create gera imagens a partir de descrições textuais usando o modelo Reve AI. Ele envia um prompt de texto para a API Reve e retorna a imagem gerada. Você pode controlar a proporção da imagem e aplicar efeitos opcionais de pós-processamento, como upscaling.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `prompt` | Descrição textual da imagem desejada. Máximo de 2560 caracteres. | STRING | Sim | N/A |
| `model` | Versão do modelo e proporção a serem usados na geração. A primeira opção seleciona o modelo, e as opções subsequentes definem a proporção da imagem. | COMBO | Sim | `"reve-create@20250915"`<br>`"3:2"`<br>`"16:9"`<br>`"9:16"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"1:1"` |
| `upscale` | Ativa ou desativa a etapa de pós-processamento de upscaling. Quando ativado, você também deve selecionar um fator de upscaling. | COMBO | Não | `"disabled"`<br>`"enabled"` |
| `upscale_factor` | O fator pelo qual aumentar a resolução da imagem. Este parâmetro só fica ativo quando `upscale` está definido como `"enabled"`. | COMBO | Não | `2`<br>`3`<br>`4` |
| `remove_background` | Quando ativado, aplica uma etapa de pós-processamento de remoção de fundo à imagem gerada. | BOOLEAN | Não | N/A |
| `seed` | Um valor de semente que controla se o nó deve ser reexecutado. Nota: Os resultados são não determinísticos independentemente do valor da semente. Padrão: 0. | INT | Não | 0 a 2147483647 |

**Nota:** O parâmetro `upscale_factor` depende do parâmetro `upscale` estar definido como `"enabled"`. O parâmetro `seed` não garante saídas determinísticas.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `image` | A imagem gerada pelo modelo Reve com base no prompt de entrada. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReveImageCreateNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `56cb32ad254d39609d9795ca29f1ccba1db2c5a7ac5bb530475298306ec4ea19`

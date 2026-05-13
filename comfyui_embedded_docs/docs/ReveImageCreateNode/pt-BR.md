> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReveImageCreateNode/pt-BR.md)

Esta documentação foi gerada por IA. Caso encontre erros ou tenha sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReveImageCreateNode/en.md)

O nó Reve Image Create gera imagens a partir de descrições textuais usando o modelo Reve AI. Ele envia um prompt de texto para a API Reve e retorna a imagem gerada. Você pode controlar a proporção da imagem e aplicar efeitos opcionais de pós-processamento, como upscaling.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `prompt` | STRING | Sim | N/A | Descrição textual da imagem desejada. Máximo de 2560 caracteres. |
| `model` | COMBO | Sim | `"reve-create@20250915"`<br>`"3:2"`<br>`"16:9"`<br>`"9:16"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"1:1"` | Versão do modelo e proporção a serem usados na geração. A primeira opção seleciona o modelo, e as opções subsequentes definem a proporção da imagem. |
| `upscale` | COMBO | Não | `"disabled"`<br>`"enabled"` | Ativa ou desativa a etapa de pós-processamento de upscaling. Quando ativado, você também deve selecionar um fator de upscaling. |
| `upscale_factor` | COMBO | Não | `2`<br>`3`<br>`4` | O fator pelo qual aumentar a resolução da imagem. Este parâmetro só fica ativo quando `upscale` está definido como `"enabled"`. |
| `remove_background` | BOOLEAN | Não | N/A | Quando ativado, aplica uma etapa de pós-processamento de remoção de fundo à imagem gerada. |
| `seed` | INT | Não | 0 a 2147483647 | Um valor de semente que controla se o nó deve ser reexecutado. Nota: Os resultados são não determinísticos independentemente do valor da semente. Padrão: 0. |

**Nota:** O parâmetro `upscale_factor` depende do parâmetro `upscale` estar definido como `"enabled"`. O parâmetro `seed` não garante saídas determinísticas.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `image` | IMAGE | A imagem gerada pelo modelo Reve com base no prompt de entrada. |

---
**Source fingerprint (SHA-256):** `56cb32ad254d39609d9795ca29f1ccba1db2c5a7ac5bb530475298306ec4ea19`

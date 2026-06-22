# Reve Image Edit

O nó Reve Image Edit permite modificar uma imagem existente com base em uma descrição textual. Ele utiliza a API Reve para interpretar suas instruções e aplicar as alterações solicitadas à imagem fornecida.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `image` | A imagem a ser editada. | IMAGE | Sim | - |
| `edit_instruction` | Descrição textual de como editar a imagem. Máximo de 2560 caracteres. | STRING | Sim | - |
| `model` | Versão do modelo a ser usada para edição. | MODEL | Sim | `"reve-edit@20250915"`<br>`"reve-edit-fast@20251030"` |
| `model.aspect_ratio` | A proporção de aspecto para a imagem editada. Quando definido como "auto", a proporção de aspecto é determinada automaticamente. | COMBO | Não | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"3:2"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"1:1"` |
| `model.test_time_scaling` | Fator de escalonamento em tempo de teste para o modelo. Valores mais altos podem melhorar a qualidade, mas aumentam o tempo de processamento. | FLOAT | Não | - |
| `upscale` | Controla se deve aumentar a resolução da imagem gerada. | COMBO | Não | `"disabled"`<br>`"enabled"` |
| `upscale.upscale_factor` | O fator pelo qual aumentar a resolução da imagem quando o aumento de resolução está ativado. | FLOAT | Não | - |
| `remove_background` | Controla se deve remover o fundo da imagem gerada. | BOOLEAN | Não | - |
| `seed` | A semente controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente da semente. (padrão: 0) | INT | Não | 0 a 2147483647 |

**Nota:** O parâmetro `upscale.upscale_factor` só é relevante quando o parâmetro `upscale` está definido como `"enabled"`.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `image` | A imagem editada gerada com base na instrução. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReveImageEditNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `0a9504ae5e8b7216d309fe3ba95c014da32eadbf11cfc5701247ba5973dd98be`

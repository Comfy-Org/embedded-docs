> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReveImageEditNode/pt-BR.md)

O nó Reve Image Edit permite modificar uma imagem existente com base em uma descrição textual. Ele utiliza a API Reve para interpretar suas instruções e aplicar as alterações solicitadas à imagem fornecida.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Sim | - | A imagem a ser editada. |
| `edit_instruction` | STRING | Sim | - | Descrição textual de como editar a imagem. Máximo de 2560 caracteres. |
| `model` | MODEL | Sim | `"reve-edit@20250915"`<br>`"reve-edit-fast@20251030"` | Versão do modelo a ser usada para edição. |
| `model.aspect_ratio` | COMBO | Não | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"3:2"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"1:1"` | A proporção de aspecto para a imagem editada. Quando definido como "auto", a proporção de aspecto é determinada automaticamente. |
| `model.test_time_scaling` | FLOAT | Não | - | Fator de escalonamento em tempo de teste para o modelo. Valores mais altos podem melhorar a qualidade, mas aumentam o tempo de processamento. |
| `upscale` | COMBO | Não | `"disabled"`<br>`"enabled"` | Controla se deve aumentar a resolução da imagem gerada. |
| `upscale.upscale_factor` | FLOAT | Não | - | O fator pelo qual aumentar a resolução da imagem quando o aumento de resolução está ativado. |
| `remove_background` | BOOLEAN | Não | - | Controla se deve remover o fundo da imagem gerada. |
| `seed` | INT | Não | 0 a 2147483647 | A semente controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente da semente. (padrão: 0) |

**Nota:** O parâmetro `upscale.upscale_factor` só é relevante quando o parâmetro `upscale` está definido como `"enabled"`.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `image` | IMAGE | A imagem editada gerada com base na instrução. |

---
**Source fingerprint (SHA-256):** `0a9504ae5e8b7216d309fe3ba95c014da32eadbf11cfc5701247ba5973dd98be`

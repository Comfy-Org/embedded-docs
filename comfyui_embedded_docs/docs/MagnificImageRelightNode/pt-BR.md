# Magnific Reiluminar Imagem

O nó Magnific Image Relight ajusta a iluminação de uma imagem de entrada. Ele pode aplicar iluminação estilística com base em um prompt de texto ou transferir as características de iluminação de uma imagem de referência opcional. O nó oferece vários controles para ajustar o brilho, contraste e o clima geral da saída final.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `image` | A imagem a ser reiluminada. Exatamente uma imagem é necessária. Dimensões mínimas de 160x160 pixels. A proporção deve estar entre 1:3 e 3:1. | IMAGE | Sim | N/A |
| `prompt` | Orientação descritiva para a iluminação. Suporta notação de ênfase (1-1.4). O padrão é uma string vazia. | STRING | Não | N/A |
| `light_transfer_strength` | Intensidade da aplicação da transferência de luz. Padrão: 100. | INT | Sim | 0 a 100 |
| `style` | Preferência de saída estilística. | COMBO | Sim | `"standard"`<br>`"darker_but_realistic"`<br>`"clean"`<br>`"smooth"`<br>`"brighter"`<br>`"contrasted_n_hdr"`<br>`"just_composition"` |
| `interpolate_from_original` | Restringe a liberdade de geração para corresponder mais ao original. Padrão: False. | BOOLEAN | Sim | N/A |
| `change_background` | Modifica o fundo com base no prompt/referência. Padrão: True. | BOOLEAN | Sim | N/A |
| `preserve_details` | Mantém a textura e os detalhes finos do original. Padrão: True. | BOOLEAN | Sim | N/A |
| `advanced_settings` | Opções de ajuste fino para controle avançado de iluminação. Quando definido como `"enabled"`, parâmetros adicionais ficam disponíveis. | DYNAMICCOMBO | Sim | `"disabled"`<br>`"enabled"` |
| `reference_image` | Imagem de referência opcional para transferir a iluminação. Se fornecida, exatamente uma imagem é necessária. Dimensões mínimas de 160x160 pixels. A proporção deve estar entre 1:3 e 3:1. | IMAGE | Não | N/A |

**Nota sobre Configurações Avançadas:** Quando `advanced_settings` está definido como `"enabled"`, os seguintes parâmetros aninhados se tornam ativos:

* `whites`: Ajusta os tons mais claros na imagem. Faixa: 0 a 100. Padrão: 50.
* `blacks`: Ajusta os tons mais escuros na imagem. Faixa: 0 a 100. Padrão: 50.
* `brightness`: Ajuste geral de brilho. Faixa: 0 a 100. Padrão: 50.
* `contrast`: Ajuste de contraste. Faixa: 0 a 100. Padrão: 50.
* `saturation`: Ajuste de saturação de cor. Faixa: 0 a 100. Padrão: 50.
* `engine`: Seleção do mecanismo de processamento. Opções: `"automatic"`, `"balanced"`, `"cool"`, `"real"`, `"illusio"`, `"fairy"`, `"colorful_anime"`, `"hard_transform"`, `"softy"`.
* `transfer_light_a`: A intensidade da transferência de luz. Opções: `"automatic"`, `"low"`, `"medium"`, `"normal"`, `"high"`, `"high_on_faces"`.
* `transfer_light_b`: Também modifica a intensidade da transferência de luz. Pode ser combinado com o controle anterior para efeitos variados. Opções: `"automatic"`, `"composition"`, `"straight"`, `"smooth_in"`, `"smooth_out"`, `"smooth_both"`, `"reverse_both"`, `"soft_in"`, `"soft_out"`, `"soft_mid"`, `"style_shift"`, `"strong_shift"`.
* `fixed_generation`: Garante saída consistente com as mesmas configurações. Padrão: True.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `image` | A imagem reiluminada. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MagnificImageRelightNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `c260b7c88a267a20fdea7f436404fe96ede782bc522ab29da36e94c20f7330cd`

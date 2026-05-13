> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MagnificImageRelightNode/pt-BR.md)

O nó Magnific Image Relight ajusta a iluminação de uma imagem de entrada. Ele pode aplicar iluminação estilística com base em um prompt de texto ou transferir as características de iluminação de uma imagem de referência opcional. O nó oferece vários controles para ajustar o brilho, contraste e o clima geral da saída final.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Sim | N/A | A imagem a ser reiluminada. Exatamente uma imagem é necessária. Dimensões mínimas de 160x160 pixels. A proporção deve estar entre 1:3 e 3:1. |
| `prompt` | STRING | Não | N/A | Orientação descritiva para a iluminação. Suporta notação de ênfase (1-1.4). O padrão é uma string vazia. |
| `light_transfer_strength` | INT | Sim | 0 a 100 | Intensidade da aplicação da transferência de luz. Padrão: 100. |
| `style` | COMBO | Sim | `"standard"`<br>`"darker_but_realistic"`<br>`"clean"`<br>`"smooth"`<br>`"brighter"`<br>`"contrasted_n_hdr"`<br>`"just_composition"` | Preferência de saída estilística. |
| `interpolate_from_original` | BOOLEAN | Sim | N/A | Restringe a liberdade de geração para corresponder mais ao original. Padrão: False. |
| `change_background` | BOOLEAN | Sim | N/A | Modifica o fundo com base no prompt/referência. Padrão: True. |
| `preserve_details` | BOOLEAN | Sim | N/A | Mantém a textura e os detalhes finos do original. Padrão: True. |
| `advanced_settings` | DYNAMICCOMBO | Sim | `"disabled"`<br>`"enabled"` | Opções de ajuste fino para controle avançado de iluminação. Quando definido como `"enabled"`, parâmetros adicionais ficam disponíveis. |
| `reference_image` | IMAGE | Não | N/A | Imagem de referência opcional para transferir a iluminação. Se fornecida, exatamente uma imagem é necessária. Dimensões mínimas de 160x160 pixels. A proporção deve estar entre 1:3 e 3:1. |

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

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `image` | IMAGE | A imagem reiluminada. |

---
**Source fingerprint (SHA-256):** `c260b7c88a267a20fdea7f436404fe96ede782bc522ab29da36e94c20f7330cd`

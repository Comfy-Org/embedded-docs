# Criar Vídeo

O nó Create Video combina uma sequência de imagens em um vídeo. Você pode definir a velocidade de reprodução em quadros por segundo, opcionalmente adicionar áudio e escolher o formato de compressão, a profundidade de bits e o espaço de cores do vídeo resultante.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `images` | As imagens a partir das quais criar um vídeo. | IMAGE | Sim | - |
| `fps` | A taxa de quadros por segundo para a velocidade de reprodução do vídeo (padrão: 30.0). | FLOAT | Sim | 1.0 - 120.0 |
| `audio` | O áudio a ser adicionado ao vídeo. | AUDIO | Não | - |
| `bit_depth` | A opção `"auto"` usa 8 bits para sRGB e 10 bits para HDR e HDR PQ. As escolhas explícitas de 8 bits e 10 bits são independentes do espaço de cores. (padrão: "auto") | COMBO | Não | `"auto"`<br>8<br>10 |
| `color_space` | Espaço de cores das imagens de entrada. HDR seleciona BT.2020/HLG e HDR PQ seleciona BT.2020/PQ. (padrão: "sRGB") | COMBO | Não | `"sRGB"`<br>`"HDR"`<br>`"HDR PQ"` |
| `codec` | Opcionalmente, codifica o vídeo imediatamente. `"none"` mantém as imagens em formato de tensor; `"auto"` usa H.264. (padrão: "none") | COMBO | Não | `"none"`<br>Opções de codec de vídeo disponíveis na lista de codecs de vídeo (por exemplo, `"auto"` e outros codecs suportados) |

Observação: Quando `bit_depth` está definido como `"auto"`, o nó usa automaticamente 10 bits para os espaços de cores HDR e HDR PQ, e 8 bits para sRGB.

Observação: O parâmetro `codec` é uma opção avançada. Quando ele é deixado como `"none"`, a saída permanece em formato de tensor; selecionar qualquer outro codec codifica o vídeo imediatamente.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `output` | O vídeo gerado contendo as imagens de entrada e o áudio opcional. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `9274559caabbafbcaad47883bf017967f9685f155ea1031e66cf22ee8d0d14c3`

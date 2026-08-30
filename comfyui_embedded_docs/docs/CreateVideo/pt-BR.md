# Criar Vídeo

O nó Create Video gera um arquivo de vídeo a partir de uma sequência de imagens. Você pode definir a velocidade de reprodução em quadros por segundo, adicionar áudio opcionalmente e escolher a profundidade de bits e o espaço de cores do vídeo resultante.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `imagens` | As imagens para criar um vídeo. | IMAGE | Sim | - |
| `fps` | A velocidade de reprodução do vídeo em quadros por segundo (padrão: 30.0). | FLOAT | Sim | 1.0 - 120.0 |
| `áudio` | O áudio a ser adicionado ao vídeo. | AUDIO | Não | - |
| `bit_depth` | Auto usa 8 bits para sRGB e 10 bits para HDR. As opções explícitas de 8 bits e 10 bits são independentes do espaço de cores. (padrão: "auto") | COMBO | Não | `"auto"`<br>8<br>10 |
| `color_space` | Espaço de cores das imagens de entrada. HDR seleciona BT.2020/HLG e HDR PQ seleciona BT.2020/PQ. (padrão: "sRGB") | COMBO | Não | `"sRGB"`<br>`"HDR"`<br>`"HDR PQ"` |

Nota: Quando `bit_depth` está definido como "auto", o nó usa 10 bits para os espaços de cores HDR e HDR PQ, e 8 bits para sRGB.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `output` | O vídeo gerado contendo as imagens de entrada e o áudio opcional. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `2fa73f38b0609de4159e557b6abe73652c5bebab9d34ffdda743b0eac6049f13`

# Imagem para Vídeo ByteDance

O nó ByteDance Image to Video gera vídeos usando modelos ByteDance por meio de uma API com base em uma imagem de entrada e um prompt de texto. Ele utiliza um quadro inicial da imagem e cria uma sequência de vídeo que segue a descrição fornecida. O nó oferece várias opções de personalização para resolução do vídeo, proporção de aspecto, duração e outros parâmetros de geração.

**Nota:** A BytePlus descontinua o modelo Seedance 1.5 Pro em 11 de novembro de 2026, então este nó não o oferece mais e os fluxos salvos com ele param de funcionar. Use `seedance-1-0-pro-250528`, `seedance-1-0-pro-fast-251015` ou o [nó parceiro Seedance 2.5](https://docs.comfy.org/pt-BR/tutorials/partner-nodes/bytedance/seedance-2-5).

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `modelo` | O modelo ByteDance a ser usado para geração de vídeo (padrão: `"seedance-1-0-pro-fast-251015"`). | COMBO | Sim | `"seedance-1-0-pro-250528"`<br>`"seedance-1-0-pro-fast-251015"` |
| `prompt` | O prompt de texto usado para gerar o vídeo. Deve ter pelo menos 1 caractere após a remoção de espaços em branco nas extremidades. | STRING | Sim | - |
| `imagem` | Primeiro quadro a ser usado para o vídeo. Deve ter entre 300x300 e 6000x6000 pixels, com proporção de aspecto entre 0,4 e 2,5. | IMAGE | Sim | - |
| `resolução` | A resolução do vídeo de saída. | COMBO | Sim | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `proporção` | A proporção de aspecto do vídeo de saída. | COMBO | Sim | `"adaptive"`<br>`"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"` |
| `duração` | A duração do vídeo de saída em segundos (padrão: 5). | INT | Sim | 3 - 12 |
| `semente` | Semente a ser usada para a geração (padrão: 0). | INT | Não | 0 - 2147483647 |
| `câmera fixa` | Especifica se a câmera deve ser fixada. A plataforma acrescenta uma instrução para fixar a câmera ao seu prompt, mas não garante o efeito real (padrão: False). | BOOLEAN | Não | `False`<br>`True` |
| `marca d'água` | Se deve adicionar uma marca d'água "gerado por IA" ao vídeo (padrão: False). | BOOLEAN | Não | `False`<br>`True` |
| `generate_audio` | Adiciona uma faixa de áudio gerada por IA. Os modelos restantes ignoram esta entrada (padrão: False). | BOOLEAN | Não | `False`<br>`True` |

**Nota:** o prompt não deve conter as seguintes palavras (sem diferenciar maiúsculas de minúsculas): `resolution`, `ratio`, `duration`, `seed`, `camerafixed`, `watermark`. Esses parâmetros são definidos por meio de suas entradas dedicadas.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `output` | O arquivo de vídeo gerado com base na imagem de entrada e nos parâmetros do prompt. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceImageToVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `9f4ad18642533689f9c664f2ca6a4ce8e92c8698754cdf9b6bb2d2735bc80415`

# LTXV Texto para Vídeo

O nó LTXV Text To Video gera vídeos de qualidade profissional a partir de uma descrição em texto. Ele se conecta a uma API externa para criar vídeos com duração, resolução e taxa de quadros personalizáveis. Você também pode optar por incluir áudio gerado por IA no vídeo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `model` | O modelo de IA a ser usado para a geração de vídeos. "LTX-2 (Pro)" oferece maior qualidade, enquanto "LTX-2 (Fast)" é otimizado para velocidade. | COMBO | Sim | `"LTX-2 (Pro)"`<br>`"LTX-2 (Fast)"` |
| `prompt` | A descrição em texto que a IA usará para gerar o vídeo. Este campo aceita várias linhas de texto. | STRING | Sim | - |
| `duration` | A duração do vídeo gerado em segundos (padrão: 8). | COMBO | Sim | `6`<br>`8`<br>`10`<br>`12`<br>`14`<br>`16`<br>`18`<br>`20` |
| `resolution` | As dimensões em pixels (largura x altura) do vídeo de saída. | COMBO | Sim | `"1920x1080"`<br>`"2560x1440"`<br>`"3840x2160"` |
| `fps` | Os quadros por segundo do vídeo (padrão: 25). | COMBO | Sim | `25`<br>`50` |
| `generate_audio` | Quando verdadeiro, o vídeo gerado incluirá áudio gerado por IA que combina com a cena (padrão: False). | BOOLEAN | Não | `True`<br>`False` |

**Restrições importantes:**

* O `prompt` deve ter entre 1 e 10.000 caracteres.
* Se você selecionar uma `duration` maior que 10 segundos, também deverá usar o modelo `"LTX-2 (Fast)"`, a resolução `"1920x1080"` e um `fps` de `25`. Essa combinação é obrigatória para vídeos mais longos.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `output` | O arquivo de vídeo gerado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxvApiTextToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `8cf7409e46bb92abdff8a12e0d4ab49d67bb70e66c0c9074c9af99d1cf250df8`

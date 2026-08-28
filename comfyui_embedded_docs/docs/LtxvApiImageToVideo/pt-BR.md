# LTXV Imagem para Vídeo

O nó LTXV Image To Video gera um vídeo de qualidade profissional a partir de uma única imagem inicial. Ele usa uma API externa para criar uma sequência de vídeo com base no seu prompt de texto, permitindo personalizar a duração, a resolução e a taxa de quadros.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `image` | Primeiro quadro a ser usado no vídeo. | IMAGE | Sim | - |
| `model` | O modelo de IA a ser usado para a geração de vídeo. O modelo "Pro" é otimizado para qualidade, enquanto o modelo "Fast" é otimizado para velocidade. | COMBO | Sim | `"LTX-2 (Pro)"`<br>`"LTX-2 (Fast)"` |
| `prompt` | Uma descrição em texto que orienta o conteúdo e o movimento do vídeo gerado (padrão: vazio). | STRING | Sim | - |
| `duration` | A duração do vídeo em segundos (padrão: 8). | COMBO | Sim | `6`<br>`8`<br>`10`<br>`12`<br>`14`<br>`16`<br>`18`<br>`20` |
| `resolution` | A resolução de saída do vídeo gerado. | COMBO | Sim | `"1920x1080"`<br>`"2560x1440"`<br>`"3840x2160"` |
| `fps` | Os quadros por segundo do vídeo (padrão: 25). | COMBO | Sim | `25`<br>`50` |
| `generate_audio` | Quando verdadeiro, o vídeo gerado incluirá áudio gerado por IA correspondente à cena (padrão: Falso). | BOOLEAN | Não | - |

**Restrições importantes:**

* A entrada `image` deve conter exatamente uma imagem.
* O `prompt` deve ter entre 1 e 10.000 caracteres.
* Se você selecionar uma `duration` maior que 10 segundos, deverá usar o modelo **"LTX-2 (Fast)"**, a resolução **"1920x1080"** e **25** FPS. Essa combinação é necessária para vídeos mais longos.

**Observação:** Este nó está marcado como obsoleto.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `video` | O arquivo de vídeo gerado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxvApiImageToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `fa3928262e59105718b6ed97ddc8d2801e540b6b0c142541d92525dd75540cc7`

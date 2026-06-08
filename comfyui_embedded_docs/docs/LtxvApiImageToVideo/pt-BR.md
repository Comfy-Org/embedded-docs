Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxvApiImageToVideo/en.md)

O nó LTXV Image To Video gera um vídeo de qualidade profissional a partir de uma única imagem inicial. Ele usa uma API externa para criar uma sequência de vídeo com base no seu prompt de texto, permitindo personalizar a duração, resolução e taxa de quadros.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `image` | Primeiro quadro a ser usado para o vídeo. | IMAGE | Sim | - |
| `model` | O modelo de IA a ser usado para geração de vídeo. O modelo "Fast" é otimizado para velocidade, enquanto o modelo "Quality" prioriza a fidelidade visual. | COMBO | Sim | `"LTX-2 (Fast)"`<br>`"LTX-2 (Quality)"` |
| `prompt` | Uma descrição textual que orienta o conteúdo e o movimento do vídeo gerado. | STRING | Sim | - |
| `duration` | A duração do vídeo em segundos (padrão: 8). | COMBO | Sim | `6`<br>`8`<br>`10`<br>`12`<br>`14`<br>`16`<br>`18`<br>`20` |
| `resolution` | A resolução de saída do vídeo gerado. | COMBO | Sim | `"1920x1080"`<br>`"2560x1440"`<br>`"3840x2160"` |
| `fps` | Os quadros por segundo do vídeo (padrão: 25). | COMBO | Sim | `25`<br>`50` |
| `generate_audio` | Quando verdadeiro, o vídeo gerado incluirá áudio gerado por IA correspondente à cena (padrão: Falso). | BOOLEAN | Não | - |

**Restrições Importantes:**

* A entrada `image` deve conter exatamente uma imagem.
* O `prompt` deve ter entre 1 e 10.000 caracteres.
* Se você selecionar uma `duration` maior que 10 segundos, deverá usar o modelo **"LTX-2 (Fast)"**, resolução **"1920x1080"** e **25** FPS. Essa combinação é necessária para vídeos mais longos.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `video` | O arquivo de vídeo gerado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxvApiImageToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `af891b45997173c3210d3de4f7b6bd05b14e9d3bf8a94dcb2c1ce08038b7d99d`

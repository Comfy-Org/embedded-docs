> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxvApiImageToVideo/pt-BR.md)

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxvApiImageToVideo/en.md)

O nó LTXV Image To Video gera um vídeo de qualidade profissional a partir de uma única imagem inicial. Ele usa uma API externa para criar uma sequência de vídeo com base no seu prompt de texto, permitindo personalizar a duração, resolução e taxa de quadros.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `image` | IMAGE | Sim | - | Primeiro quadro a ser usado para o vídeo. |
| `model` | COMBO | Sim | `"LTX-2 (Fast)"`<br>`"LTX-2 (Quality)"` | O modelo de IA a ser usado para geração de vídeo. O modelo "Fast" é otimizado para velocidade, enquanto o modelo "Quality" prioriza a fidelidade visual. |
| `prompt` | STRING | Sim | - | Uma descrição textual que orienta o conteúdo e o movimento do vídeo gerado. |
| `duration` | COMBO | Sim | `6`<br>`8`<br>`10`<br>`12`<br>`14`<br>`16`<br>`18`<br>`20` | A duração do vídeo em segundos (padrão: 8). |
| `resolution` | COMBO | Sim | `"1920x1080"`<br>`"2560x1440"`<br>`"3840x2160"` | A resolução de saída do vídeo gerado. |
| `fps` | COMBO | Sim | `25`<br>`50` | Os quadros por segundo do vídeo (padrão: 25). |
| `generate_audio` | BOOLEAN | Não | - | Quando verdadeiro, o vídeo gerado incluirá áudio gerado por IA correspondente à cena (padrão: Falso). |

**Restrições Importantes:**

* A entrada `image` deve conter exatamente uma imagem.
* O `prompt` deve ter entre 1 e 10.000 caracteres.
* Se você selecionar uma `duration` maior que 10 segundos, deverá usar o modelo **"LTX-2 (Fast)"**, resolução **"1920x1080"** e **25** FPS. Essa combinação é necessária para vídeos mais longos.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `video` | VIDEO | O arquivo de vídeo gerado. |

---
**Source fingerprint (SHA-256):** `af891b45997173c3210d3de4f7b6bd05b14e9d3bf8a94dcb2c1ce08038b7d99d`

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxvApiImageToVideo/pt-BR.md)

O nó LTXV Image To Video gera um vídeo de qualidade profissional a partir de uma única imagem inicial. Ele utiliza uma API externa para criar uma sequência de vídeo com base no seu prompt de texto, permitindo personalizar a duração, resolução e taxa de quadros.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Sim | - | Primeiro quadro a ser usado para o vídeo. |
| `model` | COMBO | Sim | `"LTX-2 (Fast)"`<br>`"LTX-2 (Quality)"` | O modelo de IA a ser usado para a geração do vídeo. O modelo "Fast" é otimizado para velocidade, enquanto o modelo "Quality" prioriza a fidelidade visual. |
| `prompt` | STRING | Sim | - | Uma descrição textual que orienta o conteúdo e o movimento do vídeo gerado. |
| `duration` | COMBO | Sim | `6`<br>`8`<br>`10`<br>`12`<br>`14`<br>`16`<br>`18`<br>`20` | A duração do vídeo em segundos (padrão: 8). |
| `resolution` | COMBO | Sim | `"1920x1080"`<br>`"2560x1440"`<br>`"3840x2160"` | A resolução de saída do vídeo gerado. |
| `fps` | COMBO | Sim | `25`<br>`50` | A taxa de quadros por segundo para o vídeo (padrão: 25). |
| `generate_audio` | BOOLEAN | Não | - | Quando verdadeiro, o vídeo gerado incluirá áudio gerado por IA que combina com a cena (padrão: Falso). |

**Restrições Importantes:**

* A entrada `image` deve conter exatamente uma imagem.
* O `prompt` deve ter entre 1 e 10.000 caracteres.
* Se você selecionar uma `duration` maior que 10 segundos, deverá usar o modelo **"LTX-2 (Fast)"**, a resolução **"1920x1080"** e **25** FPS. Esta combinação é obrigatória para vídeos mais longos.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `video` | VIDEO | O arquivo de vídeo gerado. |

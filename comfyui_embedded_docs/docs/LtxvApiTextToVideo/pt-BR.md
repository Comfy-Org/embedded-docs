> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxvApiTextToVideo/pt-BR.md)

O nó LTXV Text To Video gera vídeos de qualidade profissional a partir de uma descrição textual. Ele se conecta a uma API externa para criar vídeos com duração, resolução e taxa de quadros personalizáveis. Você também pode optar por adicionar áudio gerado por IA ao vídeo.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Sim | `"LTX-2 (Fast)"`<br>`"LTX-2 (Quality)"`<br>`"LTX-2 (Turbo)"` | O modelo de IA a ser usado para a geração do vídeo. Os modelos disponíveis são mapeados a partir do `MODELS_MAP` do código-fonte. |
| `prompt` | STRING | Sim | - | A descrição textual que a IA usará para gerar o vídeo. Este campo suporta múltiplas linhas de texto. |
| `duration` | COMBO | Sim | `6`<br>`8`<br>`10`<br>`12`<br>`14`<br>`16`<br>`18`<br>`20` | A duração do vídeo gerado em segundos (padrão: 8). |
| `resolution` | COMBO | Sim | `"1920x1080"`<br>`"2560x1440"`<br>`"3840x2160"` | As dimensões em pixels (largura x altura) do vídeo de saída. |
| `fps` | COMBO | Sim | `25`<br>`50` | A taxa de quadros por segundo para o vídeo (padrão: 25). |
| `generate_audio` | BOOLEAN | Não | - | Quando ativado, o vídeo gerado incluirá áudio gerado por IA que combina com a cena (padrão: Falso). |

**Restrições Importantes:**

* O `prompt` deve ter entre 1 e 10.000 caracteres.
* Se você selecionar uma `duration` maior que 10 segundos, também deverá usar o modelo `"LTX-2 (Fast)"`, uma resolução de `"1920x1080"` e um `fps` de `25`. Esta combinação é obrigatória para vídeos mais longos.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `output` | VIDEO | O arquivo de vídeo gerado. |

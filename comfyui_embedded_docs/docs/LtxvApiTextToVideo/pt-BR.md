Este é um nó de Texto para Vídeo LTXV que gera vídeos com qualidade profissional a partir de uma descrição textual. Ele se conecta a uma API externa para criar vídeos com duração, resolução e taxa de quadros personalizáveis. Você também pode optar por adicionar áudio gerado por IA ao vídeo.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo de IA a ser usado para geração de vídeo. Os modelos disponíveis são mapeados a partir do `MODELS_MAP` do código-fonte. | COMBO | Sim | `"LTX-2 (Rápido)"`<br>`"LTX-2 (Qualidade)"`<br>`"LTX-2 (Turbo)"` |
| `prompt` | A descrição textual que a IA usará para gerar o vídeo. Este campo suporta múltiplas linhas de texto. | STRING | Sim | - |
| `duração` | A duração do vídeo gerado em segundos (padrão: 8). | COMBO | Sim | `6`<br>`8`<br>`10`<br>`12`<br>`14`<br>`16`<br>`18`<br>`20` |
| `resolução` | As dimensões em pixels (largura x altura) do vídeo de saída. | COMBO | Sim | `"1920x1080"`<br>`"2560x1440"`<br>`"3840x2160"` |
| `fps` | Os quadros por segundo do vídeo (padrão: 25). | COMBO | Sim | `25`<br>`50` |
| `gerar_áudio` | Quando ativado, o vídeo gerado incluirá áudio gerado por IA que corresponde à cena (padrão: Falso). | BOOLEAN | Não | - |

**Restrições Importantes:**

* O `prompt` deve ter entre 1 e 10.000 caracteres.
* Se você selecionar uma `duration` maior que 10 segundos, também deverá usar o modelo `"LTX-2 (Rápido)"`, uma resolução de `"1920x1080"` e um `fps` de `25`. Esta combinação é necessária para vídeos mais longos.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `output` | O arquivo de vídeo gerado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxvApiTextToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `a0c16995a07d879113bd3ca8fea64be414feee96bd8293a3e7737ede7d30e11d`

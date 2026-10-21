# Mirelo Video to SFX

Gere efeitos sonoros que acompanham um vídeo com o Mirelo SFX. O clipe é enviado, o modelo acompanha a ação na tela e retorna uma mixagem de efeitos sonoros, além de uma faixa de fala separada com o diálogo extraído da trilha sonora. Use-o para adicionar foley, ambiência e impactos a clipes silenciosos ou parcialmente silenciosos.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model` | Modelo a usar. Selecionar um modelo revela os parâmetros específicos dele: `video`, `audio`, `prompt`, `negative_prompt`, `preserve_speech` e `seed`. | DYNAMIC_COMBO | Sim | `"sfx-2.0"` |
| `video` | O vídeo para o qual gerar som. O som é gerado para o clipe inteiro, de 1 a 600 segundos. | VIDEO | Sim | 1 a 600 segundos |
| `audio` | Faixa de diálogo a usar em vez da trilha sonora do próprio vídeo para `preserve_speech` e para a saída `speech`. Deixe desconectada para usar o som embutido no vídeo. | AUDIO | Não | - |
| `prompt` | Como o som deve ser. Pode ser deixado vazio (padrão: vazio) porque o modelo descreve o vídeo por conta própria, e nem sempre segue o prompt. Máximo de 2000 caracteres. | STRING | Sim | Até 2000 caracteres |
| `negative_prompt` | Sons a evitar, como uma lista curta separada por vírgulas. Pode ser deixado vazio (padrão: vazio). Máximo de 1000 caracteres. | STRING | Sim | Até 1000 caracteres |
| `preserve_speech` | Manter o diálogo mixado sob o som gerado. Desligado retorna apenas efeitos sonoros. (padrão: True) | BOOLEAN | Sim | false<br>true |
| `seed` | A seed para a requisição. Os resultados são não determinísticos, portanto a mesma seed não repete um clipe. (padrão: 42) | INT | Sim | 0 a 4294967295 |

O nó para com um erro quando o clipe tem menos de 1 segundo ou mais de 600 segundos. Uma faixa `audio` conectada define o diálogo que `preserve_speech` mantém e que a saída `speech` separa; sem uma, o diálogo vem da trilha sonora do próprio vídeo.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `audio` | A mixagem de efeitos sonoros para o clipe, com o diálogo mixado sob ela quando `preserve_speech` está ativado. | AUDIO |
| `speech` | O diálogo separado da trilha sonora. Silencioso, com a mesma taxa de amostragem de `audio`, quando nenhuma fala é encontrada ou a separação de fala não retorna nada. | AUDIO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MireloVideoToSFX/pt-BR.md)

---
**Source fingerprint (SHA-256):** `fa09525e6c9b10412823e358652220850fbc7109d81cc207d31ffa8921956495`

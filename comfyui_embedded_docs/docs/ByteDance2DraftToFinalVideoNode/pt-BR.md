# ByteDance Seedance 2.5 Rascunho para Vídeo Final

Este nó renderiza o vídeo final de um Seedance 2.5 Draft em 1080p ou 4k. O 4k está disponível para todas as contas. Um draft é uma pré-visualização rápida em 480p: em um nó de vídeo Seedance 2.5 (texto para vídeo, primeiro-último quadro para vídeo ou referência para vídeo), defina `model` como `Seedance 2.5 Draft`, execute-o e conecte sua saída `draft_task_id` aqui. O final mantém a cena e o movimento do draft e reutiliza o prompt, as referências, a duração, a proporção e a configuração de áudio que produziram o draft.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `draft_task_id` | A saída `draft_task_id` de um nó Seedance 2.5 executado com o modelo Seedance 2.5 Draft, ou um ID de tarefa de draft colado. Ao executar novamente o nó produtor, defina seu controle de seed como fixo, caso contrário, a próxima execução gerará um novo draft em vez de reutilizar o que você revisou. | STRING | Sim | - |
| `watermark` | Se deve adicionar uma marca d'água ao vídeo. O padrão é False. Esta é uma configuração avançada. | BOOLEAN | Não | True ou False |
| `resolution` | Resolução do vídeo final. `"4k"` está disponível para todas as contas; use exatamente o valor em minúsculas `"4k"`. Padrão: `"1080p"`. | COMBO | Não | `"1080p"`<br>`"4k"` |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `video` | O vídeo final renderizado, baixado do provedor assim que a tarefa de renderização for concluída. | VIDEO |

**Nota:** Um draft pode ser renderizado por 7 dias após sua criação. O ID da tarefa de draft identifica o draft por conta própria, portanto, o prompt, as referências, a duração, a proporção e a configuração de áudio não precisam ser passados novamente.

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2DraftToFinalVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `757f1330775554d654012daa83880c3a2fbcee5b0a9efe0a2d2650f940962be6`

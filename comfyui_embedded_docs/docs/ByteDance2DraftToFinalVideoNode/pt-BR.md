# ByteDance Seedance 2.5 Draft to Final Video

Este nó renderiza o vídeo final em 1080p de um rascunho do Seedance 2.5. Um rascunho é uma prévia rápida em 480p: em um nó de vídeo Seedance 2.5 (texto para vídeo, primeiro e último quadro para vídeo ou referência para vídeo), defina `model` como `Seedance 2.5 Draft`, execute-o e conecte sua saída `draft_task_id` aqui. O resultado final mantém a cena e o movimento do rascunho e reutiliza o prompt, as referências, a duração, a proporção de aspecto e a configuração de áudio que produziram o rascunho.

## Entradas

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `draft_task_id` | A saída `draft_task_id` de um nó Seedance 2.5 executado com o modelo `Seedance 2.5 Draft`, ou um ID de tarefa de rascunho colado. Ao executar novamente o nó produtor, defina seu controle de seed como fixo; caso contrário, a próxima execução gerará um novo rascunho em vez de reutilizar o que você revisou. | STRING | Sim | - |
| `watermark` | Define se deve ser adicionada uma marca d'água ao vídeo. O padrão é False. Esta é uma configuração avançada. | BOOLEAN | Não | True / False |

## Saídas

| Nome da saída | Descrição | Tipo de dados |
| --- | --- | --- |
| `video` | O vídeo final renderizado em 1080p, baixado do provedor assim que a tarefa de renderização for concluída. | VIDEO |

**Nota:** Um rascunho pode ser renderizado por 7 dias após sua criação. O ID da tarefa do rascunho identifica o rascunho por si só, então o prompt, as referências, a duração, a proporção de aspecto e a configuração de áudio não precisam ser passados novamente.

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2DraftToFinalVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `c9a607826915f09ec199748964010a00a239b5efab3647a3b97fdceee6b04cde`

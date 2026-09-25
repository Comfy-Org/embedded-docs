# ByteDance Seedance 2.5 Draft to Final Video

Este nó renderiza o vídeo final em 1080p de um Seedance 2.5 Draft. Um Draft é uma prévia rápida em 480p: em um nó de vídeo do Seedance 2.5 (texto para vídeo, primeiro-último frame para vídeo ou referência para vídeo), defina `model` como `Seedance 2.5 Draft`, execute-o e conecte sua saída `draft_task_id` aqui. O vídeo final mantém a cena e o movimento do Draft e reutiliza o prompt, as referências, a duração, a proporção de tela e a configuração de áudio que produziram o Draft.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `draft_task_id` | A saída `draft_task_id` de um nó Seedance 2.5 executado com o modelo Seedance 2.5 Draft, ou um ID de tarefa de Draft colado. Defina o controle de seed desse nó como fixo; caso contrário, a próxima execução gerará um novo Draft em vez de reutilizar o que você revisou. | STRING | Sim | - |
| `watermark` | Se deve adicionar uma marca d'água ao vídeo. O padrão é False. Esta é uma configuração avançada. | BOOLEAN | Não | True / False |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `video` | O vídeo final renderizado em 1080p, baixado do provedor quando a tarefa de renderização é concluída. | VIDEO |

**Nota:** Um Draft pode ser renderizado por 7 dias após sua criação. O ID da tarefa de Draft identifica o Draft por si só, então o prompt, as referências, a duração, a proporção de tela e a configuração de áudio não precisam ser passados novamente.

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2DraftToFinalVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `c9a607826915f09ec199748964010a00a239b5efab3647a3b97fdceee6b04cde`

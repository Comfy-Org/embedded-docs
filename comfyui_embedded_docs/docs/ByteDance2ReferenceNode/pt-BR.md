> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2ReferenceNode/pt-BR.md)

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2ReferenceNode/en.md)

O nó ByteDance Seedance 2.0 Reference to Video usa o modelo de IA Seedance 2.0 para criar, editar ou estender vídeos com base no seu prompt de texto e nos materiais de referência fornecidos. Ele pode usar imagens, vídeos e áudio como referências para guiar o processo de geração, suportando tarefas como edição e extensão de vídeos.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Faixa | Descrição |
|-----------|---------------|-------------|-------|-----------|
| `model` | COMBO | Sim | `"Seedance 2.0"`<br>`"Seedance 2.0 Fast"` | O modelo de IA a ser usado. Seedance 2.0 é para máxima qualidade, enquanto Seedance 2.0 Fast é otimizado para velocidade. Selecionar um modelo revela entradas obrigatórias adicionais para `prompt`, `resolution`, `duration`, `ratio`, `generate_audio`, e entradas opcionais para `reference_images`, `reference_videos`, `reference_audios`, `reference_assets` e `auto_downscale`. |
| `seed` | INT | Não | 0 a 2147483647 | Um número usado para controlar se o nó deve ser executado novamente. Os resultados são não determinísticos, independentemente do valor da semente (padrão: 0). |
| `watermark` | BOOLEAN | Não | `True` / `False` | Se deve adicionar uma marca d'água ao vídeo gerado (padrão: False). |

**Restrições Importantes:**
*   Pelo menos uma imagem ou vídeo de referência (fornecido através das entradas `reference_images`, `reference_videos` ou `reference_assets`) é necessário para o funcionamento do nó.
*   Cada vídeo de referência deve ter pelo menos 1,8 segundos de duração. A duração combinada de todos os vídeos de referência não pode exceder 15,1 segundos.
*   Cada clipe de áudio de referência deve ter pelo menos 1,8 segundos de duração. A duração combinada de todo o áudio de referência não pode exceder 15,1 segundos.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|---------------|---------------|-----------|
| `video` | VIDEO | O arquivo de vídeo gerado. |
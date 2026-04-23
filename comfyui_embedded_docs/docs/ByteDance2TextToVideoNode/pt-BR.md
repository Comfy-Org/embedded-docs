> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2TextToVideoNode/pt-BR.md)

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2TextToVideoNode/en.md)

Este nó utiliza a API Seedance 2.0 da ByteDance para gerar um vídeo a partir de uma descrição textual. Ele envia seu prompt para o modelo selecionado, aguarda o processamento do vídeo e retorna o resultado final.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Faixa | Descrição |
|-----------|---------------|-------------|-------|-----------|
| `model` | COMBO | Sim | `"Seedance 2.0"`<br>`"Seedance 2.0 Fast"` | O modelo a ser usado para geração de vídeo. Selecionar um modelo revelará entradas adicionais obrigatórias para o prompt, resolução, proporção de aspecto, duração e geração de áudio. "Seedance 2.0" é para máxima qualidade; "Seedance 2.0 Fast" é para otimização de velocidade. |
| `seed` | INT | Não | 0 a 2147483647 | Um valor de semente (padrão: 0). O nó será executado novamente se este valor mudar, mas os resultados são não determinísticos independentemente da semente. |
| `watermark` | BOOLEAN | Não | `True` / `False` | Se deve adicionar uma marca d'água ao vídeo (padrão: False). Esta é uma configuração avançada. |

**Nota:** O parâmetro `model` é uma combinação dinâmica. Ao selecionar um modelo, vários subparâmetros obrigatórios serão revelados, incluindo o prompt de texto, resolução, proporção de aspecto, duração e se deve gerar áudio. O texto do prompt deve ter pelo menos 1 caractere após a remoção de espaços em branco.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|---------------|---------------|-----------|
| `video` | VIDEO | O arquivo de vídeo gerado. |
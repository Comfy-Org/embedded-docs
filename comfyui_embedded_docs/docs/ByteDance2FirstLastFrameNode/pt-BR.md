> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2FirstLastFrameNode/pt-BR.md)

Este nó utiliza o modelo Seedance 2.0 da ByteDance para gerar um vídeo. Ele cria o vídeo com base em um prompt de texto e uma imagem obrigatória do primeiro quadro. Opcionalmente, você pode fornecer uma imagem do último quadro para orientar o final da sequência de vídeo.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `model` | COMBO | Sim | `"Seedance 2.0"`<br>`"Seedance 2.0 Fast"` | O modelo a ser usado para geração de vídeo. Seedance 2.0 é para máxima qualidade, enquanto Seedance 2.0 Fast é otimizado para velocidade. Selecionar um modelo revelará entradas adicionais para `prompt`, `resolution`, `ratio`, `duration` e `generate_audio`. |
| `first_frame` | IMAGE | Não | - | A imagem a ser usada como primeiro quadro do vídeo. |
| `last_frame` | IMAGE | Não | - | A imagem a ser usada como último quadro do vídeo. |
| `first_frame_asset_id` | STRING | Não | - | Um asset_id do Seedance para usar como primeiro quadro. Não pode ser usado ao mesmo tempo que a entrada de imagem `first_frame`. O padrão é uma string vazia. |
| `last_frame_asset_id` | STRING | Não | - | Um asset_id do Seedance para usar como último quadro. Não pode ser usado ao mesmo tempo que a entrada de imagem `last_frame`. O padrão é uma string vazia. |
| `seed` | INT | Não | 0 a 2147483647 | Um valor de semente. Alterar esta semente fará com que o nó seja executado novamente, mas os resultados são não determinísticos. O padrão é 0. |
| `watermark` | BOOLEAN | Não | - | Se deve adicionar uma marca d'água ao vídeo gerado. O padrão é Falso. |

**Restrições de Parâmetros:**
*   Você deve fornecer **ou** uma imagem `first_frame` **ou** um `first_frame_asset_id`. Fornecer ambos causará um erro.
*   Você não pode fornecer uma imagem `last_frame` e um `last_frame_asset_id` para o mesmo quadro.
*   A entrada `model` é uma combinação dinâmica. Após selecionar um modelo, você também deve preencher o campo `prompt` revelado (uma descrição em texto) e configurar os outros parâmetros revelados (`resolution`, `ratio`, `duration`, `generate_audio`).

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `output` | VIDEO | O vídeo gerado. |
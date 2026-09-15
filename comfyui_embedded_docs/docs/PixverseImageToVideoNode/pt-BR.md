# PixVerse Imagem para Vídeo

Gera um vídeo a partir de uma imagem estática e um prompt de texto usando PixVerse. O nó faz upload da imagem de entrada, aplica as configurações de qualidade, duração e movimento selecionadas e, em seguida, retorna o vídeo resultante quando a geração termina.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `imagem` | Imagem de entrada a ser transformada em vídeo | IMAGE | Sim | - |
| `prompt` | Prompt para a geração do vídeo (padrão: string vazia) | STRING | Sim | - |
| `qualidade` | Configuração de qualidade do vídeo (padrão: res_540p) | COMBO | Sim | `res_540p`<br>`res_1080p` |
| `duração_segundos` | Duração do vídeo gerado em segundos | COMBO | Sim | `dur_2`<br>`dur_5`<br>`dur_10` |
| `modo_de_movimento` | Estilo de movimento aplicado à geração do vídeo | COMBO | Sim | `normal`<br>`fast`<br>`slow`<br>`zoom_in`<br>`zoom_out`<br>`pan_left`<br>`pan_right`<br>`pan_up`<br>`pan_down`<br>`tilt_up`<br>`tilt_down`<br>`roll_clockwise`<br>`roll_counterclockwise` |
| `semente` | Semente para a geração do vídeo (padrão: 0) | INT | Sim | 0-2147483647 |
| `prompt_negativo` | Uma descrição textual opcional de elementos indesejados em uma imagem (padrão: string vazia) | STRING | Não | - |
| `pixverse_template` | Um template opcional para influenciar o estilo da geração, criado pelo nó PixVerse Template | CUSTOM | Não | - |

**Nota:** Ao usar a qualidade 1080p, o modo de movimento é automaticamente definido como normal e a duração é limitada a 5 segundos. Para durações diferentes de 5 segundos, o modo de movimento também é automaticamente definido como normal.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `output` | Vídeo gerado com base na imagem de entrada e nos parâmetros | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseImageToVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `93ea662a27159f55bf12e49ea230f0005813614ad07f5189d1fd61e7b937fd4b`

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ChromaRadianceOptions/pt-BR.md)

O nó ChromaRadianceOptions permite configurar configurações avançadas para o modelo Chroma Radiance. Ele encapsula um modelo existente e aplica opções específicas durante o processo de remoção de ruído com base em valores sigma, permitindo um controle refinado sobre o tamanho do tile NeRF e outros parâmetros relacionados à radiação.

## Entradas

| Parâmetro | Tipo de Dados | Tipo de Entrada | Padrão | Intervalo | Descrição |
|-----------|-----------|------------|---------|-------|-------------|
| `model` | MODEL | Obrigatório | - | - | O modelo ao qual aplicar as opções do Chroma Radiance |
| `preserve_wrapper` | BOOLEAN | Opcional | Verdadeiro | - | Quando habilitado, delegará a um wrapper de função de modelo existente, se houver. Geralmente deve ser deixado habilitado. |
| `start_sigma` | FLOAT | Opcional | 1.0 | 0.0 - 1.0 | O primeiro sigma para o qual estas opções estarão em vigor. |
| `end_sigma` | FLOAT | Opcional | 0.0 | 0.0 - 1.0 | O último sigma para o qual estas opções estarão em vigor. |
| `nerf_tile_size` | INT | Opcional | -1 | -1 e acima | Permite substituir o tamanho padrão do tile NeRF. -1 significa usar o padrão (32). 0 significa usar o modo sem tiling (pode exigir muita VRAM). |

**Observação:** As opções do Chroma Radiance só entram em vigor quando o valor sigma atual está entre `end_sigma` e `start_sigma` (inclusive). O parâmetro `nerf_tile_size` só é aplicado quando definido como 0 ou valores superiores.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `model` | MODEL | O modelo modificado com as opções do Chroma Radiance aplicadas |

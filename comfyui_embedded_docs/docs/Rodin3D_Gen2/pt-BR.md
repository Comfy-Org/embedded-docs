> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Gen2/pt-BR.md)

O nó Rodin3D_Gen2 gera ativos 3D usando a API Rodin. Ele recebe imagens de entrada e as converte em modelos 3D com vários tipos de material e contagens de polígonos. O nó gerencia todo o processo de geração, incluindo a criação da tarefa, a verificação do status e o download dos arquivos, de forma automática.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `Images` | IMAGE | Sim | - | Imagens de entrada a serem usadas para a geração do modelo 3D |
| `Seed` | INT | Não | 0-65535 | Valor de semente aleatória para a geração (padrão: 0) |
| `Material_Type` | COMBO | Não | "PBR"<br>"Shaded" | Tipo de material a ser aplicado ao modelo 3D (padrão: "PBR") |
| `Polygon_count` | COMBO | Não | "4K-Quad"<br>"8K-Quad"<br>"18K-Quad"<br>"50K-Quad"<br>"2K-Triangle"<br>"20K-Triangle"<br>"150K-Triangle"<br>"500K-Triangle" | Contagem de polígonos alvo para o modelo 3D gerado (padrão: "500K-Triangle") |
| `TAPose` | BOOLEAN | Não | - | Se deve aplicar o processamento TAPose (padrão: False) |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `3D Model Path` | STRING | Caminho do arquivo para o modelo 3D gerado |

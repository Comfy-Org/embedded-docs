> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Smooth/pt-BR.md)

O nó Rodin 3D Smooth gera ativos 3D usando a API Rodin, processando imagens de entrada e convertendo-as em modelos 3D suaves. Ele recebe múltiplas imagens como entrada e produz um arquivo de modelo 3D para download. O nó gerencia todo o processo de geração, incluindo a criação da tarefa, a verificação do status e o download do arquivo, de forma automática.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `Images` | IMAGE | Sim | - | Imagens de entrada a serem usadas para a geração do modelo 3D |
| `Seed` | INT | Sim | - | Valor de semente aleatória para consistência na geração |
| `Material_Type` | STRING | Sim | - | Tipo de material a ser aplicado ao modelo 3D |
| `Polygon_count` | STRING | Sim | - | Quantidade alvo de polígonos para o modelo 3D gerado |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `3D Model Path` | STRING | Caminho do arquivo para o modelo 3D baixado |

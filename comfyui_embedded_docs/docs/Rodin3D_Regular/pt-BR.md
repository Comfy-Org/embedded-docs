> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Regular/pt-BR.md)

O nó Rodin 3D Regular gera ativos 3D usando a API Rodin. Ele recebe imagens de entrada e as processa através do serviço Rodin para criar modelos 3D. O nó gerencia todo o fluxo de trabalho, desde a criação da tarefa até o download dos arquivos finais do modelo 3D.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `Images` | IMAGE | Sim | - | Imagens de entrada usadas para a geração do modelo 3D |
| `Seed` | INT | Sim | - | Valor de semente aleatória para resultados reproduzíveis |
| `Material_Type` | STRING | Sim | - | Tipo de material a ser aplicado ao modelo 3D |
| `Polygon_count` | STRING | Sim | - | Contagem de polígonos alvo para o modelo 3D gerado |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `3D Model Path` | STRING | Caminho do arquivo para o modelo 3D gerado |

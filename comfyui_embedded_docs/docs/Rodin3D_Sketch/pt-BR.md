> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Sketch/pt-BR.md)

Este nó gera ativos 3D usando a API Rodin. Ele recebe imagens de entrada e as converte em modelos 3D por meio de um serviço externo. O nó gerencia todo o processo, desde a criação da tarefa até o download dos arquivos finais do modelo 3D.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `Images` | IMAGE | Sim | - | Imagens de entrada a serem convertidas em modelos 3D |
| `Seed` | INT | Não | 0-65535 | Valor de semente aleatória para a geração (padrão: 0) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `3D Model Path` | STRING | Caminho do arquivo para o modelo 3D gerado |

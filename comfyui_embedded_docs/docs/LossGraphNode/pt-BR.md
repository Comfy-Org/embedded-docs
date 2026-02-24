> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LossGraphNode/pt-BR.md)

O LossGraphNode cria um gráfico visual dos valores de perda (loss) do treinamento ao longo do tempo e o salva como um arquivo de imagem. Ele recebe dados de perda de processos de treinamento e gera um gráfico de linhas mostrando como a perda muda ao longo das etapas de treinamento. O gráfico resultante inclui rótulos dos eixos, valores mínimo e máximo da perda e é salvo automaticamente no diretório de saída temporário com um carimbo de data/hora.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `loss` | LOSS | Sim | Múltiplas opções disponíveis | Os dados de perda contendo os valores a serem plotados (padrão: dicionário vazio) |
| `filename_prefix` | STRING | Sim | - | O prefixo para o nome do arquivo de imagem de saída (padrão: "loss_graph") |

**Observação:** O parâmetro `loss` requer um dicionário de perda válido contendo uma chave "loss" com os valores de perda. O nó dimensiona automaticamente os valores de perda para se ajustarem às dimensões do gráfico e gera um gráfico de linhas mostrando a progressão da perda ao longo das etapas de treinamento.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `ui.images` | IMAGE | A imagem do gráfico de perda gerada, salva no diretório temporário |

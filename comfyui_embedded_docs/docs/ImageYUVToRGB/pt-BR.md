> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageYUVToRGB/pt-BR.md)

O nó ImageYUVToRGB converte imagens do espaço de cores YUV para o espaço de cores RGB. Ele recebe três imagens de entrada separadas representando os canais Y (luminância), U (projeção azul) e V (projeção vermelha) e as combina em uma única imagem RGB usando uma conversão de espaço de cores.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `Y` | IMAGE | Sim | - | A imagem de entrada do canal Y (luminância) |
| `U` | IMAGE | Sim | - | A imagem de entrada do canal U (projeção azul) |
| `V` | IMAGE | Sim | - | A imagem de entrada do canal V (projeção vermelha) |

**Observação:** Todas as três imagens de entrada (Y, U e V) devem ser fornecidas juntas e devem ter dimensões compatíveis para uma conversão adequada.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `output` | IMAGE | A imagem RGB convertida |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FreeU_V2/pt-BR.md)

O nó FreeU_V2 aplica um aprimoramento baseado em frequência a modelos de difusão modificando a arquitetura U-Net. Ele dimensiona diferentes canais de características usando parâmetros configuráveis para melhorar a qualidade da geração de imagens sem exigir treinamento adicional. O nó funciona aplicando patches aos blocos de saída do modelo para aplicar fatores de escala a dimensões específicas dos canais.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sim | - | O modelo de difusão ao qual aplicar o aprimoramento FreeU |
| `b1` | FLOAT | Sim | 0.0 - 10.0 | Fator de escala de características do backbone para o primeiro bloco (padrão: 1.3) |
| `b2` | FLOAT | Sim | 0.0 - 10.0 | Fator de escala de características do backbone para o segundo bloco (padrão: 1.4) |
| `s1` | FLOAT | Sim | 0.0 - 10.0 | Fator de escala de características de skip para o primeiro bloco (padrão: 0.9) |
| `s2` | FLOAT | Sim | 0.0 - 10.0 | Fator de escala de características de skip para o segundo bloco (padrão: 0.2) |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `model` | MODEL | O modelo de difusão aprimorado com as modificações FreeU aplicadas |

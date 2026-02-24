> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaVideoNode/pt-BR.md)

Gera vídeos de forma síncrona com base no prompt e nas configurações de saída. Este nó cria conteúdo de vídeo usando descrições textuais e vários parâmetros de geração, produzindo o vídeo final assim que o processo de geração é concluído.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sim | - | Prompt para a geração do vídeo (padrão: string vazia) |
| `model` | COMBO | Sim | Múltiplas opções disponíveis | O modelo de geração de vídeo a ser usado |
| `aspect_ratio` | COMBO | Sim | Múltiplas opções disponíveis | A proporção de tela para o vídeo gerado (padrão: 16:9) |
| `resolution` | COMBO | Sim | Múltiplas opções disponíveis | A resolução de saída para o vídeo (padrão: 540p) |
| `duration` | COMBO | Sim | Múltiplas opções disponíveis | A duração do vídeo gerado |
| `loop` | BOOLEAN | Sim | - | Se o vídeo deve ser em loop (padrão: Falso) |
| `seed` | INT | Sim | 0 a 18446744073709551615 | Semente para determinar se o nó deve ser executado novamente; os resultados reais são não determinísticos independentemente da semente (padrão: 0) |
| `luma_concepts` | CUSTOM | Não | - | Conceitos de Câmera opcionais para ditar o movimento da câmera via o nó Luma Concepts |

**Observação:** Ao usar o modelo `ray_1_6`, os parâmetros `duration` e `resolution` são automaticamente definidos como None e não afetam a geração.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `output` | VIDEO | O arquivo de vídeo gerado |

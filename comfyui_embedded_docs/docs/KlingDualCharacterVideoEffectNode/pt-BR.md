> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingDualCharacterVideoEffectNode/pt-BR.md)

O nó Kling Dual Character Video Effect cria vídeos com efeitos especiais baseados na cena selecionada. Ele recebe duas imagens e posiciona a primeira imagem no lado esquerdo e a segunda imagem no lado direito do vídeo composto. Diferentes efeitos visuais são aplicados dependendo da cena de efeito escolhida.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `image_left` | IMAGE | Sim | - | Imagem do lado esquerdo |
| `image_right` | IMAGE | Sim | - | Imagem do lado direito |
| `effect_scene` | COMBO | Sim | Múltiplas opções disponíveis | O tipo de cena de efeito especial a ser aplicada na geração do vídeo |
| `model_name` | COMBO | Não | Múltiplas opções disponíveis | O modelo a ser usado para os efeitos de personagem (padrão: "kling-v1") |
| `mode` | COMBO | Não | Múltiplas opções disponíveis | O modo de geração de vídeo (padrão: "std") |
| `duration` | COMBO | Sim | Múltiplas opções disponíveis | A duração do vídeo gerado |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `output` | VIDEO | O vídeo gerado com efeitos de duplo personagem |
| `duration` | STRING | A informação de duração do vídeo gerado |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingSingleImageVideoEffectNode/pt-BR.md)

O nó Kling Single Image Video Effect cria vídeos com diferentes efeitos especiais baseados em uma única imagem de referência. Ele aplica vários efeitos visuais e cenas para transformar imagens estáticas em conteúdo de vídeo dinâmico. O nó suporta diferentes cenas de efeito, opções de modelo e durações de vídeo para alcançar o resultado visual desejado.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Sim | - | Imagem de Referência. URL ou string codificada em Base64 (sem o prefixo data:image). O tamanho do arquivo não pode exceder 10MB, a resolução não pode ser inferior a 300*300px, e a proporção de aspecto deve estar entre 1:2.5 e 2.5:1 |
| `effect_scene` | COMBO | Sim | Opções de KlingSingleImageEffectsScene | O tipo de cena de efeito especial a ser aplicado na geração do vídeo |
| `model_name` | COMBO | Sim | Opções de KlingSingleImageEffectModelName | O modelo específico a ser usado para gerar o efeito de vídeo |
| `duration` | COMBO | Sim | Opções de KlingVideoGenDuration | A duração do vídeo gerado |

**Observação:** As opções específicas para `effect_scene`, `model_name` e `duration` são determinadas pelos valores disponíveis em suas respectivas classes de enumeração (KlingSingleImageEffectsScene, KlingSingleImageEffectModelName e KlingVideoGenDuration).

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `output` | VIDEO | O vídeo gerado com os efeitos aplicados |
| `video_id` | STRING | O identificador único para o vídeo gerado |
| `duration` | STRING | A duração do vídeo gerado |

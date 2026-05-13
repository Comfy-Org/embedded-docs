> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingSingleImageVideoEffectNode/pt-BR.md)

O nó Kling Single Image Video Effect cria vídeos com diferentes efeitos especiais com base em uma única imagem de referência. Ele aplica vários efeitos visuais e cenas para transformar imagens estáticas em conteúdo de vídeo dinâmico. O nó suporta diferentes cenas de efeitos, opções de modelo e durações de vídeo para alcançar o resultado visual desejado.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Sim | - | Imagem de referência. URL ou string codificada em Base64 (sem o prefixo `data:image`). O tamanho do arquivo não pode exceder 10MB, a resolução não pode ser inferior a 300x300px e a proporção deve estar entre 1:2.5 e 2.5:1 |
| `effect_scene` | COMBO | Sim | `"dizzydizzy"`<br>`"bloombloom"`<br>`"neon"`<br>`"cartoon"`<br>`"sketch"`<br>`"oil"`<br>`"watercolor"`<br>`"3d"` | O tipo de cena de efeito especial a ser aplicado na geração do vídeo. Alguns efeitos podem ter preços diferentes. |
| `model_name` | COMBO | Sim | `"kling-v1-5"`<br>`"kling-v1-6"` | A versão específica do modelo a ser usada para gerar o efeito de vídeo. |
| `duration` | COMBO | Sim | `"5"`<br>`"10"` | A duração do vídeo gerado em segundos. |

**Nota:** O parâmetro `effect_scene` afeta o preço do nó. Os efeitos `dizzydizzy` e `bloombloom` custam US$ 0,49 por geração, enquanto todos os outros efeitos custam US$ 0,28 por geração.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `output` | VIDEO | O vídeo gerado com os efeitos aplicados |
| `video_id` | STRING | O identificador único para o vídeo gerado |
| `duration` | STRING | A duração do vídeo gerado |

---
**Source fingerprint (SHA-256):** `519db2f7185f200140c746bdebf89383523e0342bbfb61538adac063295d365d`

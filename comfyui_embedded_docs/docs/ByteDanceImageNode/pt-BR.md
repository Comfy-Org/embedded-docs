O nó ByteDance Image gera imagens usando modelos ByteDance por meio de uma API baseada em prompts de texto. Ele permite selecionar um modelo, especificar dimensões da imagem e controlar vários parâmetros de geração, como semente e escala de orientação. O nó se conecta ao serviço de geração de imagens da ByteDance e retorna a imagem criada.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `model` | O modelo ByteDance a ser usado para geração de imagem. Atualmente, apenas uma opção de modelo está disponível. | STRING | Sim | `"seedream-3-0-t2i-250415"` |
| `prompt` | O prompt de texto usado para gerar a imagem. Deve ter pelo menos 1 caractere após a remoção de espaços em branco. | STRING | Sim | - |
| `size_preset` | Escolha um tamanho recomendado. Selecione Personalizado para usar a largura e altura abaixo. Os predefinidos disponíveis são definidos pela lista `RECOMMENDED_PRESETS`. | STRING | Sim | Ver descrição |
| `width` | Largura personalizada para a imagem. Este valor só é usado quando `size_preset` está definido como `Personalizado`. Padrão: 1024. | INT | Sim | 512 a 2048 (passo 64) |
| `height` | Altura personalizada para a imagem. Este valor só é usado quando `size_preset` está definido como `Personalizado`. Padrão: 1024. | INT | Sim | 512 a 2048 (passo 64) |
| `seed` | Semente a ser usada para geração. Padrão: 0. | INT | Não | 0 a 2147483647 (passo 1) |
| `guidance_scale` | Valores mais altos fazem a imagem seguir o prompt mais fielmente. Padrão: 2.5. | FLOAT | Não | 1.0 a 10.0 (passo 0.01) |
| `watermark` | Se deve adicionar uma marca d'água "gerado por IA" à imagem. Padrão: Falso. Este é um parâmetro avançado. | BOOLEAN | Não | Verdadeiro / Falso |

**Observação sobre parâmetros de tamanho:** Os parâmetros `width` e `height` só são usados quando `size_preset` está definido como `Personalizado`. Se um tamanho predefinido for selecionado, as dimensões do predefinido substituem os valores personalizados de largura e altura. Tanto a largura quanto a altura devem estar entre 512 e 2048 pixels ao usar dimensões personalizadas.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `IMAGE` | A imagem gerada retornada da API ByteDance como um tensor. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceImageNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `6ad3011ae942e81bc5e5296fa7120ee89637ef7487e2f12822d84b6917ec211e`

# Recraft V4 Texto para Imagem

Gera imagens a partir de prompts de texto usando os modelos Recraft V4 e V4.1. Envia o prompt e as configurações selecionadas para a API da Recraft e retorna a imagem ou imagens geradas. Se imagens de referência de estilo forem usadas, o ID de estilo criado também é retornado.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `modelo` | O modelo a usar para geração. Os modelos recraftv4_styles são projetados para geração com estilo consistente e sempre exigem um style_id ou style_references. | DYNAMIC_COMBO | Sim | "recraftv4_1"<br>"recraftv4_1_utility"<br>"recraftv4_1_pro"<br>"recraftv4_1_utility_pro"<br>"recraftv4"<br>"recraftv4_pro"<br>"recraftv4_styles"<br>"recraftv4_styles_pro" |
| `prompt` | Prompt para a geração da imagem. Máximo de 10.000 caracteres. | STRING | Sim | 1 a 10000 caracteres |
| `prompt_negativo` | Esta entrada é ignorada: o prompt negativo não é compatível com os modelos Recraft V4 e V4.1. | STRING | Sim | N/A |
| `n` | O número de imagens a gerar (padrão: 1). | INT | Sim | 1 a 6 |
| `semente` | Seed para determinar se o nó deve ser executado novamente; os resultados reais são não determinísticos independentemente da seed (padrão: 0). | INT | Sim | 0 a 18446744073709551615 |
| `recraft_controls` | Controles adicionais opcionais sobre a geração por meio do nó Recraft Controls. | CUSTOM | Não | N/A |
| `style_id` | UUID de um estilo Recraft V4 a aplicar, por exemplo, a partir do nó Recraft V4 Create Style ou da saída style_id de uma execução anterior. Não pode ser combinado com style_references (padrão: vazio). | STRING | Não | String UUID válida |
| `style_match` | Quão fielmente seguir o estilo: precise reproduz os detalhes, flexible corresponde à aparência geral. Usado apenas quando um estilo é fornecido (padrão: "precise"). | COMBO | Não | "precise"<br>"flexible" |

### Entradas de recraftv4_1, recraftv4_1_utility, recraftv4 e recraftv4_styles

Esses modelos compartilham o mesmo parâmetro `size`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `size` | O tamanho da imagem gerada (padrão: "1024x1024"). | COMBO | Sim | Várias opções disponíveis (tamanhos padrão do Recraft V4; inclui "1024x1024") |

### Entradas de recraftv4_1_pro, recraftv4_1_utility_pro, recraftv4_pro e recraftv4_styles_pro

Esses modelos compartilham o mesmo parâmetro `size`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `size` | O tamanho da imagem gerada (padrão: "2048x2048"). | COMBO | Sim | Várias opções disponíveis (tamanhos pro do Recraft V4; inclui "2048x2048") |

### Entradas de referência

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `style_references` | Imagens de referência para criar um estilo em tempo real, cobradas além da geração. O estilo criado é retornado como style_id para reutilização. Não pode ser combinado com style_id. Slot expansível: conecte 1..N imagens (style_reference_1, style_reference_2, ...). | IMAGE | Não | 0 até o número máximo de imagens de referência permitido pela API da Recraft; o tamanho codificado total não deve exceder 10 MB |

**Observação:** O parâmetro `size` é uma entrada dinâmica cujas opções disponíveis mudam com base no `model` selecionado. Os modelos `recraftv4_styles` e `recraftv4_styles_pro` sempre exigem um estilo: conecte imagens de referência de estilo ou forneça um `style_id`. As entradas `style_id` e `style_references` são mutuamente exclusivas — forneça apenas uma delas. Um `style_id` deve ser um UUID válido. A entrada `style_match` só é usada quando um estilo é fornecido. Imagens de referência de estilo são cobradas além da geração e seu tamanho codificado total não deve exceder 10 MB. O valor de `seed` não garante saídas de imagem reproduzíveis. Se você usar um ID de estilo da Infinite Style Library, certifique-se de que não seja um estilo Vector art, pois isso pode retornar dados SVG em vez de uma imagem.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|---------------|-------------|-----------|
| `output` | A imagem gerada ou lote de imagens. | IMAGE |
| `style_id` | O ID de estilo usado ou criado por esta geração. Quando imagens de referência de estilo são fornecidas, o estilo criado é retornado aqui para reutilização; string vazia quando nenhum estilo é usado. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4TextToImageNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `af5c1f68e59ca282cdca7c32cd50f0438b743fdda27d9d22e59b2d1343f45e26`

# Recraft V4 Texto para Imagem

Recraft V4 Text to Image

Este nó gera imagens a partir de descrições textuais usando os modelos de IA Recraft V4 e V4.1. Ele envia seu prompt para uma API externa e retorna as imagens geradas. Você pode controlar a saída especificando o modelo, o tamanho da imagem, o número de imagens e um estilo opcional, seja como um ID de estilo salvo ou a partir de imagens de referência.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `modelo` | O modelo a ser usado para a geração. Os modelos recraftv4_styles são feitos para geração com consistência de estilo e sempre exigem um style_id ou style_references. | DYNAMIC_COMBO | Sim | "recraftv4_1"<br>"recraftv4_1_utility"<br>"recraftv4_1_pro"<br>"recraftv4_1_utility_pro"<br>"recraftv4"<br>"recraftv4_pro"<br>"recraftv4_styles"<br>"recraftv4_styles_pro" |
| `prompt` | Prompt para a geração da imagem. Máximo de 10.000 caracteres. | STRING | Sim | 1 a 10.000 caracteres |
| `prompt_negativo` | Esta entrada é ignorada: o prompt negativo não é suportado pelos modelos Recraft V4 e V4.1. | STRING | Sim | N/A |
| `n` | O número de imagens a gerar (padrão: 1). | INT | Sim | 1 a 6 |
| `semente` | Semente para determinar se o nó deve ser executado novamente; os resultados reais são não determinísticos independentemente da semente (padrão: 0). | INT | Sim | 0 a 18446744073709551615 |
| `recraft_controls` | Controles adicionais opcionais sobre a geração por meio do nó Recraft Controls. | CUSTOM | Não | N/A |
| `style_id` | UUID de um estilo Recraft V4 a ser aplicado, por exemplo, do nó Recraft V4 Create Style ou da saída style_id de uma execução anterior. Não pode ser combinado com style_references (padrão: vazio). | STRING | Não | String de UUID válido |
| `style_match` | O nível de fidelidade ao estilo: precise o reproduz em detalhes, flexible corresponde à aparência geral. Usado apenas quando um estilo é fornecido (padrão: "precise"). | COMBO | Não | "precise"<br>"flexible" |

### Entradas de recraftv4_1, recraftv4_1_utility, recraftv4 e recraftv4_styles

Esses modelos compartilham o mesmo parâmetro `size`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `size` | O tamanho da imagem gerada (padrão: "1024x1024"). | COMBO | Sim | Várias opções disponíveis (tamanhos padrão do Recraft V4, incluindo "1024x1024") |

### Entradas de recraftv4_1_pro, recraftv4_1_utility_pro, recraftv4_pro e recraftv4_styles_pro

Esses modelos compartilham o mesmo parâmetro `size`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `size` | O tamanho da imagem gerada (padrão: "2048x2048"). | COMBO | Sim | Várias opções disponíveis (tamanhos pro do Recraft V4, incluindo "2048x2048") |

### Entradas de referência

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `style_references` | Imagens de referência para criar um estilo dinamicamente, cobradas além da geração. O estilo criado é retornado como style_id para reutilização. Não pode ser combinado com style_id. Slot expansível: conecte de 1 a N imagens (style_reference_1, style_reference_2, ...). | IMAGE | Não | 0 até o número máximo de imagens de referência permitido pela API Recraft; o tamanho total codificado não deve exceder 10 MB |

**Nota:** O parâmetro `size` é uma entrada dinâmica cujas opções disponíveis mudam de acordo com o `model` selecionado. Os modelos `recraftv4_styles` e `recraftv4_styles_pro` sempre exigem um estilo: conecte imagens de referência de estilo ou forneça um `style_id`. As entradas `style_id` e `style_references` são mutuamente exclusivas — forneça apenas uma delas. Um `style_id` deve ser um UUID válido. A entrada `style_match` é usada somente quando um estilo é fornecido. As imagens de referência de estilo são cobradas além da geração e seu tamanho total codificado não deve exceder 10 MB. O valor de `seed` não garante saídas de imagem reproduzíveis. Se você usar um ID de estilo da Infinite Style Library, certifique-se de que ele não seja um estilo de arte vetorial, pois isso pode retornar dados SVG em vez de uma imagem.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `output` | A imagem gerada ou o lote de imagens. | IMAGE |
| `style_id` | O ID de estilo usado ou criado por esta geração. Quando imagens de referência de estilo são fornecidas, o estilo criado é retornado aqui para reutilização; string vazia quando nenhum estilo é usado. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4TextToImageNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `af5c1f68e59ca282cdca7c32cd50f0438b743fdda27d9d22e59b2d1343f45e26`

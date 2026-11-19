# HeyGen Avatar 6 Identity to Video

Gere um vídeo de um avatar HeyGen falando com o Avatar 6. Escolha uma das aparências integradas compatíveis com o Avatar 6 ou cole seu próprio ID de avatar do HeyGen e, em seguida, conduza-o com um roteiro de texto ou seu próprio áudio.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | Seletor de modelo. `"heygen-avatar-6-turbo"` é o nível mais barato e rápido; ambos os modelos aceitam as mesmas entradas e resoluções. | COMBO | Sim | `"heygen-avatar-6"`<br>`"heygen-avatar-6-turbo"` |
| `avatar` | Aparência do avatar a ser exibida. As 19 aparências integradas compatíveis com o Avatar 6 são listadas diretamente; `custom avatar` revela `custom_avatar_id` para uma aparência que você criou no HeyGen. | DYNAMIC_COMBO | Sim | 19 aparências integradas<br>`custom avatar` |
| `speech` | Conduza o avatar com um roteiro de texto (conversão de texto em fala do HeyGen) ou com seu próprio áudio. Nome de exibição: origem da fala. | DYNAMIC_COMBO | Sim | `"script"`<br>`"audio"` |
| `resolution` | Resolução do vídeo de saída. Padrão: `"1080p"`. | COMBO | Sim | `"1080p"`<br>`"2k"` |
| `aspect_ratio` | Proporção do vídeo de saída. `"auto"` segue a filmagem da própria aparência do avatar. Padrão: `"auto"`. | COMBO | Sim | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:5"`<br>`"5:4"` |
| `motion_prompt` | Direcionamento opcional para gestos, expressão, postura e movimento de câmera. Padrão: string vazia. | STRING | Sim | Texto multilinha |
| `motion_expressiveness` | `"less"` fornece menos gestos e de menor amplitude. O prompt de movimento tem precedência onde os dois se sobrepõem. Padrão: `"default"`. | COMBO | Sim | `"less"`<br>`"default"` |
| `seed` | A seed controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente da seed. Padrão: 42. | INT | Sim | 0 a 2147483647 |

### Entradas de `custom avatar`

Estas entradas aparecem quando `avatar` está definido como `custom avatar`.

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `custom_avatar_id` | ID da aparência de avatar do HeyGen compatível com o Avatar 6, como uma criada com o HeyGen Create Avatar. Padrão: string vazia. | STRING | Sim | - |

### Entradas de fala de `script`

Estas entradas aparecem quando `speech` está definido como `"script"`.

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `text` | Texto que o avatar deve falar. Padrão: string vazia. | STRING | Sim | Até 5000 caracteres |
| `voice` | Voz para o roteiro. A opção padrão usa a voz que o HeyGen atribuiu ao avatar; avatares criados com o HeyGen Create Avatar não têm nenhuma, então escolha uma voz para eles. | COMBO | Sim | `"(avatar's default voice)"` mais a lista geral de vozes do HeyGen |
| `custom_voice_id` | ID de voz opcional do HeyGen. Quando definido, ele substitui a voz selecionada acima. Padrão: string vazia. | STRING | Não | - |
| `voice_speed` | Multiplicador da velocidade da fala. Padrão: 1.0. | FLOAT | Não | 0.5 a 1.5 (passo 0.05) |

### Entradas de fala de `audio`

Estas entradas aparecem quando `speech` está definido como `"audio"`.

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `audio` | Fala para o avatar. A duração do vídeo acompanha o áudio. | AUDIO | Sim | 0.5 segundos a 10 minutos |

**Restrições e comportamento:**

* `custom avatar` requer um ID de avatar não vazio; caso contrário, o nó gera um erro.
* Um roteiro é limitado a 5000 caracteres, e o áudio, a 10 minutos.
* O preço é por segundo de vídeo de saída e depende do modelo e da resolução.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|-------------|-------------|-----------|
| `video` | O vídeo falante gerado, baixado do HeyGen assim que a renderização termina. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenAvatar6IdentityToVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `952146c3790333883ad08b7031853eb7021c8d18c59e58389b5d57b548820944`

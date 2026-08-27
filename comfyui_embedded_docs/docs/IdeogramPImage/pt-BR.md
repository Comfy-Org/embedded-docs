# Ideogram P-Image

Ideogram & Pruna P-Image gera imagens a partir de um prompt de texto usando o modelo rápido de texto para imagem da Ideogram, conhecido por sua forte tipografia e fotorrealismo. Ele também suporta legendas JSON estruturadas do Ideogram 4.0 para controle exato de strings de texto, cores e layout. O nó retorna a(s) imagem(ns) gerada(s) junto com o prompt final a partir do qual a imagem foi realmente gerada.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt de texto. Também aceita uma legenda JSON estruturada do Ideogram 4.0 (cores exatas como hexadecimais #RRGGBB, strings de texto exatas, layout de caixa delimitadora) — defina `prompt_upsampling` como OFF para usá-la exatamente como fornecida. Não deve estar vazio. (padrão: "") | STRING | Sim | Qualquer texto não vazio |
| `quality` | Nível de velocidade/preço/qualidade. MEDIUM é o padrão do dia a dia; HIGH é para prompts complexos, detalhes finos e textos difíceis; VERY_LOW/LOW para rascunhos em escala. Textos difíceis são renderizados de forma ruim abaixo de MEDIUM. (padrão: "MEDIUM") | COMBO | Sim | "VERY_LOW"<br>"LOW"<br>"MEDIUM"<br>"HIGH" |
| `resolution` | Classe de tamanho da saída (os pixels exatos seguem a proporção de aspecto, ex.: 16:9 gera 1280x720 em 1K e 2560x1440 em 2K). Prefira HIGH + 2K para tipografia nítida. (padrão: "1K") | COMBO | Sim | "1K"<br>"2K" |
| `aspect_ratio` | A proporção de aspecto para a geração da imagem. (padrão: "1:1") | COMBO | Sim | "1:3"<br>"3:1"<br>"1:2"<br>"2:1"<br>"9:16"<br>"16:9"<br>"10:16"<br>"16:10"<br>"2:3"<br>"3:2"<br>"3:4"<br>"4:3"<br>"4:5"<br>"5:4"<br>"1:1" |
| `prompt_upsampling` | Expande prompts curtos em uma legenda estruturada detalhada antes da geração (o prompt reescrito é retornado como `final_prompt`). Defina como OFF quando estiver fornecendo sua própria legenda JSON ou redação exata. (padrão: "AUTO") | COMBO | Sim | "AUTO"<br>"ON"<br>"OFF" |
| `seed` | Semente para geração reproduzível. Com `prompt_upsampling` OFF, a mesma semente e as mesmas configurações retornam a mesma imagem; com ON/AUTO, a reescrita do prompt varia a cada execução — para reproduzir um resultado, reutilize a saída `final_prompt` com `prompt_upsampling` OFF e a mesma semente. (padrão: 42) | INT | Não | 0 a 2147483647 |

**Observação sobre restrições:** O prompt deve conter pelo menos um caractere que não seja espaço em branco; caso contrário, o nó falha. Defina `prompt_upsampling` como OFF ao fornecer sua própria legenda JSON estruturada ou redação exata. Quando `prompt_upsampling` está ON ou AUTO, o prompt é reescrito antes da geração, então a mesma semente pode não reproduzir a mesma imagem; para reproduzir uma imagem, reutilize a saída `final_prompt` com `prompt_upsampling` OFF e a mesma semente.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|-------------|-------------|-----------|
| `image` | A(s) imagem(ns) gerada(s) retornada(s) como um lote de imagens. Se o filtro de segurança de conteúdo da Ideogram bloquear a geração, um erro será gerado. | IMAGE |
| `final_prompt` | O prompt a partir do qual a imagem foi realmente gerada (a legenda estruturada reescrita quando o `prompt_upsampling` foi executado, caso contrário, o seu prompt). Alimente-o de volta com `prompt_upsampling` OFF e a mesma semente para reproduzir esta imagem. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramPImage/pt-BR.md)

---
**Source fingerprint (SHA-256):** `6b014c2f097c49b5930f38869a4e2da0ebb19863763ae5817d6e566a36d2b8e8`

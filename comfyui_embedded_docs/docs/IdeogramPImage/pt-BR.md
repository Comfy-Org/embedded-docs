# IdeogramPImage

Ideogram P-Image gera imagens a partir de um prompt de texto usando o modelo rápido de texto para imagem da Ideogram, conhecido por sua excelente tipografia e fotorrealismo. O nó também suporta legendas JSON estruturadas do Ideogram 4.0 para controle exato sobre strings de texto, cores e layout. O nó retorna a(s) imagem(ns) gerada(s) junto com o prompt final que foi efetivamente usado para gerar a imagem.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt de texto. Também aceita uma legenda JSON estruturada do Ideogram 4.0 (cores exatas em formato hexadecimal #RRGGBB, strings de texto exatas, layout em caixas delimitadoras) — defina prompt_upsampling como OFF para usá-la literalmente. Não pode estar vazio. (padrão: "") | STRING | Sim | Qualquer texto |
| `quality` | Nível de velocidade/preço/qualidade. MEDIUM é o padrão para uso diário; HIGH para prompts complexos, detalhes finos e textos difíceis; VERY_LOW/LOW para rascunhos em escala. Textos difíceis são mal renderizados abaixo de MEDIUM. (padrão: "MEDIUM") | STRING | Sim | "VERY_LOW"<br>"LOW"<br>"MEDIUM"<br>"HIGH" |
| `resolution` | Classe de tamanho de saída (os pixels exatos seguem a proporção de aspecto, ex.: 16:9 gera 1280x720 em 1K e 2560x1440 em 2K). Prefira HIGH + 2K para tipografia nítida. (padrão: "1K") | STRING | Sim | "1K"<br>"2K" |
| `aspect_ratio` | A proporção de aspecto para a geração de imagens. (padrão: "1:1") | STRING | Sim | "1:3"<br>"3:1"<br>"1:2"<br>"2:1"<br>"9:16"<br>"16:9"<br>"10:16"<br>"16:10"<br>"2:3"<br>"3:2"<br>"3:4"<br>"4:3"<br>"4:5"<br>"5:4"<br>"1:1" |
| `prompt_upsampling` | Expande prompts curtos em uma legenda estruturada detalhada antes da geração (o prompt reescrito é retornado como final_prompt). Defina como OFF ao fornecer sua própria legenda JSON ou texto exato. (padrão: "AUTO") | STRING | Sim | "AUTO"<br>"ON"<br>"OFF" |
| `seed` | Semente para geração reproduzível. Com prompt_upsampling OFF, a mesma semente e as mesmas configurações retornam a mesma imagem; com ON/AUTO, a reescrita do prompt varia a cada execução — reproduza um resultado reutilizando a saída final_prompt dele com prompt_upsampling OFF e a mesma semente. (padrão: 42) | INT | Não | 0 a 2147483647 |

**Observação sobre restrições:** O prompt deve conter pelo menos um caractere que não seja espaço em branco; caso contrário, o nó falha. Defina `prompt_upsampling` como OFF ao fornecer sua própria legenda JSON estruturada ou texto exato. Quando `prompt_upsampling` estiver ON ou AUTO, o prompt é reescrito antes da geração; portanto, a mesma semente pode não reproduzir a mesma imagem; para reproduzir uma imagem, reutilize a saída `final_prompt` com `prompt_upsampling` OFF e a mesma semente.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `image` | A(s) imagem(ns) gerada(s) retornada(s) como um lote de imagens. Se o filtro de segurança de conteúdo da Ideogram bloquear a geração, um erro será gerado em vez disso. | IMAGE |
| `final_prompt` | O prompt do qual a imagem foi realmente gerada (a legenda estruturada reescrita quando o prompt_upsampling foi executado; caso contrário, o seu prompt). Realimente-o com prompt_upsampling OFF e a mesma semente para reproduzir esta imagem. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramPImage/pt-BR.md)

---
**Source fingerprint (SHA-256):** `7bd20aae508fee111ded32e87119ed6fc01c5ad5ba7d595e24391830a0f20bb7`

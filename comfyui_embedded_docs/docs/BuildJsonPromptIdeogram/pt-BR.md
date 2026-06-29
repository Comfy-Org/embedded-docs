# Construir Prompt JSON (Ideogram)

Este nó constrói um prompt JSON estruturado especificamente formatado para o modelo de geração de imagens Ideogram 4. Ele organiza suas instruções de texto, preferências de estilo e paleta de cores na estrutura JSON necessária que o modelo espera.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `elemento` | Elementos do prompt provenientes do nó Criar Caixas Delimitadoras. | ARRAY | Sim | - |
| `descrição_nível_alto` | Descrição opcional da imagem em uma ou duas frases. Fortemente recomendado. (padrão: vazio) | STRING | Não | - |
| `fundo` | Descrição obrigatória do fundo ou ambiente da imagem. (padrão: vazio) | STRING | Sim | - |
| `estilo` | A categoria de estilo visual para a imagem gerada. (padrão: "none") | COMBO | Sim | `"none"`<br>`"photo"`<br>`"art_style"` |
| `photo` | Detalhes de câmera ou lente para saídas fotográficas (ex.: 35mm, f/1.4, bokeh). Disponível apenas quando o estilo está definido como "photo". (padrão: vazio) | STRING | Não | - |
| `art_style` | Descrição do estilo artístico (ex.: ilustração vetorial plana, contornos marcantes). Disponível apenas quando o estilo está definido como "art_style". (padrão: vazio) | STRING | Não | - |
| `estética` | Palavras-chave estéticas obrigatórias (ex.: melancólico, cinematográfico, dessaturado). (padrão: vazio) | STRING | Sim | - |
| `iluminação` | Descrição obrigatória da iluminação (ex.: hora dourada, luz de contorno, sombras dramáticas). (padrão: vazio) | STRING | Sim | - |
| `meio` | Tipo de mídia obrigatório (ex.: fotografia, ilustração, render_3d, pintura, design_grafico). Quando style = photo, defina como fotografia. (padrão: vazio) | STRING | Sim | - |
| `paleta_de_cores` | Códigos de cores hexadecimais que orientam as cores dominantes da imagem. Até 16 entradas. | COLORS | Não | - |

**Nota:** Quando o parâmetro `style` estiver definido como "photo", a entrada `photo` fica disponível e você deve definir o parâmetro `medium` como "photograph". Quando `style` estiver definido como "art_style", a entrada `art_style` fica disponível.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|-------------|-------------|-----------|
| `prompt` | Um dicionário JSON estruturado contendo a descrição de alto nível, descrição de estilo (se aplicável) e desconstrução composicional com fundo e elementos. | DICT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BuildJsonPromptIdeogram/pt-BR.md)

---
**Source fingerprint (SHA-256):** `56a045e0c7c19531e6443696c0bdf3946df066d03eea7d2d217b7d92f052592f`

# Google Gemini Omni (Vídeo)

Este nó gera um vídeo com áudio a partir de um prompt de texto usando o modelo Google Gemini Omni Flash. Você pode opcionalmente fornecer imagens ou vídeos de referência para guiar ou editar o resultado.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `model` | O modelo de vídeo Gemini usado para gerar o vídeo. | COMBO | Sim | `"Omni Flash"` |
| `seed` | A semente controla se o nó deve ser reexecutado; os resultados são não determinísticos independentemente da semente. (padrão: 42) | INT | Sim | 0 a 2147483647 |

**Nota:** O parâmetro `model` é um combo dinâmico que se expande para incluir entradas adicionais quando "Omni Flash" é selecionado. Essas entradas adicionais incluem:
- `prompt` (STRING, obrigatório): O prompt de texto descrevendo o vídeo desejado. Descreva a duração desejada (3-10 segundos) e a proporção de aspecto (16:9 ou 9:16) diretamente no prompt.
- `images` (IMAGE, opcional): Imagens de referência para guiar a geração do vídeo. Máximo de 14 imagens.
- `videos` (VIDEO, opcional): Vídeos de referência para guiar a geração do vídeo. Máximo de 3 vídeos, cada um com duração máxima de 10 segundos.
- `temperature` (FLOAT, opcional, padrão: 1.0): Controla a aleatoriedade na geração.
- `top_p` (FLOAT, opcional, padrão: 0.95): Controla a amostragem por núcleo.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|-------------|-------------|-----------|
| `video` | O vídeo gerado com áudio. | VIDEO |
| `text` | A resposta de texto do modelo, se houver. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiVideoOmni/pt-BR.md)

---
**Source fingerprint (SHA-256):** `948eb712ca0ad3b7d3c7b3a9e1576f2c52a3575c07d8d52bb727bd9df717caa6`

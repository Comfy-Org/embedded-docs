# PixVerse V6 Primeiro-Último-Quadro para Vídeo

PixVerse V6 First-Last-Frame to Video gera um vídeo que faz a transição de um primeiro quadro para um último quadro usando o PixVerse, opcionalmente com áudio nativo. As duas imagens fornecidas são enviadas para a API do PixVerse, que produz o vídeo de transição e o retorna como um arquivo de vídeo. A saída mantém a proporção de aspecto do primeiro quadro.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `first_frame` | A imagem inicial do vídeo. | IMAGE | Sim | — |
| `last_frame` | A imagem final do vídeo. | IMAGE | Sim | — |
| `modelo` | Configurações do modelo e de geração. Seleciona o modelo PixVerse e exibe os seus parâmetros de geração. | DYNAMIC_COMBO | Sim | "PixVerse V6" |

### Entradas do PixVerse V6

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt que descreve a transição. | STRING | Sim | Até 5000 caracteres |
| `quality` | Resolução de saída. Define a borda longa: 360p é 640px, 540p 1024px, 720p 1280px, 1080p 1920px. (padrão: 720p) | COMBO | Sim | "360p"<br>"540p"<br>"720p"<br>"1080p" |
| `duration_seconds` | Duração do vídeo gerado em segundos. (padrão: 5) | INT | Sim | 1 a 15 |
| `generate_audio` | Gera uma trilha de áudio nativa junto com o vídeo. (padrão: true) | BOOLEAN | Sim | true<br>false |
| `seed` | Semente para a geração do vídeo. O PixVerse a registra, mas não reproduz uma execução a partir dela. (padrão: 42) | INT | Sim | 0 a 2147483647 |
| `negative_prompt` | Uma descrição textual opcional de elementos indesejados no vídeo. | STRING | Não | Até 2048 caracteres |
| `style` | Um estilo visual opcional aplicado a todo o vídeo. (padrão: nenhum) | COMBO | Não | Várias opções disponíveis (padrão: "none") |

Nota: O prompt não pode estar vazio após remover espaços em branco e está limitado a 5000 caracteres. O prompt negativo, quando fornecido, está limitado a 2048 caracteres. A duração deve estar entre 1 e 15 segundos. O vídeo de saída mantém a proporção de aspecto do primeiro quadro.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `output` | O vídeo gerado que faz a transição do primeiro quadro para o último quadro, incluindo uma trilha de áudio quando `generate_audio` está habilitado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseV6FirstLastFrameNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `cdb5e45e9de2b429b9d43bbff90b6529af246911ecae8c2809c8abd539101aaa`

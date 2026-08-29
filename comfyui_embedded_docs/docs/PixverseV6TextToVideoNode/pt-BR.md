# PixVerse V6 Texto para Vídeo

PixVerse V6 Text to Video gera um vídeo a partir de um prompt de texto usando o modelo V6 da PixVerse. O nó envia o prompt juntamente com a resolução, duração, proporção de aspecto e outras configurações escolhidas para a PixVerse, aguarda a conclusão da geração e então retorna o vídeo resultante — incluindo uma trilha de áudio nativa quando a geração de áudio está habilitada.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `modelo` | Configurações do modelo e da geração. Selecione o modelo e configure suas opções de geração. | DYNAMIC_COMBO | Sim | "PixVerse V6" |

### Entradas do PixVerse V6

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt para a geração do vídeo. (padrão: "") | STRING | Sim | 1–5000 caracteres |
| `aspect_ratio` | Proporção de aspecto da saída. Selecione uma das proporções de aspecto suportadas pelo PixVerse V6. | COMBO | Sim | Várias opções disponíveis |
| `quality` | Resolução da saída. Define o lado maior: 360p é 640px, 540p 1024px, 720p 1280px, 1080p 1920px. (padrão: "720p") | COMBO | Sim | "360p"<br>"540p"<br>"720p"<br>"1080p" |
| `duration_seconds` | Duração do vídeo gerado em segundos. (padrão: 5) | INT | Sim | 1–15 |
| `generate_audio` | Gera uma trilha de áudio nativa juntamente com o vídeo. (padrão: True) | BOOLEAN | Sim | True<br>False |
| `multi_clip` | Permite que o modelo corte o vídeo em várias cenas em vez de uma única tomada contínua. (padrão: False) | BOOLEAN | Sim | True<br>False |
| `seed` | Semente para a geração do vídeo. A PixVerse a registra, mas não reproduz uma execução a partir dela. Suporta aleatoriedade após a geração. (padrão: 42) | INT | Sim | 0–2147483647 |
| `negative_prompt` | Uma descrição textual opcional de elementos indesejados no vídeo. (padrão: "") | STRING | Não | 0–2048 caracteres |
| `style` | Um estilo visual opcional aplicado a todo o vídeo. (padrão: "none") | COMBO | Não | Várias opções disponíveis |

**Observação:** O `prompt` é obrigatório e, após remover espaços em branco das extremidades, não pode ficar vazio; seu comprimento máximo é de 5000 caracteres. O `negative_prompt` é limitado a 2048 caracteres. Definir `style` como "none" (o padrão) significa que nenhum estilo visual é aplicado. O `seed` é registrado pela PixVerse, mas não pode ser usado para reproduzir a mesma execução. O nó aguarda a PixVerse terminar de gerar o vídeo e então o baixa; se a solicitação falhar — por exemplo, porque a PixVerse já atingiu o número máximo de gerações simultâneas, a conta do provedor está sem créditos ou a moderação de conteúdo rejeita o prompt — o nó retorna um erro.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `VIDEO` | O vídeo gerado. Se `generate_audio` estiver habilitado, o vídeo inclui a trilha de áudio nativa. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseV6TextToVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `4c268be9720a4606e77a9347570ac26b489625fc6b9528b9d3cceb4497d8683b`

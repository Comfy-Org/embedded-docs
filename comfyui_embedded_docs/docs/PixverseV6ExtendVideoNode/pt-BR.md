# PixVerse V6 Estender Vídeo

Este nó dá continuidade a um vídeo existente usando o modelo PixVerse V6, gerando opcionalmente uma trilha de áudio nativa junto com a continuação. O vídeo de origem deve ter menos de 40 segundos e no máximo 1920 pixels em qualquer um dos lados. A saída mantém a resolução do vídeo de origem, portanto a configuração de qualidade controla o quão bem a continuação é renderizada, e não o tamanho do quadro.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `vídeo` | Vídeo a ser continuado. | VIDEO | Sim | Menos de 40 segundos; no máximo 1920 pixels de largura e altura |
| `modelo` | Modelo e configurações de geração. | DYNAMIC_COMBO | Sim | "PixVerse V6" |

### Entradas do PixVerse V6

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt descrevendo como o vídeo deve continuar. (padrão: vazio) | STRING | Sim | 1–5000 caracteres |
| `quality` | Qualidade de renderização da continuação gerada: 1080p parece significativamente melhor que 540p ou 360p. Ela nunca redimensiona — a saída mantém a resolução do vídeo de origem. (padrão: "720p") | COMBO | Sim | "360p"<br>"540p"<br>"720p"<br>"1080p" |
| `duration_seconds` | Duração do vídeo gerado em segundos. (padrão: 5) | INT | Sim | 1–15 |
| `generate_audio` | Gera uma trilha de áudio nativa junto com o vídeo. (padrão: true) | BOOLEAN | Sim | true / false |
| `seed` | Semente para a geração de vídeo. A PixVerse a registra, mas não reproduz uma execução a partir dela. (padrão: 42) | INT | Sim | 0–2147483647 |
| `negative_prompt` | Uma descrição textual opcional de elementos indesejados no vídeo. (padrão: vazio) | STRING | Não | Até 2048 caracteres |
| `style` | Um estilo visual opcional aplicado a todo o vídeo. (padrão: "none") | COMBO | Não | Várias opções disponíveis; "none" é o padrão |

**Nota:** O `video` de origem deve ter menos de 40 segundos e no máximo 1920 pixels tanto na largura quanto na altura; vídeos mais longos ou maiores são rejeitados. A saída gerada mantém a resolução do vídeo de origem, portanto `quality` altera a fidelidade de renderização, não o tamanho do quadro de saída. O `prompt` é obrigatório e deve conter entre 1 e 5000 caracteres após a remoção de espaços em branco. O `negative_prompt`, quando fornecido, é limitado a 2048 caracteres. A `seed` é registrada pela PixVerse, mas não pode ser usada para reproduzir a mesma execução.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `video` | O vídeo de continuação gerado, na mesma resolução do vídeo de origem. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseV6ExtendVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `8bd2a04a5da95b39fb963922e2e54a7aa4efb670260fa38313d21db3af295029`

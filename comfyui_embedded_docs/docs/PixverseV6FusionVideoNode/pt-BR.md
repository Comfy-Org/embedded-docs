# PixVerse V6 Fusão (Referência para Vídeo)

O PixVerse V6 Fusion (Reference to Video) compõe um vídeo a partir de assuntos, fundos e vídeos de referência com o PixVerse. Coloque uma referência na cena nomeando-a no prompt, por exemplo '@Subject1 walks through @Background1'. Conectar um vídeo de referência alterna o modelo para o modo Omni, onde o comprimento da saída corresponde ao vídeo de referência mais longo.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `modelo` | Configurações do modelo e de geração. Seleciona o modelo e expõe suas configurações de geração abaixo. A única opção disponível é "PixVerse V6". | DYNAMIC_COMBO | Sim | "PixVerse V6" |

### Entradas do PixVerse V6

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt para a geração do vídeo. Refira-se às referências conectadas como @Subject1, @Background1, @Video1. Padrão: vazio. | STRING | Sim | 1 a 5000 caracteres |
| `aspect_ratio` | Proporção de tela da saída. A opção "auto" só é permitida quando pelo menos um vídeo de referência está conectado. | COMBO | Sim | "auto"<br>mais as proporções de tela predefinidas do PixVerse V6 |
| `quality` | Resolução da saída. Define a borda longa: 360p é 640px, 540p é 1024px, 720p é 1280px, 1080p é 1920px. Padrão: "720p". | COMBO | Sim | "360p"<br>"540p"<br>"720p"<br>"1080p" |
| `duration_seconds` | Comprimento do vídeo gerado em segundos. Quando vídeos de referência estão conectados, o comprimento da saída segue o vídeo de referência mais longo e esta configuração é ignorada. Padrão: 5. | INT | Sim | 1 a 15 |
| `generate_audio` | Gera uma trilha de áudio nativa junto com o vídeo. Padrão: True. | BOOLEAN | Sim | True<br>False |
| `seed` | Semente para a geração do vídeo. O PixVerse a registra, mas não reproduz uma execução a partir dela. Padrão: 42. | INT | Sim | 0 a 2147483647 |
| `negative_prompt` | Uma descrição textual opcional de elementos indesejados no vídeo. Padrão: vazio. | STRING | Não | Até 2048 caracteres |
| `style` | Um estilo visual opcional aplicado a todo o vídeo. Padrão: "none". | COMBO | Não | "none"<br>mais os estilos predefinidos do PixVerse V6 |

### Entradas de referência

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `sujeitos` | Slot expansível: conecte imagens de referência dos assuntos para colocar na cena. Os slots são nomeados de subject1 a subject8; referencie-os no prompt como @Subject1, @Subject2, e assim por diante. | IMAGE | Não | 0 a 8 imagens |
| `planos de fundo` | Slot expansível: conecte imagens de referência da cena onde os assuntos serão colocados. Os slots são nomeados de background1 a background2; referencie-os no prompt como @Background1, @Background2. | IMAGE | Não | 0 a 2 imagens |
| `vídeos` | Slot expansível: conecte vídeos de referência para aproveitar assuntos, movimento, enquadramento ou estilo. Os slots são nomeados de video1 a video2; referencie-os no prompt como @Video1, @Video2. Cada vídeo deve ter no máximo 15 segundos de duração, e a duração total não pode exceder 15 segundos. Conectar pelo menos um vídeo altera o nó para o modo Omni. | VIDEO | Não | 0 a 2 vídeos<br>máximo de 15 segundos cada<br>15 segundos no total |

Nota: Conecte pelo menos um assunto, fundo ou vídeo de referência. As tags de referência no prompt (por exemplo @Subject1, @Background1, @Video1) devem corresponder aos slots conectados; caso contrário, a solicitação é rejeitada. Quando pelo menos um vídeo de referência está conectado (modo Omni), o comprimento da saída corresponde ao vídeo de referência mais longo, `duration_seconds` é ignorado, `aspect_ratio` pode ser definido como "auto", e até 10 imagens de referência são aceitas. Sem um vídeo de referência, no máximo 7 imagens de referência (assuntos e fundos combinados) são aceitas, e a proporção de tela "auto" não é permitida.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `video` | O vídeo de fusão gerado, baixado do PixVerse. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseV6FusionVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `a83ef07f6f1918921e93fa67c2eca351754794f629aa216ccff21ce80901aebd`

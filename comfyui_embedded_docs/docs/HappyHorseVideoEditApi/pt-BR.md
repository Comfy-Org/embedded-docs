# HappyHorse Edição de Vídeo

Edite um vídeo usando instruções de texto ou imagens de referência com o modelo HappyHorse. A duração da saída é de 3 a 15 segundos e corresponde ao vídeo de entrada; vídeos de entrada com mais de 15 segundos são truncados.

## Entradas

### Entradas Comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | O modelo de edição de vídeo HappyHorse a ser usado. Esta seleção determina quais opções de prompt, resolução, proporção e imagem de referência estão disponíveis. | DICT | Sim | "happyhorse-1.0-video-edit" |
| `video` | O vídeo a ser editado. | VIDEO | Sim | 3 a 60 segundos |
| `seed` | Semente a ser usada para geração (padrão: 0). | INT | Sim | 0 a 2147483647 |
| `watermark` | Se deve adicionar uma marca d'água gerada por IA ao resultado (padrão: False). | BOOLEAN | Não | True<br>False |

### Entradas do happyhorse-1.0-video-edit

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Instruções de edição ou requisitos de transferência de estilo. Deve ter pelo menos 1 caractere. | STRING | Sim | - |
| `resolution` | A resolução de saída. | STRING | Sim | "720P"<br>"1080P" |
| `ratio` | Proporção de aspecto. Se não for alterada, aproxima a proporção do vídeo de entrada. | STRING | Sim | "16:9"<br>"9:16"<br>"1:1"<br>"4:3"<br>"3:4" |

### Entradas de Referência

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | Slot expansível: conecte de 0 a 5 imagens de referência (`image1`...`image5`) para guiar a edição. | IMAGE | Não | 0 a 5 imagens |

**Nota:** O vídeo de entrada deve ter de 3 a 60 segundos. A duração da saída é de 3 a 15 segundos e corresponde ao vídeo de entrada; vídeos de entrada com mais de 15 segundos são truncados. O `prompt` deve ter pelo menos 1 caractere.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `video` | O vídeo de saída editado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HappyHorseVideoEditApi/pt-BR.md)

---
**Source fingerprint (SHA-256):** `396cad4b5a06d457746a421050df98c892fa9db6019e3de983b4d0c417842b57`

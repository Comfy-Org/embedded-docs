# PixVerse V6 Imagem para Vídeo

Este nó anima uma imagem de entrada com o modelo PixVerse V6 e retorna um vídeo, opcionalmente com uma trilha de áudio nativa. O vídeo de saída mantém a proporção da imagem de entrada.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `imagem` | A imagem de entrada a ser animada. | IMAGE | Sim | Imagem única |
| `modelo` | Modelo e configurações de geração. | DYNAMIC_COMBO | Sim | "PixVerse V6" |

### Entradas do PixVerse V6

Estas configurações aparecem quando o modelo "PixVerse V6" está selecionado.

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt para a geração do vídeo (padrão: vazio). | STRING | Sim | 1 a 5000 caracteres |
| `quality` | Resolução de saída. Define o lado maior: 360p é 640px, 540p é 1024px, 720p é 1280px, 1080p é 1920px (padrão: "720p"). | COMBO | Sim | "360p"<br>"540p"<br>"720p"<br>"1080p" |
| `duration_seconds` | Duração do vídeo gerado em segundos (padrão: 5). | INT | Sim | 1 a 15 |
| `generate_audio` | Gera uma trilha de áudio nativa junto com o vídeo (padrão: true). | BOOLEAN | Sim | true or false |
| `multi_clip` | Permite que o modelo corte o vídeo em vários planos em vez de uma tomada contínua (padrão: false). | BOOLEAN | Sim | true or false |
| `seed` | Semente para geração de vídeo. O PixVerse a registra, mas não reproduz uma execução a partir dela (padrão: 42, o controle após gerar está habilitado). | INT | Sim | 0 a 2147483647 |
| `negative_prompt` | Uma descrição de texto opcional de elementos indesejados no vídeo (padrão: vazio). | STRING | Não | Até 2048 caracteres |
| `style` | Um estilo visual opcional aplicado a todo o vídeo (padrão: nenhum). | COMBO | Não | Várias opções disponíveis (predefinições de estilo do PixVerse V6) |

Observação: O prompt deve conter pelo menos um caractere que não seja espaço em branco e no máximo 5000 caracteres; o prompt negativo, se fornecido, deve ter no máximo 2048 caracteres. O vídeo de saída sempre corresponde à proporção da imagem de entrada, portanto, nenhuma configuração de proporção é necessária. Apenas uma única imagem de entrada é aceita. O PixVerse pode rejeitar uma solicitação quando a moderação de conteúdo falha, quando a conta do provedor está sem créditos ou quando o número máximo de gerações simultâneas já está em execução.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|-------------|-------------|-----------|
| `video` | O vídeo gerado, incluindo a trilha de áudio nativa quando `generate_audio` está habilitado. A proporção corresponde à imagem de entrada. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseV6ImageToVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `6ecf958e510e7afc43f5f0e4e5dfd2b789aea02bec882d928326732501cee7b3`

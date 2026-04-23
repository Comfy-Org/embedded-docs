> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2ImageToVideoApi/pt-BR.md)

Este é um especialista em tradução técnica especializado em documentação de nós ComfyUI do inglês para português brasileiro.

## Regras de Tradução

1. **Conteúdo que NÃO deve ser traduzido:**
   - Nomes de parâmetros entre crases: `image`, `seed`, `model`
   - Tipos de dados em MAIÚSCULAS: IMAGE, STRING, INT, FLOAT, MODEL, CONDITIONING, etc.
   - Valores na coluna Range: números, "auto", nomes de opções
   - Código, caminhos de arquivos

2. **Conteúdo que DEVE ser traduzido:**
   - Títulos de seções: ## Visão Geral, ## Entradas, ## Saídas
   - Todo o texto descritivo e explicativo
   - Descrições de parâmetros

3. **Qualidade da tradução:**
   - Use português brasileiro padrão
   - Mantenha um tom profissional mas acessível
   - Garanta precisão técnica
   - Use terminologia técnica padrão em português brasileiro

4. **Formato:**
   - Mantenha toda a formatação Markdown
   - Preserve a estrutura das tabelas
   - Não adicione nenhuma nota ou link no início do documento (será adicionado automaticamente)

Por favor, traduza a seguinte documentação para português brasileiro, sem incluir a nota inicial do documento:

O nó Wan 2.7 Image to Video gera um vídeo a partir de uma imagem de primeiro quadro. Opcionalmente, você pode fornecer uma imagem de último quadro para criar uma transição entre os dois, ou fornecer um arquivo de áudio para guiar o movimento e o ritmo do vídeo. O nó usa um modelo de IA para animar a cena com base na sua descrição textual.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `model` | COMBO | Sim | `"wan2.7-i2v"` | O modelo de IA a ser usado para geração de vídeo. |
| `model.prompt` | STRING | Sim | - | Uma descrição textual dos elementos e características visuais que você deseja no vídeo. Suporta inglês e chinês. |
| `model.negative_prompt` | STRING | Sim | - | Uma descrição textual de elementos ou características que você deseja que o modelo evite. |
| `model.resolution` | COMBO | Sim | `"720P"`<br>`"1080P"` | A resolução do vídeo de saída. |
| `model.duration` | INT | Sim | 2 a 15 | A duração do vídeo gerado em segundos (padrão: 5). |
| `first_frame` | IMAGE | Sim | - | A imagem a ser usada como primeiro quadro do vídeo. A proporção de aspecto do vídeo de saída é derivada desta imagem. |
| `last_frame` | IMAGE | Não | - | Uma imagem opcional a ser usada como último quadro. Quando fornecida, o modelo gera um vídeo que faz a transição do primeiro quadro para este último quadro. |
| `audio` | AUDIO | Não | - | Um arquivo de áudio opcional para conduzir a geração do vídeo, útil para sincronização labial ou movimento sincronizado com batidas. A duração deve estar entre 2 e 30 segundos. Se não for fornecido, o modelo gerará música de fundo ou efeitos sonoros correspondentes. |
| `seed` | INT | Sim | 0 a 2147483647 | Um valor de semente para controlar a aleatoriedade da geração (padrão: 0). |
| `prompt_extend` | BOOLEAN | Sim | - | Quando ativado, o nó usará assistência de IA para aprimorar seu prompt de texto (padrão: True). Esta é uma configuração avançada. |
| `watermark` | BOOLEAN | Sim | - | Quando ativado, uma marca d'água gerada por IA será adicionada ao vídeo final (padrão: False). Esta é uma configuração avançada. |

**Nota:** A entrada `audio` tem uma restrição de duração. Se fornecida, o arquivo de áudio deve ter entre 2 e 30 segundos de duração.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `output` | VIDEO | O arquivo de vídeo gerado. |
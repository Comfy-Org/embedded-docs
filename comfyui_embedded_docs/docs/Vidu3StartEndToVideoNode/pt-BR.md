# Geração de Vídeo Quadro Inicial/Final Vidu Q3

Este nó gera um vídeo criando uma transição entre um frame inicial e um frame final, guiada por um prompt de texto. Ele usa o modelo Vidu Q3 para interpolar entre as duas imagens e produz um vídeo na duração e resolução escolhidas.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `modelo` | Modelo a ser usado para geração de vídeo. Selecionar uma opção revela parâmetros de configuração adicionais para `resolution`, `duration` e `audio`. | DYNAMIC_COMBO | Sim | `"viduq3-pro"`<br>`"viduq3-turbo"` |
| `quadro inicial` | A imagem inicial da sequência de vídeo. | IMAGE | Sim | - |
| `quadro final` | A imagem final da sequência de vídeo. | IMAGE | Sim | - |
| `prompt` | Descrição do prompt (máx. 2000 caracteres). | STRING | Sim | Até 2000 caracteres |
| `semente` | Valor de seed usado para controlar a aleatoriedade da geração. Possui uma opção de controle após geração (padrão: 1). | INT | Sim | 0 a 2147483647 |

### Entradas do viduq3-pro e viduq3-turbo

Os parâmetros a seguir são compartilhados por ambas as opções de modelo (`viduq3-pro` e `viduq3-turbo`). Eles aparecem após um modelo ser selecionado.

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `resolution` | Resolução do vídeo de saída. | COMBO | Sim | `"720p"`<br>`"1080p"` |
| `duration` | Duração do vídeo de saída em segundos (padrão: 5). | INT | Sim | 1 a 16 |
| `audio` | Quando habilitado, gera vídeo com som (incluindo diálogos e efeitos sonoros) (padrão: False). | BOOLEAN | Sim | `True`<br>`False` |

**Observação:** As imagens `first_frame` e `end_frame` devem ter proporções de aspecto semelhantes. A proporção de aspecto das duas imagens deve permanecer entre 80% e 125% uma da outra (proximidade relativa entre 0,8 e 1,25).

**Observação:** Para `viduq3-turbo`, o preço é 0,06 USD por segundo em 720p e 0,08 USD por segundo em 1080p. Para `viduq3-pro`, o preço é 0,15 USD por segundo em 720p e 0,16 USD por segundo em 1080p.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|-------------|-------------|-----------|
| `video` | O arquivo de vídeo gerado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu3StartEndToVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `c917867c5a7b68a1286f445025070f9a55d8d10091d9562960e0428cbedf25e4`

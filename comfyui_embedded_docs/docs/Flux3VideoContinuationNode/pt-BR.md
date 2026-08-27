# Flux 3 Continuação de Vídeo

Este nó dá continuidade a um clipe de vídeo existente com o FLUX 3: o novo clipe dá continuidade aos quadros finais do vídeo fornecido. Ele envia seu clipe de origem, transmite o prompt e as configurações para o serviço de geração e retorna o vídeo de continuação resultante assim que estiver pronto.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|---------------|-------------|-----------|
| `vídeo` | O clipe a ser continuado. | VIDEO | Sim | Clipe de vídeo único |
| `prompt` | O que a continuação deve mostrar; o prompt é interpretado e expandido antes da geração. (padrão: "") | STRING | Sim | Texto não vazio (mínimo de 1 caractere) |
| `proporção` | Proporção de aspecto da saída. 'auto' escolhe uma com base no prompt e nas entradas. (padrão: "auto") | COMBO | Sim | "auto" (padrão)<br>Múltiplas opções predefinidas |
| `duração` | Duração do clipe em segundos. 'auto' ajusta a duração ao conteúdo. (padrão: "auto") | COMBO | Sim | "auto" (padrão)<br>Valores numéricos em segundos |
| `resolução` | Resolução da saída. (padrão: "720p") | COMBO | Sim | "720p" (padrão)<br>"1080p"<br>Outras opções predefinidas |
| `gerar áudio` | Gerar áudio sincronizado (ambiente, fala, efeitos). Desativado produz um vídeo sem trilha de áudio. (padrão: true) | BOOLEAN | Sim | true<br>false |
| `tolerância de segurança` | Tolerância de moderação, 0 é a mais rigorosa. Solicitações que enviam imagens ou vídeo são limitadas a 2 independentemente do valor definido aqui. (parâmetro avançado, padrão: 2) | INT | Sim | 0 - 4 (máximo efetivo: 2 para solicitações de vídeo) |
| `semente` | Semente para determinar se o nó deve ser executado novamente; o FLUX 3 escolhe sua própria semente, portanto os resultados reais são não determinísticos independentemente desse valor. (parâmetro avançado, padrão: 42) | INT | Sim | 0 - 4294967295 (0xFFFFFFFF) |

### Notas

- O `prompt` deve conter pelo menos um caractere, caso contrário a geração falha. Embora o campo tenha como padrão uma string vazia, é necessário um prompt não vazio para executar o nó.
- O `safety_tolerance` aceita qualquer valor de 0 a 4, mas como este nó envia um vídeo para a API, a tolerância efetiva é limitada a 2, independentemente do valor selecionado.
- Quando `duration` é definido como um número, ele é convertido em um número inteiro de segundos. O valor especial "auto" permite que o serviço ajuste a duração ao conteúdo.
- As listas exatas de opções para `aspect_ratio`, `duration` e `resolution` são definidas internamente pelo nó. As opções de resolução incluem pelo menos "720p" (padrão) e "1080p". O preço é calculado com base na `resolution` e `duration` selecionadas; "1080p" é cobrado a $0.7579 por segundo, enquanto outras resoluções são cobradas a $0.5863 por segundo.
- Os campos de autenticação e identificação do nó (`auth_token_comfy_org`, `api_key_comfy_org`, `unique_id`) são ocultados e tratados automaticamente pela plataforma.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|---------------|-------------|---------------|
| `video` | O clipe de continuação gerado pelo FLUX 3, que dá continuidade ao final do vídeo de origem. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux3VideoContinuationNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `129ad0eb62c368854cebb010cc886aecac4caab00f9111143b883d028d7c30d9`

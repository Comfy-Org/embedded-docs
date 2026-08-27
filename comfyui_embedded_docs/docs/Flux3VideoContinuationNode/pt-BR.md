# Flux3VideoContinuationNode

Este nó dá continuidade a um videoclipe existente com o FLUX 3, fazendo com que o novo clipe continue a partir dos quadros finais do vídeo fornecido. Ele envia seu clipe de origem, envia o prompt e as configurações ao serviço de geração e retorna o vídeo de continuação resultante assim que estiver pronto.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `vídeo` | O clipe a ser continuado. | VIDEO | Sim | Videoclipe único |
| `prompt` | O que a continuação deve mostrar; o prompt é interpretado e expandido antes da geração. (padrão: "") | STRING | Sim | Texto não vazio (mínimo de 1 caractere) |
| `proporção` | Proporção de aspecto da saída. 'auto' escolhe uma a partir do prompt e das entradas. (padrão: "auto") | STRING | Sim | Múltiplas opções predefinidas (padrão: "auto") |
| `duração` | Duração do clipe em segundos. 'auto' ajusta a duração ao conteúdo. (padrão: "auto") | STRING | Sim | "auto" (padrão)<br>Valores numéricos em segundos |
| `resolução` | Resolução da saída. (padrão: "720p") | STRING | Sim | Múltiplas opções predefinidas (padrão: "720p") |
| `gerar áudio` | Gera áudio sincronizado (ambiente, fala, efeitos). Desativado produz um vídeo sem trilha de áudio. (padrão: true) | BOOLEAN | Sim | true<br>false |
| `tolerância de segurança` | Tolerância de moderação; 0 é o mais estrito. Solicitações que enviam imagens ou vídeo são limitadas a 2, independentemente do valor definido aqui. (parâmetro avançado, padrão: 2) | INT | Sim | 0 - 4 (máximo efetivo: 2 para solicitações de vídeo) |
| `semente` | Semente para determinar se o nó deve ser executado novamente; o FLUX 3 escolhe sua própria semente, portanto os resultados reais são não determinísticos independentemente desse valor. (parâmetro avançado, padrão: 42) | INT | Sim | 0 - 4294967295 (0xFFFFFFFF) |

### Notas

- `prompt` deve conter pelo menos um caractere; caso contrário, a geração falha. Embora o campo tenha como padrão uma string vazia, um prompt não vazio é necessário para executar o nó.
- `safety_tolerance` aceita qualquer valor de 0 a 4, mas, como este nó envia um vídeo para a API, a tolerância efetiva é limitada a 2, independentemente do valor selecionado.
- Quando `duration` é definido como um número, ele é convertido em um número inteiro de segundos. O valor especial "auto" permite que o serviço ajuste a duração ao conteúdo.
- As listas exatas de opções de `aspect_ratio`, `duration` e `resolution` são definidas internamente pelo nó. As opções de resolução incluem pelo menos "720p" (o padrão) e "1080p", que usa uma taxa de preço diferente.
- Os campos de autenticação e identificação do nó (`auth_token_comfy_org`, `api_key_comfy_org`, `unique_id`) são ocultos e gerenciados automaticamente pela plataforma.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `video` | O clipe de continuação gerado pelo FLUX 3, que dá continuidade a partir do final do vídeo de origem. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux3VideoContinuationNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `4b3a3df86b870edd696d10d352c7123b9c6c60ce0b57910529fca60615efa9f9`

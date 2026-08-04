# LumaRay32ExtendVideoNode

Luma Ray 3.2 Extend Video continua uma geração de vídeo anterior do Luma Ray 3.2 criando um novo segmento de 5 segundos, após o clipe original (para frente) ou antes dele (para trás). Conecte a saída `generation_id` de um nó Luma Ray 3.2 anterior para usar esse clipe como quadro inicial (para frente) ou final (para trás) da extensão.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|---------------|-------------|-------|
| `source_generation_id` | ID de geração do vídeo Ray 3.2 anterior a ser estendido. Conecte a saída `generation_id` de outro nó Luma Ray 3.2. Este valor é obrigatório e não deve estar vazio. | STRING | Sim | - |
| `direction` | Para frente continua após o clipe anterior; para trás é anteposto antes dele. Selecionar "Forward (continue after)" também adiciona a opção `loop`. | COMBO | Sim | "Forward (continuar após)"<br>"Backward (introdução antes)" |
| `loop` | Repete o vídeo estendido sem emendas (somente extensão para frente). Disponível apenas quando `direction` é "Forward (continue after)". Padrão: False. | BOOLEAN | Não | Verdadeiro<br>Falso |
| `prompt` | Prompt de texto para o novo conteúdo. Deve ter entre 1 e 6000 caracteres. | STRING | Sim | - |
| `resolution` | Resolução de saída para o segmento de vídeo estendido. Padrão: "720p". | COMBO | Sim | "540p"<br>"720p"<br>"1080p" |
| `seed` | Semente aleatória para resultados de geração reproduzíveis. | INT | Sim | - |

**Nota:** O parâmetro `loop` está disponível apenas quando `direction` está definido como "Forward (continuar após)". Ao usar "Backward (introdução antes)", a opção de loop não está disponível. O `prompt` deve ter entre 1 e 6000 caracteres.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|---------------|-------------|---------------|
| `VIDEO` | O segmento de vídeo estendido gerado de 5 segundos. | VIDEO |
| `generation_id` | Identificador único para esta geração, que pode ser conectado a outro nó Luma Ray 3.2 Extend Video para extensões adicionais. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaRay32ExtendVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `a67ca53d4bcb9f3fd82bc0482b579f5f7fe4bf866f8d83cb922e1082ad320057`

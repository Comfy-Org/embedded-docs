# Salvar Áudio (MP3)

O nó SaveAudioMP3 salva dados de áudio como um arquivo MP3. Ele recebe uma entrada de áudio e a grava no diretório de saída com um prefixo de nome de arquivo personalizável e uma configuração de qualidade. Este nó está obsoleto e pode ser removido em versões futuras.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-----------|---------------|-------------|-------|
| `audio` | Os dados de áudio a serem salvos como arquivo MP3 | AUDIO | Sim | - |
| `filename_prefix` | O prefixo para o nome do arquivo de saída (padrão: "audio/ComfyUI") | STRING | Não | - |
| `quality` | A configuração de qualidade de codificação MP3 (padrão: "V0"). V0 usa taxa de bits variável para alta qualidade; 128k e 320k usam taxas de bits fixas de 128 e 320 kbps | COMBO | Não | `"V0"`<br>`"128k"`<br>`"320k"` |
| `prompt` | Dados internos do prompt, fornecidos automaticamente pelo sistema | PROMPT | Não | - |
| `extra_pnginfo` | Informações PNG adicionais, fornecidas automaticamente pelo sistema | EXTRA_PNGINFO | Não | - |

**Observação:** Se a entrada `audio` for None (por exemplo, quando o vídeo de origem não possui trilha de áudio), o nó gera um ValueError.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|---------------|-----------|---------------|
| `audio` | Os dados de áudio que foram salvos como arquivo MP3 | AUDIO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudioMP3/pt-BR.md)

---
**Source fingerprint (SHA-256):** `7d3b439dfd7cb211dd6568f6b5124bb225909dcf0ae150addc4ca226d947a4f0`

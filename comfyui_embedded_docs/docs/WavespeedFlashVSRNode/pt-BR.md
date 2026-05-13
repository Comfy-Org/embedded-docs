> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WavespeedFlashVSRNode/pt-BR.md)

O nó WavespeedFlashVSRNode é um upscaler de vídeo rápido e de alta qualidade que aumenta a resolução e restaura a nitidez de vídeos com baixa resolução ou desfocados. Ele processa um vídeo de entrada e gera um novo vídeo em uma resolução superior selecionada pelo usuário.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Faixa | Descrição |
|-----------|---------------|-------------|-------|-----------|
| `vídeo` | VIDEO | Sim | N/A | O arquivo de vídeo de entrada a ser ampliado. Deve estar no formato contêiner MP4 com duração entre 5 segundos e 10 minutos. |
| `resolução_alvo` | STRING | Sim | `"720p"`<br>`"1080p"`<br>`"2K"`<br>`"4K"` | A resolução desejada para o vídeo de saída ampliado. |

**Restrições de Entrada:**

* O arquivo de `video` de entrada deve estar no formato contêiner MP4.
* A duração do `video` de entrada deve estar entre 5 segundos e 10 minutos (600 segundos).

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|---------------|---------------|-----------|
| `output` | VIDEO | O arquivo de vídeo ampliado na resolução alvo selecionada. |

---
**Source fingerprint (SHA-256):** `9a495889753ac866177921727228846d8ef9516c54ccd9aa425350b87237c397`

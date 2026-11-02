# Pruna P-Video Upscale

O Pruna P-Video Upscale amplia um vídeo para 720p, 1080p, 2K ou 4K, mantendo sua proporção e faixa de áudio. O clipe é enviado ao Pruna, a previsão é consultada periodicamente e o vídeo ampliado é retornado. Uma fonte que já está no tamanho alvo ou acima dele mantém suas dimensões e é apenas aprimorada.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `video` | Vídeo a ser ampliado, até 512 MiB. Vídeos maiores que 10 megapixels só podem ser enviados para o alvo 2K ou 4K. | VIDEO | Sim | Até 512 MiB |
| `target` | Área de pixels da saída: 720p tem cerca de 0,9 megapixel, 1080p 2,1, 2K 3,7 e 4K 8,3. O clipe mais longo é limitado pelo alvo: 2400, 1200, 600 ou 300 quadros, cerca de 100, 50, 25 ou 12,5 segundos a 24 fps (padrão: "1080p"). | COMBO | Sim | "720p"<br>"1080p"<br>"2K"<br>"4K" |
| `fps` | Taxa de quadros da saída (padrão: "source"). "source" mantém a taxa do vídeo, até 60; uma taxa maior é interpolada. Saída acima de 30 fps custa o dobro. | COMBO | Sim | "source"<br>"16"<br>"24"<br>"25"<br>"30"<br>"48"<br>"50"<br>"60" |
| `turbo` | Ampliação mais rápida com detalhes mais suaves, pelo mesmo preço (padrão: false). | BOOLEAN | Não | true<br>false |

### Restrições de parâmetros

- O clipe deve ter 512 MiB ou menos, medido após ser recodificado para H.264 MP4.
- O limite de quadros é contado a até 30 fps: 2400 quadros para 720p, 1200 para 1080p, 600 para 2K e 300 para 4K. Um clipe mais longo precisa de um alvo menor, um `fps` menor ou um corte mais curto.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `video` | O vídeo ampliado com seu áudio original. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrunaPVideoUpscaleNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `e8fc88b6177085e0852d17ff92b0a22a26c9914c012a9a244b19da9b2c0e38c2`

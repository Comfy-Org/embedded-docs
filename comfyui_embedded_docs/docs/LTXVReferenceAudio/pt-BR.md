> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVReferenceAudio/pt-BR.md)

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVReferenceAudio/pt-BR.md)

O nó LTXV Reference Audio é utilizado para transferência de identidade do locutor na geração de áudio. Ele codifica um clipe de áudio de referência no condicionamento de um modelo, permitindo que o áudio gerado adote as características vocais do locutor. Também pode aplicar orientação de identidade, que executa uma etapa extra de processamento para amplificar o efeito da identidade do locutor.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `model` | MODEL | Sim | - | O modelo a ser ajustado com orientação de identidade. |
| `positive` | CONDITIONING | Sim | - | A entrada de condicionamento positivo. |
| `negative` | CONDITIONING | Sim | - | A entrada de condicionamento negativo. |
| `reference_audio` | AUDIO | Sim | - | Clipe de áudio de referência cuja identidade do locutor será transferida. ~5 segundos recomendados (duração do treinamento). Clipes mais curtos ou mais longos podem degradar a transferência de identidade vocal. |
| `audio_vae` | VAE | Sim | - | VAE de áudio LTXV para codificar o áudio de referência. |
| `identity_guidance_scale` | FLOAT | Não | 0.0 - 100.0 | Intensidade da orientação de identidade. Executa uma passagem extra sem referência a cada etapa para amplificar a identidade do locutor. Defina como 0 para desabilitar (sem passagem extra). (padrão: 3.0) |
| `start_percent` | FLOAT | Não | 0.0 - 1.0 | Início da faixa sigma onde a orientação de identidade está ativa. (padrão: 0.0) |
| `end_percent` | FLOAT | Não | 0.0 - 1.0 | Fim da faixa sigma onde a orientação de identidade está ativa. (padrão: 1.0) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `model` | MODEL | O modelo ajustado com a função de orientação de identidade. |
| `positive` | CONDITIONING | O condicionamento positivo, agora contendo os dados de áudio de referência codificados. |
| `negative` | CONDITIONING | O condicionamento negativo, agora contendo os dados de áudio de referência codificados. |

---
**Source fingerprint (SHA-256):** `0b87fb135ba8e752f4114cb47152503b0ec548eefcaa03f99f1cbdda6664874c`

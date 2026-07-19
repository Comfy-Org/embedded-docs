# HeyGenVideoTranslateNode

Traduza um vídeo falado para outro idioma com clonagem de voz e sincronização labial. Este nó clona a voz do falante original e reanima a boca para corresponder à fala traduzida, produzindo um resultado de aparência natural.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-----------|--------------|-------------|-------|
| `video` | Vídeo com fala a ser traduzida. | VIDEO | Sim | - |
| `output_language` | Idioma de destino para o vídeo traduzido. | STRING | Sim | "Árabe"<br>"Bengali"<br>"Chinês"<br>"Dinamarquês"<br>"Holandês"<br>"Inglês"<br>"Francês"<br>"Alemão"<br>"Grego"<br>"Hindi"<br>"Indonésio"<br>"Italiano"<br>"Japonês"<br>"Coreano"<br>"Malaio"<br>"Polonês"<br>"Português"<br>"Russo"<br>"Espanhol"<br>"Sueco"<br>"Tâmil"<br>"Telugu"<br>"Tailandês"<br>"Turco"<br>"Ucraniano"<br>"Vietnamita" |
| `mode` | 'speed' é mais rápido; 'precision' produz sincronização labial de maior qualidade pelo dobro do preço. | STRING | Sim | "speed"<br>"precision" |
| `translate_audio_only` | Apenas troca a trilha de áudio, mantendo os movimentos originais da boca (sem sincronização labial). (padrão: False) | BOOLEAN | Não | Verdadeiro<br>Falso |
| `speaker_count` | Número de falantes no vídeo. 0 = detectar automaticamente. (padrão: 0) | INT | Não | 0 a 10 |
| `seed` | Não enviado ao HeyGen; altere-o para forçar uma nova execução. (padrão: 42) | INT | Não | 0 a 2147483647 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|---------------|-----------|--------------|
| `video` | O vídeo traduzido com clonagem de voz e sincronização labial aplicadas. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenVideoTranslateNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `31056060b6309b8ec28b37b353322403e173fd2862b56021392dba24e7a15f69`

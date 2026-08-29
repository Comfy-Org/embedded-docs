# HeyGen Video Translate

Traduza um vídeo falado para outro idioma com clonagem de voz e sincronização labial. Este nó clona a voz do falante original e reanima a boca para acompanhar a fala traduzida, produzindo um resultado de aparência natural.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|---------------|-------------|-----------|
| `vídeo` | Vídeo com fala para traduzir. | VIDEO | Sim | - |
| `idioma de saída` | Idioma de destino para o vídeo traduzido. | COMBO | Sim | "Arabic"<br>"Bengali"<br>"Chinese"<br>"Danish"<br>"Dutch"<br>"English"<br>"French"<br>"German"<br>"Greek"<br>"Hindi"<br>"Indonesian"<br>"Italian"<br>"Japanese"<br>"Korean"<br>"Malay"<br>"Polish"<br>"Portuguese"<br>"Russian"<br>"Spanish"<br>"Swedish"<br>"Tamil"<br>"Telugu"<br>"Thai"<br>"Turkish"<br>"Ukrainian"<br>"Vietnamese" |
| `modo` | 'speed' é mais rápido; 'precision' produz sincronização labial de maior qualidade a um preço mais alto. (padrão: "speed") | COMBO | Sim | "speed"<br>"precision" |
| `somente áudio traduzido` | Apenas troca a trilha de áudio, mantendo os movimentos originais da boca (sem sincronização labial). (padrão: False) | BOOLEAN | Não | True<br>False |
| `número de locutores` | Número de falantes no vídeo. 0 = detectar automaticamente. Valores acima de 0 são enviados à API como o número de falantes. (padrão: 0) | INT | Não | 0 a 10 |
| `semente` | Não é enviado à HeyGen; altere-o para forçar uma nova execução. (padrão: 42) | INT | Não | 0 a 2147483647 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|---------------|-------------|---------------|
| `video` | O vídeo traduzido com clonagem de voz e sincronização labial aplicadas. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenVideoTranslateNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `709438c0c713d6db750643cc48f75352c6f293ae1ff2fd82c1bacb03b2581923`

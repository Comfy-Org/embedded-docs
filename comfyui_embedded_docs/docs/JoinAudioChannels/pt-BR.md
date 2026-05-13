> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/JoinAudioChannels/pt-BR.md)

O nó **Join Audio Channels** combina duas entradas de áudio mono separadas em uma única saída de áudio estéreo. Ele recebe um canal esquerdo e um canal direito, garante que tenham taxas de amostragem e durações compatíveis e os mescla em uma forma de onda de áudio de dois canais.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|-----------|----------|-------|-------------|
| `audio_left` | AUDIO | Sim | | Os dados de áudio mono a serem usados como canal esquerdo no áudio estéreo resultante. |
| `audio_right` | AUDIO | Sim | | Os dados de áudio mono a serem usados como canal direito no áudio estéreo resultante. |

**Observação:** Ambos os fluxos de áudio de entrada devem ser mono (canal único). Se tiverem taxas de amostragem diferentes, o canal com a taxa mais baixa será automaticamente reamostrado para corresponder à taxa mais alta. Se os fluxos de áudio tiverem durações diferentes, eles serão cortados para a duração do mais curto.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `audio` | AUDIO | O áudio estéreo resultante, contendo os canais esquerdo e direito unidos. |

---
**Source fingerprint (SHA-256):** `6dced8c2288fb8f214e04b621ed3ab934231983d7987ff08aa43da6814331be0`

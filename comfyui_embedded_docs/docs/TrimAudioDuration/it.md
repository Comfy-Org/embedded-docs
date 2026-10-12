# Taglia Durata Audio

Il nodo TrimAudioDuration consente di ritagliare un segmento temporale specifico da un file audio. È possibile specificare quando iniziare il ritaglio e quanto deve durare il clip audio risultante. Il nodo funziona convertendo i valori temporali in posizioni dei frame audio ed estraendo la porzione corrispondente della forma d'onda audio.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `audio` | L'audio di input da ritagliare | AUDIO | Sì | - |
| `start_index` | Tempo di inizio in secondi, può essere negativo per contare dalla fine (supporta valori inferiori al secondo). Predefinito: 0.0 | FLOAT | Sì | da -0xffffffffffffffff a 0xffffffffffffffff |
| `duration` | Durata in secondi. Predefinito: 60.0 | FLOAT | Sì | da 0.0 a 0xffffffffffffffff |

**Nota:** Il tempo di inizio deve essere minore del tempo di fine e rientrare nella durata dell'audio. I valori di inizio negativi vengono contati a ritroso dalla fine dell'audio. Se il tempo di inizio è negativo, viene convertito in una posizione di frame contando dalla fine dell'audio. I frame di inizio e fine vengono limitati ai confini dell'audio. Se il tempo di inizio è uguale o superiore al tempo di fine, il nodo genererà un errore.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `audio` | Il segmento audio ritagliato con il tempo di inizio e la durata specificati | AUDIO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TrimAudioDuration/it.md)

---
**Source fingerprint (SHA-256):** `4f8c9f966fec8c1d1a1a2bb531014fe7460d61abbafdc367adb667a5044752ef`

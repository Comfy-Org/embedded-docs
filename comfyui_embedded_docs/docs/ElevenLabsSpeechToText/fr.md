# ElevenLabs Speech to Text

Le nœud ElevenLabs Speech to Text transcrit l'audio en texte à l'aide de l'API ElevenLabs. Il prend en charge la détection automatique de la langue, la diarisation des locuteurs (identification des différents locuteurs) et l'étiquetage des événements audio (annotation des sons comme les rires ou la musique dans la transcription).

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Modèle à utiliser pour la transcription. La sélection de ce modèle révèle des paramètres supplémentaires. | DYNAMIC_COMBO | Oui | `"scribe_v2"` |
| `audio` | Audio à transcrire. | AUDIO | Oui | - |
| `language_code` | Code de langue ISO-639-1 ou ISO-639-3 (par ex. 'en', 'es', 'fra'). Laissez vide pour la détection automatique. (par défaut : "") | STRING | Non | - |
| `num_speakers` | Nombre maximal de locuteurs à prédire. Mettez 0 pour la détection automatique. (par défaut : 0) | INT | Non | 0 - 32 |
| `seed` | Graine pour la reproductibilité (déterminisme non garanti). (par défaut : 1) | INT | Non | 0 - 2147483647 |

### Entrées Scribe v2

Ces paramètres sont affichés lorsque le modèle `"scribe_v2"` est sélectionné.

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `tag_audio_events` | Annoter les sons comme (rires), (musique), etc. dans la transcription. (par défaut : False) | BOOLEAN | Non | - |
| `diarize` | Annoter quel locuteur parle. (par défaut : False) | BOOLEAN | Non | - |
| `diarization_threshold` | Sensibilité de séparation des locuteurs. Des valeurs plus faibles sont plus sensibles aux changements de locuteur. Utilisé uniquement lorsque `diarize` est activé. (par défaut : 0.22) | FLOAT | Non | 0.1 - 0.4 |
| `temperature` | Contrôle du caractère aléatoire. 0.0 utilise la valeur par défaut du modèle. Des valeurs plus élevées augmentent le caractère aléatoire. (par défaut : 0.0) | FLOAT | Non | 0.0 - 2.0 |
| `timestamps_granularity` | Précision temporelle pour les mots de la transcription. (par défaut : "word") | COMBO | Non | `"word"`<br>`"character"`<br>`"none"` |

**Remarque :** `num_speakers` ne peut pas être défini sur une valeur supérieure à 0 lorsque `diarize` est activé. Vous devez soit désactiver `diarize`, soit définir `num_speakers` sur 0.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `text` | Le texte transcrit à partir de l'audio. | STRING |
| `language_code` | Le code de langue détecté de l'audio. | STRING |
| `words_json` | Une chaîne au format JSON contenant des informations détaillées au niveau du mot, y compris les horodatages et les étiquettes de locuteur si activés. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsSpeechToText/fr.md)

---
**Source fingerprint (SHA-256):** `7eb5d72615aa8a9e4a8014e45b39cf83dc8d8432d7ce0dccba20489be80a5830`

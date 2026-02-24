> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsSpeechToText/fr.md)

Le nœud ElevenLabs Speech to Text (Reconnaissance vocale) retranscrit des fichiers audio en texte. Il utilise l'API d'ElevenLabs pour convertir la parole en une transcription écrite, prenant en charge des fonctionnalités comme la détection automatique de la langue, l'identification des différents locuteurs et l'étiquetage des sons non vocaux comme la musique ou les rires.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `audio` | AUDIO | Oui | - | Audio à transcrire. |
| `model` | COMBO | Oui | `"scribe_v2"` | Modèle à utiliser pour la transcription. La sélection de ce modèle révèle des paramètres supplémentaires. |
| `tag_audio_events` | BOOLEAN | Non | - | Annote les sons comme (rire), (musique), etc. dans la transcription. Ce paramètre est révélé lorsque le modèle `"scribe_v2"` est sélectionné. (par défaut : Faux) |
| `diarize` | BOOLEAN | Non | - | Annote quel locuteur parle. Ce paramètre est révélé lorsque le modèle `"scribe_v2"` est sélectionné. (par défaut : Faux) |
| `diarization_threshold` | FLOAT | Non | 0.1 - 0.4 | Sensibilité de la séparation des locuteurs. Des valeurs plus basses sont plus sensibles aux changements de locuteur. Ce paramètre est révélé lorsque le modèle `"scribe_v2"` est sélectionné et que `diarize` est activé. (par défaut : 0.22) |
| `temperature` | FLOAT | Non | 0.0 - 2.0 | Contrôle de l'aléatoire. 0.0 utilise la valeur par défaut du modèle. Des valeurs plus élevées augmentent l'aléatoire. Ce paramètre est révélé lorsque le modèle `"scribe_v2"` est sélectionné. (par défaut : 0.0) |
| `timestamps_granularity` | COMBO | Non | `"word"`<br>`"character"`<br>`"none"` | Précision du minutage pour les mots de la transcription. Ce paramètre est révélé lorsque le modèle `"scribe_v2"` est sélectionné. (par défaut : "word") |
| `language_code` | STRING | Non | - | Code de langue ISO-639-1 ou ISO-639-3 (par ex., 'en', 'es', 'fra'). Laisser vide pour une détection automatique. (par défaut : "") |
| `num_speakers` | INT | Non | 0 - 32 | Nombre maximum de locuteurs à prédire. Régler à 0 pour une détection automatique. (par défaut : 0) |
| `seed` | INT | Non | 0 - 2147483647 | Graine pour la reproductibilité (la déterminisme n'est pas garantie). (par défaut : 1) |

**Note :** Le paramètre `num_speakers` ne peut pas être défini sur une valeur supérieure à 0 lorsque l'option `diarize` est activée. Vous devez soit désactiver `diarize`, soit définir `num_speakers` sur 0.

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `text` | STRING | Le texte transcrit de l'audio. |
| `language_code` | STRING | Le code de langue détecté de l'audio. |
| `words_json` | STRING | Une chaîne de caractères au format JSON contenant des informations détaillées au niveau des mots, y compris les horodatages et les étiquettes de locuteur si activées. |

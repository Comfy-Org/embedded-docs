> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsSpeechToText/fr.md)

Voici la traduction de la documentation du nœud ElevenLabs Speech to Text :

Le nœud ElevenLabs Speech to Text transcrit des fichiers audio en texte. Il utilise l'API d'ElevenLabs pour convertir la parole en transcription écrite, prenant en charge des fonctionnalités telles que la détection automatique de la langue, l'identification des différents locuteurs et l'étiquetage des sons non vocaux comme la musique ou les rires.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `audio` | AUDIO | Oui | - | Audio à transcrire. |
| `model` | COMBO | Oui | `"scribe_v2"` | Modèle à utiliser pour la transcription. La sélection de ce modèle révèle des paramètres supplémentaires. |
| `tag_audio_events` | BOOLEAN | Non | - | Annoter les sons comme (rires), (musique), etc. dans la transcription. Ce paramètre est révélé lorsque le modèle `"scribe_v2"` est sélectionné. (par défaut : False) |
| `diarize` | BOOLEAN | Non | - | Annoter quel locuteur parle. Ce paramètre est révélé lorsque le modèle `"scribe_v2"` est sélectionné. (par défaut : False) |
| `diarization_threshold` | FLOAT | Non | 0.1 - 0.4 | Sensibilité de séparation des locuteurs. Des valeurs plus faibles sont plus sensibles aux changements de locuteur. Ce paramètre est révélé lorsque le modèle `"scribe_v2"` est sélectionné et que `diarize` est activé. (par défaut : 0.22) |
| `temperature` | FLOAT | Non | 0.0 - 2.0 | Contrôle de l'aléatoire. 0.0 utilise la valeur par défaut du modèle. Des valeurs plus élevées augmentent l'aléatoire. Ce paramètre est révélé lorsque le modèle `"scribe_v2"` est sélectionné. (par défaut : 0.0) |
| `timestamps_granularity` | COMBO | Non | `"word"`<br>`"character"`<br>`"none"` | Précision temporelle pour les mots de la transcription. Ce paramètre est révélé lorsque le modèle `"scribe_v2"` est sélectionné. (par défaut : "word") |
| `language_code` | STRING | Non | - | Code de langue ISO-639-1 ou ISO-639-3 (par exemple, 'en', 'es', 'fra'). Laissez vide pour la détection automatique. (par défaut : "") |
| `num_speakers` | INT | Non | 0 - 32 | Nombre maximum de locuteurs à prédire. Réglez sur 0 pour la détection automatique. (par défaut : 0) |
| `seed` | INT | Non | 0 - 2147483647 | Graine pour la reproductibilité (déterminisme non garanti). (par défaut : 1) |

**Remarque :** Le paramètre `num_speakers` ne peut pas être défini sur une valeur supérieure à 0 lorsque l'option `diarize` est activée. Vous devez soit désactiver `diarize`, soit définir `num_speakers` sur 0.

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `language_code` | STRING | Le texte transcrit à partir de l'audio. |
| `words_json` | STRING | Le code de langue détecté de l'audio. |
| `words_json` | STRING | Une chaîne formatée en JSON contenant des informations détaillées au niveau des mots, y compris les horodatages et les étiquettes de locuteur si activés. |

---
**Source fingerprint (SHA-256):** `aca2ac04d7280ef2b604f7c8d29ad7fea1e7abcfc38beabb64ba6b268a8cade1`

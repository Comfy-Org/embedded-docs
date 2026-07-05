# ElevenLabs Speech to Text

Voici la traduction de la documentation du nœud ElevenLabs Speech to Text :

Le nœud ElevenLabs Speech to Text transcrit des fichiers audio en texte. Il utilise l'API d'ElevenLabs pour convertir la parole en transcription écrite, prenant en charge des fonctionnalités telles que la détection automatique de la langue, l'identification des différents locuteurs et l'étiquetage des sons non vocaux comme la musique ou les rires.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `audio` | Audio à transcrire. | AUDIO | Oui | - |
| `model` | Modèle à utiliser pour la transcription. La sélection de ce modèle révèle des paramètres supplémentaires. | COMBO | Oui | `"scribe_v2"` |
| `tag_audio_events` | Annoter les sons comme (rires), (musique), etc. dans la transcription. Ce paramètre est révélé lorsque le modèle `"scribe_v2"` est sélectionné. (par défaut : False) | BOOLEAN | Non | - |
| `diarize` | Annoter quel locuteur parle. Ce paramètre est révélé lorsque le modèle `"scribe_v2"` est sélectionné. (par défaut : False) | BOOLEAN | Non | - |
| `diarization_threshold` | Sensibilité de séparation des locuteurs. Des valeurs plus faibles sont plus sensibles aux changements de locuteur. Ce paramètre est révélé lorsque le modèle `"scribe_v2"` est sélectionné et que `diarize` est activé. (par défaut : 0.22) | FLOAT | Non | 0.1 - 0.4 |
| `temperature` | Contrôle de l'aléatoire. 0.0 utilise la valeur par défaut du modèle. Des valeurs plus élevées augmentent l'aléatoire. Ce paramètre est révélé lorsque le modèle `"scribe_v2"` est sélectionné. (par défaut : 0.0) | FLOAT | Non | 0.0 - 2.0 |
| `timestamps_granularity` | Précision temporelle pour les mots de la transcription. Ce paramètre est révélé lorsque le modèle `"scribe_v2"` est sélectionné. (par défaut : "word") | COMBO | Non | `"word"`<br>`"character"`<br>`"none"` |
| `language_code` | Code de langue ISO-639-1 ou ISO-639-3 (par exemple, 'en', 'es', 'fra'). Laissez vide pour la détection automatique. (par défaut : "") | STRING | Non | - |
| `num_speakers` | Nombre maximum de locuteurs à prédire. Réglez sur 0 pour la détection automatique. (par défaut : 0) | INT | Non | 0 - 32 |
| `seed` | Graine pour la reproductibilité (déterminisme non garanti). (par défaut : 1) | INT | Non | 0 - 2147483647 |

**Remarque :** Le paramètre `num_speakers` ne peut pas être défini sur une valeur supérieure à 0 lorsque l'option `diarize` est activée. Vous devez soit désactiver `diarize`, soit définir `num_speakers` sur 0.


| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `text` | Le texte transcrit à partir de l'audio. | STRING |
| `language_code` | Le code de langue détecté de l'audio. | STRING |
| `words_json` | Une chaîne formatée en JSON contenant des informations détaillées au niveau des mots, y compris les horodatages et les étiquettes de locuteur si activés. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsSpeechToText/fr.md)

---
**Source fingerprint (SHA-256):** `aca2ac04d7280ef2b604f7c8d29ad7fea1e7abcfc38beabb64ba6b268a8cade1`

Voici la traduction en français de la documentation du nœud ElevenLabs Speech to Speech :

Le nœud ElevenLabs Speech to Speech transforme un fichier audio d'entrée d'une voix à une autre. Il utilise l'API ElevenLabs pour convertir la parole tout en préservant le contenu original et le ton émotionnel de l'audio.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `voix` | Voix cible pour la transformation. Connectez depuis le sélecteur de voix ou le clonage vocal instantané. | CUSTOM | Oui | - |
| `audio` | Audio source à transformer. | AUDIO | Oui | - |
| `stabilité` | Stabilité de la voix. Des valeurs plus faibles offrent une gamme émotionnelle plus large, des valeurs plus élevées produisent une parole plus cohérente mais potentiellement monotone (par défaut : 0.5). | FLOAT | Non | 0.0 - 1.0 |
| `modèle` | Modèle à utiliser pour la transformation parole-à-parole. Chaque option fournit un ensemble spécifique de paramètres vocaux (similarity_boost, style, use_speaker_boost, speed). | DYNAMICCOMBO | Non | `eleven_multilingual_sts_v2`<br>`eleven_english_sts_v2` |
| `format_de_sortie` | Format de sortie audio (par défaut : "mp3_44100_192"). | COMBO | Non | `"mp3_44100_192"`<br>`"opus_48000_192"` |
| `graine` | Graine pour la reproductibilité (par défaut : 0). | INT | Non | 0 - 4294967295 |
| `supprimer_bruit_de_fond` | Supprimer le bruit de fond de l'audio d'entrée en utilisant l'isolation audio (par défaut : False). | BOOLEAN | Non | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `audio` | Le fichier audio transformé dans le format de sortie spécifié. | AUDIO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsSpeechToSpeech/fr.md)

---
**Source fingerprint (SHA-256):** `118fe6e85b146d0649b104d814abb518d37f69ade2e53becac365a0ec90146fd`

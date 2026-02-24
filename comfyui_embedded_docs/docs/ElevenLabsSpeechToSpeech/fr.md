> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsSpeechToSpeech/fr.md)

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `voice` | CUSTOM | Oui | - | Voix cible pour la transformation. À connecter depuis Voice Selector ou Instant Voice Clone. |
| `audio` | AUDIO | Oui | - | Audio source à transformer. |
| `stability` | FLOAT | Non | 0.0 - 1.0 | Stabilité de la voix. Des valeurs plus basses donnent une plage émotionnelle plus large, des valeurs plus élevées produisent une parole plus cohérente mais potentiellement monotone (par défaut : 0.5). |
| `model` | DYNAMICCOMBO | Non | `eleven_multilingual_sts_v2`<br>`eleven_english_sts_v2` | Modèle à utiliser pour la transformation parole-à-parole. Chaque option fournit un ensemble spécifique de paramètres vocaux (similarity_boost, style, use_speaker_boost, speed). |
| `output_format` | COMBO | Non | `"mp3_44100_192"`<br>`"opus_48000_192"` | Format de sortie audio (par défaut : "mp3_44100_192"). |
| `seed` | INT | Non | 0 - 4294967295 | Graine pour la reproductibilité (par défaut : 0). |
| `remove_background_noise` | BOOLEAN | Non | - | Supprimer le bruit de fond de l'audio d'entrée en utilisant l'isolation audio (par défaut : False). |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `audio` | AUDIO | Le fichier audio transformé dans le format de sortie spécifié. |
# FishAudioSpeechToText

Ce nœud transcrit l'audio en texte à l'aide du service de reconnaissance vocale Fish Audio. Il détecte automatiquement la langue de l'audio et peut éventuellement renvoyer des segments horodatés au niveau du mot sous forme de JSON.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `audio` | Audio à transcrire. | AUDIO | Oui | — |
| `language` | Indication de langue ISO 639-1 (par ex. `en`, `zh`). La langue est automatiquement détectée dans tous les cas. Défaut : « "" » (chaîne vide). | STRING | Non | Tout code de langue ISO 639-1, par ex. `en`, `zh` ; chaîne vide pour la détection automatique |
| `precise_timestamps` | Renvoie des segments horodatés au niveau du mot. Défaut : false. | BOOLEAN | Non | true ou false |

Remarque : le paramètre `language` n'est qu'une indication — la langue est toujours automatiquement détectée à partir de l'audio. Lorsque `precise_timestamps` est false (défaut), les horodatages au niveau du mot ne sont pas renvoyés ; lorsqu'il est true, les segments de sortie incluent les horodatages au niveau du mot.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `text` | Le texte transcrit. | STRING |
| `language_code` | Le code de langue ISO 639-1 détecté pour l'audio. | STRING |
| `segments_json` | Chaîne JSON contenant les segments de transcription. Inclut les horodatages au niveau du mot lorsque `precise_timestamps` est activé. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FishAudioSpeechToText/fr.md)

---
**Source fingerprint (SHA-256):** `eaf1c9a9d2b90ec962a408615cc417b552864354c3f272144b8e239b23961920`

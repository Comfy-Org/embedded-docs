# Enregistrer l’Audio (Avancé)

Sauvegarde l'audio d'entrée dans votre répertoire de sortie ComfyUI. Ce nœud vous permet d'exporter l'audio dans différents formats, notamment FLAC, MP3 et Opus, avec des paramètres de qualité configurables.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `audio` | L'audio à sauvegarder. | AUDIO | Oui | - |
| `préfixe_nom_fichier` | Le préfixe du fichier à sauvegarder. Peut inclure des jetons de formatage tels que %date:yyyy-MM-dd%. (par défaut : "audio/ComfyUI") | STRING | Oui | - |
| `format` | Le format de fichier dans lequel sauvegarder l'audio. | COMBO | Oui | "flac"<br>"mp3"<br>"opus" |

Lorsque "mp3" est sélectionné comme format, un sous-paramètre `quality` devient disponible avec les options suivantes : "V0", "128k", "320k" (par défaut : "V0").

Lorsque "opus" est sélectionné comme format, un sous-paramètre `quality` devient disponible avec les options suivantes : "64k", "96k", "128k", "192k", "320k" (par défaut : "128k").

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `ui` | Sortie d'interface contenant les informations du fichier audio sauvegardé. | UI |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudioAdvanced/fr.md)

---
**Source fingerprint (SHA-256):** `98314263dd84c562e7c02ba89f3d10551fcb898ac784af2aa397ca8357e4aae8`

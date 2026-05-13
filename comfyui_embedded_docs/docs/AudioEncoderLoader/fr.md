> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioEncoderLoader/fr.md)

Le nœud AudioEncoderLoader charge un modèle d'encodeur audio à partir d'un fichier situé dans votre dossier d'encodeurs audio. Il prend en entrée le nom du fichier du modèle d'encodeur audio et retourne le modèle chargé, qui peut ensuite être utilisé pour des tâches de traitement audio dans votre workflow.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `audio_encoder_name` | STRING | Oui | Liste des fichiers d'encodeur audio disponibles dans le dossier audio_encoders | Sélectionne le fichier de modèle d'encodeur audio à charger |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `audio_encoder` | AUDIO_ENCODER | Le modèle d'encodeur audio chargé, prêt à être utilisé dans les workflows de traitement audio |

---
**Source fingerprint (SHA-256):** `24cbd45198db7d950633358c29de57f56c999bc33534fabe80404528d194163c`

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewAudio/fr.md)

Le nœud PreviewAudio crée un aperçu audio temporaire pouvant être lu directement dans l'interface. Il prend des données audio en entrée et génère un widget de prévisualisation, permettant aux utilisateurs d'écouter les sorties audio sans enregistrer de fichiers permanents.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `audio` | AUDIO | Oui | - | Les données audio à prévisualiser |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `ui` | UI | Affiche un widget de lecteur audio dans l'interface pour prévisualiser l'audio |

---
**Source fingerprint (SHA-256):** `3f4b38e9768abde9d7f406c5442660679b80532799dfff8af20b2ea178268582`

# Enregistrer Audio (Opus)

Le nœud SaveAudioOpus enregistre les données audio dans un fichier au format Opus, ce qui vous permet de choisir la qualité d'encodage (débit binaire) et le préfixe du nom de fichier pour le fichier exporté. Ce nœud est obsolète et pourra être supprimé dans les versions futures.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `audio` | Les données audio à enregistrer dans un fichier Opus. Une ValueError est levée si cette valeur est None (par exemple, lorsque la vidéo source ne contient aucune piste audio). | AUDIO | Oui | - |
| `préfixe_nom_fichier` | Préfixe utilisé pour le nom du fichier de sortie (par défaut : "audio/ComfyUI"). | STRING | Non | - |
| `qualité` | Débit binaire utilisé pour encoder le fichier Opus ; des valeurs plus élevées produisent une meilleure qualité mais des fichiers plus volumineux (par défaut : "128k"). | COMBO | Non | `"64k"`<br>`"96k"`<br>`"128k"`<br>`"192k"`<br>`"320k"` |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `audio` | Les données audio qui ont été enregistrées dans le fichier Opus. | AUDIO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudioOpus/fr.md)

---
**Source fingerprint (SHA-256):** `a2f585f45299759738fa85f6b73f51680d4e86da57d3fc9c2236e66114fa3d6c`

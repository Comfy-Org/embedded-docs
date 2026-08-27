# Enregistrer Audio (Opus)

Le nœud SaveAudioOpus enregistre des données audio dans un fichier au format Opus. Il prend une entrée audio et l’exporte sous forme de fichier Opus compressé avec des paramètres de qualité configurables. Ce nœud est obsolète et pourrait être supprimé dans les versions futures.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `audio` | Les données audio à enregistrer en tant que fichier Opus. Une ValueError est levée si ce paramètre est None (par exemple, lorsque la vidéo source ne comporte aucune piste audio). | AUDIO | Oui | - |
| `préfixe_nom_fichier` | Le préfixe du nom de fichier de sortie (défaut : « audio/ComfyUI ») | STRING | Non | - |
| `qualité` | Le débit binaire utilisé pour encoder le fichier Opus ; des valeurs plus élevées produisent une meilleure qualité mais des fichiers plus volumineux (défaut : « 128k ») | COMBO | Non | "64k"<br>"96k"<br>"128k"<br>"192k"<br>"320k" |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `audio` | Les données audio qui ont été enregistrées dans le fichier Opus | AUDIO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudioOpus/fr.md)

---
**Source fingerprint (SHA-256):** `a2f585f45299759738fa85f6b73f51680d4e86da57d3fc9c2236e66114fa3d6c`

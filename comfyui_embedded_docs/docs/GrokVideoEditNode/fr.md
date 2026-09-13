# Grok Video Edit

Ce nœud utilise l'API Grok pour modifier une vidéo existante à partir d'une invite textuelle. Il téléverse votre vidéo, envoie une requête au modèle d'IA pour la modifier selon votre description, et renvoie la vidéo nouvellement générée.

## Entrées

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `modèle` | Modèle d'IA à utiliser pour l'édition vidéo (par défaut : "grok-imagine-video"). | COMBO | Oui | "grok-imagine-video" |
| `invite` | Description textuelle de la vidéo souhaitée. | STRING | Oui | N/A |
| `vidéo` | Vidéo d'entrée à modifier. Durée maximale prise en charge : 8,7 secondes et taille de fichier maximale : 50 Mo. | VIDEO | Oui | N/A |
| `graine` | Graine permettant de déterminer si le nœud doit être réexécuté ; les résultats réels sont non déterministes quel que soit la graine (par défaut : 0). | INT | Non | 0 à 2147483647 |

**Contraintes :**

* Le `prompt` ne doit pas être vide.
* La `video` d'entrée doit avoir une durée comprise entre 1 et 8,7 secondes.
* La taille du fichier `video` d'entrée ne doit pas dépasser 50 Mo.

**Remarque :** Ce nœud est un nœud API et nécessite un compte Comfy.org ainsi qu'une clé API pour fonctionner. L'utilisation est facturée environ 0,06 $ par seconde de vidéo.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `video` | Vidéo modifiée générée par le modèle d'IA. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoEditNode/fr.md)

---
**Source fingerprint (SHA-256):** `7ceedff2f858bc0849b5e0d92d10ed51e7fdccd1391c6a6966561cb05999b4b1`

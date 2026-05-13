> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveVideo/fr.md)

Le nœud SaveVideo enregistre le contenu vidéo d’entrée dans votre répertoire de sortie ComfyUI. Il vous permet de spécifier le préfixe du nom de fichier, le format vidéo et le codec pour le fichier sauvegardé. Le nœud gère automatiquement la numérotation des noms de fichiers avec incrémentation et peut inclure les métadonnées du workflow dans la vidéo enregistrée.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `vidéo` | VIDEO | Oui | - | La vidéo à sauvegarder. |
| `préfixe_nom_fichier` | STRING | Non | - | Le préfixe pour le fichier à sauvegarder. Peut inclure des informations de formatage telles que `%date:yyyy-MM-dd%` ou `%Empty Latent Image.width%` pour inclure des valeurs provenant de nœuds (par défaut : "video/ComfyUI"). |
| `format` | COMBO | Non | `"auto"`<br>`"mp4"`<br>`"webm"`<br>`"mkv"`<br>`"gif"` | Le format de sauvegarde de la vidéo (par défaut : "auto"). |
| `codec` | COMBO | Non | `"auto"`<br>`"h264"`<br>`"h265"`<br>`"vp9"`<br>`"av1"`<br>`"prores"` | Le codec à utiliser pour la vidéo (par défaut : "auto"). |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| *Aucune sortie* | - | Ce nœud ne renvoie aucune donnée de sortie. |

---
**Source fingerprint (SHA-256):** `506ddc8820924688cccb9fd838ff9c0f5217a38f708f28f15a060be9325cea61`

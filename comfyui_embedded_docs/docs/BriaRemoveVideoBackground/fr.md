> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaRemoveVideoBackground/fr.md)

Ce nœud supprime l'arrière-plan d'une vidéo en utilisant le service Bria AI. Il traite la vidéo d'entrée et remplace l'arrière-plan original par une couleur unie de votre choix. L'opération est effectuée via une API externe, et le résultat est renvoyé sous la forme d'un nouveau fichier vidéo.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `video` | VIDEO | Oui | N/A | Le fichier vidéo d'entrée dont l'arrière-plan sera supprimé. |
| `background_color` | STRING | Oui | `"Black"`<br>`"White"`<br>`"Gray"`<br>`"Red"`<br>`"Green"`<br>`"Blue"`<br>`"Yellow"`<br>`"Cyan"`<br>`"Magenta"`<br>`"Orange"` | La couleur unie à utiliser comme nouvel arrière-plan pour la vidéo de sortie. |
| `seed` | INT | Non | 0 à 2147483647 | Une valeur de seed qui contrôle si le nœud doit être réexécuté. Les résultats sont non déterministes, quelle que soit la valeur du seed. (par défaut : 0) |

**Note :** La vidéo d'entrée doit avoir une durée de 60 secondes ou moins.

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | VIDEO | Le fichier vidéo traité avec l'arrière-plan supprimé et remplacé par la couleur sélectionnée. |
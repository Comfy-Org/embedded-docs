Voici la traduction en français de la documentation du nœud ComfyUI, en respectant vos règles :

Ce nœud supprime l'arrière-plan d'une vidéo à l'aide du service IA Bria. Il traite la vidéo d'entrée et remplace l'arrière-plan d'origine par une couleur unie de votre choix. L'opération est effectuée via une API externe, et le résultat est renvoyé sous forme d'un nouveau fichier vidéo.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `vidéo` | Le fichier vidéo d'entrée dont l'arrière-plan sera supprimé. | VIDEO | Oui | N/D |
| `couleur d’arrière-plan` | La couleur unie à utiliser comme nouvel arrière-plan pour la vidéo de sortie. | STRING | Oui | `"Black"`<br>`"White"`<br>`"Gray"`<br>`"Red"`<br>`"Green"`<br>`"Blue"`<br>`"Yellow"`<br>`"Cyan"`<br>`"Magenta"`<br>`"Orange"` |
| `graine` | Une valeur de graine qui contrôle si le nœud doit être réexécuté. Les résultats sont non déterministes, quelle que soit la valeur de la graine. (par défaut : 0) | INT | Non | 0 à 2147483647 |

**Remarque :** La vidéo d'entrée doit avoir une durée de 60 secondes ou moins.

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `output` | Le fichier vidéo traité avec l'arrière-plan supprimé et remplacé par la couleur sélectionnée. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaRemoveVideoBackground/fr.md)

---
**Source fingerprint (SHA-256):** `51499fc006d3fd3fd45f8aad686d92537d399255b3a583fd54b77c5a0698a068`

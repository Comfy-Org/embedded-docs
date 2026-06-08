Voici la traduction en français de la documentation du nœud ImageRotate :

Le nœud ImageRotate fait pivoter une image d'entrée selon des angles spécifiés. Il prend en charge quatre options de rotation : aucune rotation, 90 degrés dans le sens horaire, 180 degrés et 270 degrés dans le sens horaire. La rotation est effectuée à l'aide d'opérations tensorielles efficaces qui préservent l'intégrité des données de l'image.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `image` | L'image d'entrée à faire pivoter | IMAGE | Oui | - |
| `rotation` | L'angle de rotation à appliquer à l'image (par défaut : "none") | STRING | Oui | "none"<br>"90 degrees"<br>"180 degrees"<br>"270 degrees" |

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `image` | L'image pivotée en sortie | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageRotate/fr.md)

---
**Source fingerprint (SHA-256):** `068946b31ebe87b2524a1e628b5bc0a3da7367d7252fa7afafe96bcbb174747d`

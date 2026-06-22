# Topaz Amélioration d'image

Le nœud Topaz Image Enhance offre une mise à l'échelle et une amélioration d'image de qualité professionnelle. Il traite une seule image d'entrée à l'aide d'un modèle d'IA basé sur le cloud pour améliorer la qualité, les détails et la résolution. Le nœud permet un contrôle précis du processus d'amélioration, notamment des options pour l'orientation créative, la concentration sur le sujet et la préservation des visages.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle d'IA à utiliser pour l'amélioration d'image. | COMBO | Oui | `"Reimagine"` |
| `image` | L'image d'entrée à améliorer. Une seule image est prise en charge. | IMAGE | Oui | - |
| `invite` | Une invite textuelle facultative pour guider la mise à l'échelle créative (par défaut : vide). | STRING | Non | - |
| `détection du sujet` | Contrôle la partie de l'image sur laquelle l'amélioration se concentre (par défaut : "All"). | COMBO | Non | `"All"`<br>`"Foreground"`<br>`"Background"` |
| `amélioration du visage` | Activer pour améliorer les visages s'ils sont présents dans l'image (par défaut : True). | BOOLEAN | Non | - |
| `créativité de l'amélioration du visage` | Définit le niveau de créativité pour l'amélioration des visages (par défaut : 0,0). | FLOAT | Non | 0,0 - 1,0 |
| `intensité de l'amélioration du visage` | Contrôle le degré de netteté des visages améliorés par rapport à l'arrière-plan (par défaut : 1,0). | FLOAT | Non | 0,0 - 1,0 |
| `rogner pour remplir` | Par défaut, l'image est mise en boîte aux lettres lorsque le rapport hauteur/largeur de sortie diffère. Activez cette option pour recadrer l'image afin de remplir les dimensions de sortie (par défaut : False). | BOOLEAN | Non | - |
| `largeur de sortie` | La largeur souhaitée de l'image de sortie. Une valeur de 0 signifie qu'elle sera calculée automatiquement, généralement en fonction de la taille d'origine ou de la `hauteur de sortie` si spécifiée (par défaut : 0). | INT | Non | 0 - 32000 |
| `hauteur de sortie` | La hauteur souhaitée de l'image de sortie. Une valeur de 0 signifie qu'elle sera calculée automatiquement, généralement en fonction de la taille d'origine ou de la `largeur de sortie` si spécifiée (par défaut : 0). | INT | Non | 0 - 32000 |
| `créativité` | Contrôle le niveau de créativité global de l'amélioration (par défaut : 3). | INT | Non | 1 - 9 |
| `préservation du visage` | Préserver l'identité faciale des sujets dans l'image (par défaut : True). | BOOLEAN | Non | - |
| `préservation des couleurs` | Préserver les couleurs d'origine de l'image d'entrée (par défaut : True). | BOOLEAN | Non | - |

**Remarque :** Ce nœud ne peut traiter qu'une seule image d'entrée. La fourniture d'un lot de plusieurs images entraînera une erreur.

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `image` | L'image de sortie améliorée. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazImageEnhance/fr.md)

---
**Source fingerprint (SHA-256):** `69f2c929f2cd11f13557e064e30a4514e3862e127a2bdb3a3f40ec92023f255d`

# Topaz Amélioration d'image

Le nœud Topaz Image Enhance fournit une mise à l'échelle et une amélioration d'image conformes aux standards du secteur. Il traite une seule image d'entrée à l'aide d'un modèle d'IA basé sur le cloud pour améliorer la qualité, les détails et la résolution. Le nœud offre un contrôle précis du processus d'amélioration, notamment des options pour le guidage créatif, la mise au point sur le sujet et la préservation des visages.

Ce nœud est une version héritée et est marqué comme obsolète dans l'interface.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `modèle` | Le modèle d'IA à utiliser pour l'amélioration de l'image. | COMBO | Oui | `"Reimagine"` |
| `image` | L'image d'entrée à améliorer. Une seule image est prise en charge. | IMAGE | Oui | - |
| `invite` | Invite textuelle facultative pour guider la mise à l'échelle créative (par défaut : vide). | STRING | Non | - |
| `détection du sujet` | Contrôle la partie de l'image sur laquelle l'amélioration se concentre (par défaut : "All"). | COMBO | Non | `"All"`<br>`"Foreground"`<br>`"Background"` |
| `amélioration du visage` | Améliore les visages (s'ils sont présents) pendant le traitement (par défaut : True). | BOOLEAN | Non | - |
| `créativité de l'amélioration du visage` | Définit le niveau de créativité pour l'amélioration des visages (par défaut : 0.0). | FLOAT | Non | 0.0 - 1.0 |
| `intensité de l'amélioration du visage` | Contrôle la netteté des visages améliorés par rapport à l'arrière-plan (par défaut : 1.0). | FLOAT | Non | 0.0 - 1.0 |
| `rogner pour remplir` | Par défaut, l'image est letterboxée lorsque le rapport d'aspect de sortie diffère. Activez cette option pour recadrer l'image afin de remplir les dimensions de sortie (par défaut : False). | BOOLEAN | Non | - |
| `largeur de sortie` | Une valeur nulle signifie que la valeur est calculée automatiquement (il s'agira généralement de la taille d'origine ou de output_height si spécifié) (par défaut : 0). | INT | Non | 0 - 32000 |
| `hauteur de sortie` | Une valeur nulle signifie que la sortie aura la même hauteur que l'original ou que la largeur de sortie (par défaut : 0). | INT | Non | 0 - 32000 |
| `créativité` | Contrôle le niveau global de créativité de l'amélioration (par défaut : 3). | INT | Non | 1 - 9 |
| `préservation du visage` | Préserve l'identité faciale des sujets (par défaut : True). | BOOLEAN | Non | - |
| `préservation des couleurs` | Préserve les couleurs d'origine (par défaut : True). | BOOLEAN | Non | - |

**Remarque :** Ce nœud ne peut traiter qu'une seule image d'entrée. Fournir un lot de plusieurs images entraînera une erreur.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `image` | L'image de sortie améliorée. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazImageEnhance/fr.md)

---
**Source fingerprint (SHA-256):** `1a0e708cdea9ec4f92f7f3aaabbdeea06a8fdab2f91a45ad2dea15f2bc2e8fa3`

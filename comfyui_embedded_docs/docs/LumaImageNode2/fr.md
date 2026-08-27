# Luma UNI-1 Image

## Aperçu

Ce nœud génère des images à partir de descriptions textuelles à l'aide du modèle Luma UNI-1. Il prend une invite textuelle et des paramètres facultatifs comme le rapport hauteur/largeur et le style, puis envoie la requête à l'API Luma pour créer une image. Deux variantes de modèle sont disponibles : `uni-1` et `uni-1-max`.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Modèle à utiliser pour la génération. La sélection d'un modèle révèle des paramètres supplémentaires pour ce modèle. | DYNAMIC_COMBO | Oui | `"uni-1"`<br>`"uni-1-max"` |
| `invite` | Description textuelle de l'image souhaitée. De 1 à 6000 caractères. | STRING | Oui | 1 à 6000 caractères |
| `graine` | La graine (seed) contrôle si le nœud doit s'exécuter de nouveau ; les résultats ne sont pas déterministes quelle que soit la graine. (par défaut : 0) | INT | Oui | 0 à 2147483647 |

### Entrées uni-1 et uni-1-max

Partagées par les options de modèle `uni-1` et `uni-1-max`. Ces paramètres apparaissent lorsque l'un ou l'autre modèle est sélectionné.

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `aspect_ratio` | Rapport hauteur/largeur de l'image de sortie. `"auto"` laisse le modèle choisir en fonction de l'invite. (par défaut : `"auto"`) | COMBO | Oui | `"auto"`<br>`"3:1"`<br>`"2:1"`<br>`"16:9"`<br>`"3:2"`<br>`"1:1"`<br>`"2:3"`<br>`"9:16"`<br>`"1:2"`<br>`"1:3"` |
| `style` | Préréglage de style. `"auto"` choisit en fonction de l'invite ; `"manga"` applique une esthétique manga/anime et nécessite un rapport hauteur/largeur portrait (2:3, 9:16, 1:2, 1:3). (par défaut : `"auto"`) | COMBO | Oui | `"auto"`<br>`"manga"` |
| `web_search` | Rechercher sur le Web des références visuelles avant la génération. (par défaut : False) | BOOLEAN | Oui | True / False |

### Entrées de référence

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `image_ref` | Emplacement extensible : connectez 1 à 9 éléments (par ex. `image_1` à `image_9`). Jusqu'à 9 images de référence pour guider le style/contenu. | IMAGE | Non | Jusqu'à 9 images |

**Remarque :** Si `style` est défini sur `"manga"`, le `aspect_ratio` doit être soit `"auto"`, soit l'un des ratios portrait `"2:3"`, `"9:16"`, `"1:2"`, `"1:3"`. L'utilisation de tout autre ratio avec le style `"manga"` entraînera une erreur. Le nombre maximal d'images de référence est de 9 pour `uni-1` et `uni-1-max`.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `image` | L'image générée sous forme de tenseur. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageNode2/fr.md)

---
**Source fingerprint (SHA-256):** `27254fe4627fd340426a68f651cab4513ffb6668cafc0accd17f2c442f7d3125`

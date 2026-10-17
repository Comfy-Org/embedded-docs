# Krea 3 Image

Krea 3 Image modifie des images avec Krea 3, ou génère une nouvelle image à partir d'un prompt textuel lorsqu'aucune image n'est connectée. Connectez jusqu'à 8 images et décrivez ce qu'il faut modifier et ce qu'il faut conserver, en y faisant référence dans le prompt sous la forme @Image1, @Image2, etc. Le ratio d'aspect et la résolution définissent la taille de sortie, et le mode de réflexion sacrifie de la vitesse pour un plan plus détaillé.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Le modèle Krea 3 à utiliser. La sélection d'un modèle révèle les paramètres qu'il accepte. | DYNAMIC_COMBO | Oui | `"Krea 3"` |

### Entrées Krea 3

Ces entrées apparaissent lorsque `model` est défini sur `Krea 3`.

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model.images` | Les images à modifier, numérotées dans l'ordre de connexion. Chaque image connectée compte dans la limite de 8. Laissez vide pour générer uniquement à partir du texte. | IMAGE | Non | 0 à 8 images |
| `model.prompt` | Ce qu'il faut modifier et ce qu'il faut conserver. Faites référence aux images sous la forme `@Image1`, `@Image2`, etc., ou comme image 1, image 2, ... Le prompt ne peut pas être vide. | STRING | Oui | - |
| `model.aspect_ratio` | Le ratio d'aspect du résultat. `"auto"` suit la première image, ou le prompt lorsqu'aucune image n'est connectée. (valeur par défaut : `"auto"`) | COMBO | Oui | `"auto"`<br>`"1:1"`<br>`"4:5"`<br>`"3:4"`<br>`"2:3"`<br>`"9:16"`<br>`"5:4"`<br>`"4:3"`<br>`"3:2"`<br>`"16:9"`<br>`"21:9"` |
| `model.resolution` | La résolution de sortie. `"2K"` prend plus de temps et produit une image plus grande que `"1K"`. (valeur par défaut : `"2K"`) | COMBO | Oui | `"1K"`<br>`"2K"` |
| `model.thinking_mode` | La quantité de travail que Krea 3 consacre à la planification de la modification. `"fast"` est recommandé, tandis que `"high"` planifie les modifications complexes de manière plus détaillée et prend plus de temps. (valeur par défaut : `"fast"`) | COMBO | Oui | `"fast"`<br>`"high"` |
| `model.precise_edit` | Maintenir inchangé tout ce qui se trouve en dehors de la zone modifiée. Nécessite au moins une image connectée. (valeur par défaut : False) | BOOLEAN | Oui | false<br>true |
| `model.seed` | La graine pour la requête (valeur par défaut : 42). Krea réécrit le prompt avant de générer, donc la même graine ne reproduit pas une image identique. | INT | Oui | 0 à 2147483647 |

Une référence telle que `@Image3` n'est acceptée que lorsqu'au moins trois images sont connectées, sinon le nœud déclenche une erreur. Les images de référence sont téléversées avant l'envoi de la requête.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `image` | L'image générée ou modifiée. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Krea3ImageNode/fr.md)

---
**Source fingerprint (SHA-256):** `3d14262a3b5f2593fb75abc50e1278db00b81fd0e79ab829fea241dbd07e22dc`

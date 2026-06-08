Voici la traduction en français de la documentation du nœud ComfyUI, en respectant toutes vos règles :

## Aperçu

Ce nœud génère des images à partir de descriptions textuelles en utilisant le modèle Luma UNI-1. Il prend une invite textuelle et des paramètres optionnels comme le rapport hauteur/largeur et le style, puis envoie la requête à l'API Luma pour créer une image.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `invite` | Description textuelle de l'image souhaitée. | STRING | Oui | 1 à 6000 caractères |
| `modèle` | Modèle à utiliser pour la génération. La sélection d'un modèle révèle des paramètres supplémentaires pour ce modèle. | COMBO | Oui | `"uni-1"`<br>`"uni-1-max"` |
| `graine` | La graine contrôle si le nœud doit se ré-exécuter ; les résultats sont non déterministes quelle que soit la graine. (par défaut : 0) | INT | Oui | 0 à 2147483647 |

### Entrées spécifiques au modèle

Lorsque `"uni-1"` ou `"uni-1-max"` est sélectionné pour le paramètre `model`, les entrées suivantes deviennent disponibles :

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `aspect_ratio` | Rapport hauteur/largeur de l'image de sortie. `"auto"` laisse le modèle choisir en fonction de l'invite. (par défaut : `"auto"`) | COMBO | Oui | `"auto"`<br>`"3:1"`<br>`"2:1"`<br>`"16:9"`<br>`"3:2"`<br>`"1:1"`<br>`"2:3"`<br>`"9:16"`<br>`"1:2"`<br>`"1:3"` |
| `style` | Le style visuel de l'image générée. (par défaut : `"auto"`) | COMBO | Oui | `"auto"`<br>`"manga"` |
| `web_search` | Permet ou non au modèle de rechercher sur le web pour obtenir un contexte supplémentaire. (par défaut : Faux) | BOOLEAN | Oui | Vrai / Faux |
| `image_ref` | Images de référence pour guider la génération. | IMAGE | Non | Jusqu'à 9 images |

**Remarque sur les contraintes de `style` et `aspect_ratio` :** Si `style` est défini sur `"manga"`, le `aspect_ratio` doit être soit `"auto"`, soit l'un des rapports portrait suivants : `"2:3"`, `"9:16"`, `"1:2"`, `"1:3"`. L'utilisation d'un rapport paysage ou carré avec le style `"manga"` entraînera une erreur.

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `image` | L'image générée sous forme de tenseur. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageNode2/fr.md)

---
**Source fingerprint (SHA-256):** `0a71bcd7c68c3610c162601b4c3f700034e47af8f16cf7853606753ad270c96e`

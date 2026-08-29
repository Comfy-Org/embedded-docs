# Recraft V4 Texte vers Vectoriel

Le nœud Recraft V4 Text to Vector génère des illustrations vectorielles (SVG) à partir d'une description textuelle en utilisant les modèles Recraft V4 et V4.1. Il se connecte à l'API Recraft pour générer un ou plusieurs fichiers SVG en fonction de votre prompt, et peut appliquer un style vectoriel existant ou en créer un nouveau à partir d'images de référence — lorsque des images de référence sont utilisées, le style créé est renvoyé sous la forme d'un `style_id` réutilisable.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `modèle` | Le modèle à utiliser pour la génération. Les modèles recraftv4_styles sont conçus pour une génération cohérente en termes de style et nécessitent toujours un style_id ou des style_references. La sélection d'un modèle modifie les options `size` disponibles. | DYNAMIC_COMBO | Oui | `"recraftv4_1_vector"`<br>`"recraftv4_1_utility_vector"`<br>`"recraftv4_1_pro_vector"`<br>`"recraftv4_1_utility_pro_vector"`<br>`"recraftv4"`<br>`"recraftv4_pro"`<br>`"recraftv4_styles_vector"`<br>`"recraftv4_styles_pro_vector"` |
| `prompt` | Prompt pour la génération d'images. 10 000 caractères maximum. | STRING | Oui | N/A |
| `prompt_négatif` | Cette entrée est ignorée : le prompt négatif n'est pas pris en charge par les modèles Recraft V4 et V4.1. | STRING | Oui | N/A |
| `n` | Le nombre d'images à générer (par défaut : 1). | INT | Oui | 1 à 6 |
| `graine` | Seed permettant de déterminer si le nœud doit se réexécuter ; les résultats réels sont non déterministes quelle que soit la seed (par défaut : 0). | INT | Oui | 0 à 18446744073709551615 |
| `recraft_controls` | Contrôles supplémentaires facultatifs sur la génération via le nœud Recraft Controls. | CUSTOM | Non | N/A |
| `style_id` | UUID d'un style vectoriel Recraft V4 à appliquer, par exemple depuis le nœud Recraft V4 Create Style ou la sortie style_id d'une exécution précédente. Ne peut pas être combiné avec style_references. | STRING | Non | N/A |
| `style_match` | Degré de fidélité au style : precise le reproduit en détail, flexible correspond à l'apparence générale. Uniquement utilisé lorsqu'un style est fourni (par défaut : « precise »). | COMBO | Non | `"precise"`<br>`"flexible"` |

### Entrées recraftv4_1_vector, recraftv4_1_utility_vector, recraftv4 et recraftv4_styles_vector

Ces modèles partagent les mêmes options `size`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `size` | La taille de l'image générée. Par défaut : `"1024x1024"`. | COMBO | Oui | `"1024x1024"`<br>`"1152x896"`<br>`"896x1152"`<br>`"1216x832"`<br>`"832x1216"`<br>`"1344x768"`<br>`"768x1344"`<br>`"1536x640"`<br>`"640x1536"` |

### Entrées recraftv4_1_pro_vector, recraftv4_1_utility_pro_vector, recraftv4_pro et recraftv4_styles_pro_vector

Ces modèles partagent les mêmes options `size`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `size` | La taille de l'image générée. Par défaut : `"2048x2048"`. | COMBO | Oui | `"2048x2048"`<br>`"2304x1792"`<br>`"1792x2304"`<br>`"2432x1664"`<br>`"1664x2432"`<br>`"2688x1536"`<br>`"1536x2688"`<br>`"3072x1280"`<br>`"1280x3072"` |

### Entrées de référence

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `style_references` | Images de référence pour créer un style vectoriel à la volée, facturées en plus de la génération. Le style créé est renvoyé comme style_id pour être réutilisé. Ne peut pas être combiné avec style_id. | IMAGE | Non | Emplacement extensible : connectez de 1 à N images de référence (jusqu'au maximum du nœud) |

**Remarque :** Le paramètre `size` est une entrée dynamique dont les options disponibles changent en fonction du `model` sélectionné. La valeur `seed` ne garantit pas des résultats reproductibles depuis l'API externe. Les modèles `recraftv4_styles_vector` et `recraftv4_styles_pro_vector` nécessitent toujours un style : fournissez un `style_id` ou connectez au moins une image `style_references`. `style_id` et `style_references` ne peuvent pas être utilisés ensemble — fournir les deux provoque une erreur, et `style_id` doit être un UUID valide. Les images de référence sont limitées en nombre et leur taille totale encodée ne doit pas dépasser 10 Mo.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `output` | La ou les images vectorielles (SVG) générées. | SVG |
| `style_id` | L'UUID du style renvoyé par l'API Recraft. Lorsque des images de référence sont fournies, le style créé est renvoyé ici pour être réutilisé ; sinon, chaîne vide. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4TextToVectorNode/fr.md)

---
**Source fingerprint (SHA-256):** `182a40b206b164cf2e96c7344d23e4906b7d61b90e3000743a3fd31941e08539`

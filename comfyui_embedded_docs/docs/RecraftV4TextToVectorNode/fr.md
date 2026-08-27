# Recraft V4 Texte vers Vectoriel

Le nœud Recraft V4 Text to Vector génère des illustrations SVG (Scalable Vector Graphics) à partir d’une description textuelle. Il se connecte à l’API Recraft pour générer des images à l’aide des modèles Recraft V4 et V4.1, et produit un ou plusieurs fichiers SVG en fonction de votre prompt.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `modèle` | Le modèle à utiliser pour la génération. La sélection d’un modèle modifie les options `size` disponibles. | DYNAMIC_COMBO | Oui | `"recraftv4_1_vector"`<br>`"recraftv4_1_utility_vector"`<br>`"recraftv4_1_pro_vector"`<br>`"recraftv4_1_utility_pro_vector"`<br>`"recraftv4"`<br>`"recraftv4_pro"` |
| `prompt` | Prompt pour la génération d’images. 10 000 caractères maximum. | STRING | Oui | N/A |
| `prompt_négatif` | Cette entrée est ignorée : le prompt négatif n’est pas pris en charge par les modèles Recraft V4 et V4.1. | STRING | Oui | N/A |
| `n` | Le nombre d’images à générer (par défaut : 1). | INT | Oui | 1 à 6 |
| `graine` | Seed pour déterminer si le nœud doit s’exécuter à nouveau ; les résultats réels sont non déterministes indépendamment de la seed (par défaut : 0). | INT | Oui | 0 à 18446744073709551615 |
| `recraft_controls` | Contrôles supplémentaires optionnels sur la génération via le nœud Recraft Controls. | CUSTOM | Non | N/A |

### Entrées recraftv4_1_vector, recraftv4_1_utility_vector et recraftv4

Ces modèles partagent les mêmes options `size`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `size` | La taille de l’image générée. Par défaut : `"1024x1024"`. | COMBO | Oui | `"1024x1024"`<br>`"1152x896"`<br>`"896x1152"`<br>`"1216x832"`<br>`"832x1216"`<br>`"1344x768"`<br>`"768x1344"`<br>`"1536x640"`<br>`"640x1536"` |

### Entrées recraftv4_1_pro_vector, recraftv4_1_utility_pro_vector et recraftv4_pro

Ces modèles partagent les mêmes options `size`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `size` | La taille de l’image générée. Par défaut : `"2048x2048"`. | COMBO | Oui | `"2048x2048"`<br>`"2304x1792"`<br>`"1792x2304"`<br>`"2432x1664"`<br>`"1664x2432"`<br>`"2688x1536"`<br>`"1536x2688"`<br>`"3072x1280"`<br>`"1280x3072"` |

**Remarque :** Le paramètre `size` est une entrée dynamique dont les options disponibles changent en fonction du `model` sélectionné. La valeur `seed` ne garantit pas des résultats reproductibles depuis l’API externe.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `output` | Les images SVG (Scalable Vector Graphics) générées. | SVG |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4TextToVectorNode/fr.md)

---
**Source fingerprint (SHA-256):** `822f6b9fef67ef6beb1eba099c41c72570a1f79e316612201c81f6e5eb91408d`

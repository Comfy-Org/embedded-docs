# Luma UNI-1 Image Edit

Ce nœud modifie une image existante à l'aide d'une invite texte, propulsé par le modèle Luma UNI-1. Il prend une image source et une description de la modification souhaitée, puis génère une nouvelle version modifiée de l'image. Vous pouvez choisir entre les modèles `uni-1` et `uni-1-max`, ajuster le style, activer la recherche web et fournir éventuellement jusqu'à 8 images de référence.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `modèle` | Modèle à utiliser pour l'édition. La sélection d'un modèle révèle les options spécifiques au modèle ci-dessous. | DYNAMIC_COMBO | Oui | `"uni-1"`<br>`"uni-1-max"` |
| `source` | Image source à modifier. | IMAGE | Oui | - |
| `invite` | Description de la modification souhaitée. 1 à 6000 caractères. Par défaut : "" (chaîne vide ; la requête est invalide tant qu'au moins un caractère n'est pas saisi). | STRING | Oui | 1 à 6000 caractères |
| `graine` | Le seed contrôle si le nœud doit être réexécuté ; les résultats sont non déterministes quel que soit le seed. Par défaut : 0. | INT | Oui | 0 à 2147483647 |

### Entrées uni-1 et uni-1-max

Ces options sont partagées par les modèles `uni-1` et `uni-1-max`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `style` | Préréglage de style. `"auto"` choisit en fonction de l'invite ; `"manga"` applique une esthétique manga/anime et nécessite un format portrait (2:3, 9:16, 1:2, 1:3). Par défaut : `"auto"`. | COMBO | Oui | `"auto"`<br>`"manga"` |
| `web_search` | Rechercher sur le web des références visuelles avant de générer. Par défaut : false. | BOOLEAN | Oui | `true`<br>`false` |

### Entrées de référence

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image_ref` | Emplacement extensible : connectez jusqu'à 8 images de référence (`image_1` à `image_8`) pour guider le style/contenu. Facultatif. | IMAGE | Non | 0 à 8 images |

**Remarques :**
- Le paramètre `prompt` doit contenir entre 1 et 6000 caractères.
- Les entrées `style`, `web_search` et `image_ref` apparaissent lorsque `model` est défini sur `"uni-1"` ou `"uni-1-max"`.
- Les deux modèles prennent en charge les mêmes options spécifiques au modèle, y compris jusqu'à 8 images de référence.
- Le style `"manga"` nécessite un format portrait (2:3, 9:16, 1:2 ou 1:3).
- Connecter plus de 8 images de référence génère une erreur.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `image` | L'image modifiée générée par le modèle Luma UNI-1, renvoyée au format PNG. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageEditNode2/fr.md)

---
**Source fingerprint (SHA-256):** `66f62bb2807759edb405c2caeeefe32c341920924e267c32449a620190b9a7ab`

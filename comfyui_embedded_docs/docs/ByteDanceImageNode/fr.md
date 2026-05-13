> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceImageNode/fr.md)

Voici la traduction de la documentation du nœud ByteDance Image Node :

Le nœud ByteDance Image génère des images à l'aide des modèles ByteDance via une API, en se basant sur des invites textuelles. Il vous permet de sélectionner un modèle, de spécifier les dimensions de l'image et de contrôler divers paramètres de génération tels que le seed et l'échelle de guidage. Le nœud se connecte au service de génération d'images ByteDance et renvoie l'image créée.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `model` | STRING | Oui | `"seedream-3-0-t2i-250415"` | Le modèle ByteDance à utiliser pour la génération d'images. Actuellement, une seule option de modèle est disponible. |
| `prompt` | STRING | Oui | - | L'invite textuelle utilisée pour générer l'image. Doit contenir au moins 1 caractère après suppression des espaces. |
| `size_preset` | STRING | Oui | Voir description | Choisissez une taille recommandée. Sélectionnez Personnalisé pour utiliser la largeur et la hauteur ci-dessous. Les préréglages disponibles sont définis par la liste `RECOMMENDED_PRESETS`. |
| `width` | INT | Oui | 512 à 2048 (pas de 64) | Largeur personnalisée de l'image. Cette valeur n'est utilisée que lorsque `size_preset` est défini sur `Personnalisé`. Par défaut : 1024. |
| `height` | INT | Oui | 512 à 2048 (pas de 64) | Hauteur personnalisée de l'image. Cette valeur n'est utilisée que lorsque `size_preset` est défini sur `Personnalisé`. Par défaut : 1024. |
| `seed` | INT | Non | 0 à 2147483647 (pas de 1) | Seed à utiliser pour la génération. Par défaut : 0. |
| `guidance_scale` | FLOAT | Non | 1.0 à 10.0 (pas de 0.01) | Une valeur plus élevée fait que l'image suit l'invite plus fidèlement. Par défaut : 2.5. |
| `watermark` | BOOLEAN | Non | Vrai / Faux | Indique s'il faut ajouter un filigrane "Généré par IA" à l'image. Par défaut : Faux. Il s'agit d'un paramètre avancé. |

**Remarque sur les paramètres de taille :** Les paramètres `width` et `height` ne sont utilisés que lorsque `size_preset` est défini sur `Personnalisé`. Si une taille prédéfinie est sélectionnée, les dimensions du préréglage remplacent les valeurs personnalisées de largeur et de hauteur. La largeur et la hauteur doivent toutes deux être comprises entre 512 et 2048 pixels lors de l'utilisation de dimensions personnalisées.

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `IMAGE` | IMAGE | L'image générée renvoyée par l'API ByteDance sous forme de tenseur. |

---
**Source fingerprint (SHA-256):** `6ad3011ae942e81bc5e5296fa7120ee89637ef7487e2f12822d84b6917ec211e`

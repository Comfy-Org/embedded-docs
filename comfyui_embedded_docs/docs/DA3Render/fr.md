# Rendu Depth Anything 3

Ce nœud génère une visualisation à partir des données géométriques de Depth Anything 3. Il peut produire des cartes de profondeur, des cartes de confiance ou des masques de ciel selon le mode de sortie sélectionné.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `da3_geometry` | Le paquet de données géométriques Depth Anything 3 contenant la profondeur, et optionnellement les tenseurs de ciel et de confiance | DA3_GEOMETRY | Oui | - |
| `output` | Le type de visualisation à générer. Les options incluent depth, depth_colored, sky_mask et confidence. Chaque option possède son propre ensemble de sous-paramètres. | COMBO | Oui | `"depth"`<br>`"depth_colored"`<br>`"sky_mask"`<br>`"confidence"` |

### Sous-paramètres pour les options `output`

Lorsque `output` est défini sur `"depth"` ou `"depth_colored"` :

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `normalization` | La méthode de normalisation de la profondeur. v2_style utilise la normalisation moyenne/écart-type pour des résultats perceptuellement équilibrés (par défaut). min_max étend la plage complète de profondeur à [0, 1] pour un contraste maximal. raw préserve les unités métriques pour le modèle Metric sans mise à l'échelle. | COMBO | Oui | `"v2_style"`<br>`"min_max"`<br>`"raw"` |
| `apply_sky_clip` | Limiter la profondeur de la région du ciel au 99e percentile de la profondeur du premier plan avant la normalisation. Nécessite une clé sky dans l'entrée da3_geometry (pour les modèles Mono/Metric uniquement). Par défaut : False | BOOLEAN | Oui | True<br>False |

Lorsque `output` est défini sur `"sky_mask"` :

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `colored` | Appliquer la carte de couleurs Turbo au masque de ciel. Par défaut : False | BOOLEAN | Oui | True<br>False |

Lorsque `output` est défini sur `"confidence"` :

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `colored` | Appliquer la carte de couleurs Turbo à la carte de confiance. Par défaut : False | BOOLEAN | Oui | True<br>False |

### Contraintes des paramètres

- Lorsque `apply_sky_clip` est défini sur True, l'entrée `da3_geometry` doit contenir un tenseur de ciel. Ceci n'est disponible qu'avec les modèles Mono ou Metric. Si le tenseur de ciel est manquant, le nœud générera une erreur.
- L'option de sortie `sky_mask` nécessite un tenseur de ciel dans l'entrée `da3_geometry`. Ceci n'est disponible qu'avec les modèles Mono ou Metric.
- L'option de sortie `confidence` nécessite un tenseur de confiance dans l'entrée `da3_geometry`. Ceci n'est disponible qu'avec les modèles Small ou Base.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `IMAGE` | La visualisation générée sous forme de tenseur d'image. Pour les sorties de profondeur, retourne une carte de profondeur en niveaux de gris ou colorée. Pour sky_mask et confidence, retourne une visualisation en niveaux de gris ou colorée selon le paramètre colored. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DA3Render/fr.md)

---
**Source fingerprint (SHA-256):** `54d4cde95a916cac26c8a2e19c5623e794d46c0d7652f1c8204f9f2a0deabe0c`

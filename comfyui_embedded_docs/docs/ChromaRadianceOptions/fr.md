> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ChromaRadianceOptions/fr.md)

Le nœud ChromaRadianceOptions vous permet de configurer les paramètres avancés du modèle Chroma Radiance. Il encapsule un modèle existant et applique des options spécifiques pendant le processus de débruitage en fonction des valeurs sigma, offrant un contrôle précis sur la taille des tuiles NeRF et d'autres paramètres liés à la radiance.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `modèle` | MODEL | Oui | - | Le modèle auquel appliquer les options Chroma Radiance |
| `préserver_wrapper` | BOOLEAN | Non | - | Lorsqu'activé, délègue à un wrapper de fonction de modèle existant s'il existe. Doit généralement rester activé. (par défaut : True) |
| `sigma_début` | FLOAT | Non | 0,0 à 1,0 | Premier sigma pour lequel ces options seront actives. (par défaut : 1,0) |
| `sigma_fin` | FLOAT | Non | 0,0 à 1,0 | Dernier sigma pour lequel ces options seront actives. (par défaut : 0,0) |
| `taille_tuile_nerf` | INT | Non | -1 et plus | Permet de remplacer la taille par défaut des tuiles NeRF. -1 signifie utiliser la valeur par défaut (32). 0 signifie utiliser le mode sans tuilage (peut nécessiter beaucoup de VRAM). (par défaut : -1) |

**Remarque :** Les options Chroma Radiance ne prennent effet que lorsque la valeur sigma actuelle se situe entre `end_sigma` et `start_sigma` (inclus). Le paramètre `nerf_tile_size` n'est appliqué que lorsqu'il est défini sur 0 ou une valeur supérieure.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `modèle` | MODEL | Le modèle modifié avec les options Chroma Radiance appliquées |

---
**Source fingerprint (SHA-256):** `b49a12e9aba59e4669c59e05a6aeff6d4ae5a4b656ca5b0de4bdf71291dca095`

# OptionsChromaRadiance

Le nœud ChromaRadianceOptions vous permet de configurer des paramètres avancés pour le modèle Chroma Radiance. Il enveloppe un modèle existant et applique des options spécifiques pendant le processus de débruitage en fonction des valeurs sigma, permettant un contrôle fin de la taille des tuiles NeRF et d'autres paramètres liés à la radiance.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `modèle` | Le modèle auquel appliquer les options Chroma Radiance | MODEL | Oui | - |
| `préserver_wrapper` | Lorsqu'elle est activée, délègue à un wrapper de fonction de modèle existant s'il existe. En général, doit rester activée. (par défaut : True) | BOOLEAN | Non | - |
| `sigma_début` | Premier sigma pour lequel ces options seront en vigueur. (par défaut : 1.0) | FLOAT | Non | 0.0 à 1.0 |
| `sigma_fin` | Dernier sigma pour lequel ces options seront en vigueur. (par défaut : 0.0) | FLOAT | Non | 0.0 à 1.0 |
| `taille_tuile_nerf` | Permet de remplacer la taille de tuile NeRF par défaut. -1 signifie utiliser la valeur par défaut (32). 0 signifie utiliser le mode sans tuilage (peut nécessiter beaucoup de VRAM). (par défaut : -1) | INT | Non | -1 et plus |
| `force_sequential_txt_ids` | Force l'utilisation d'identifiants de jetons de texte séquentiels au lieu de zéros. Doit être utilisé pour les checkpoints du 2026-05-22 au 2026-06-01 qui sont entraînés de cette manière mais ne contiennent pas la clé __sequential__ dans le dictionnaire d'état. (par défaut : False) | BOOLEAN | Non | - |

**Remarque :** Les options Chroma Radiance ne prennent effet que lorsque la valeur sigma actuelle se situe entre `end_sigma` et `start_sigma` (inclus). Le paramètre `nerf_tile_size` n'est appliqué que lorsqu'il est défini sur 0 ou une valeur supérieure. Le paramètre `force_sequential_txt_ids` n'est appliqué que lorsqu'il est défini sur True. Lorsque `nerf_tile_size` est -1 et que `force_sequential_txt_ids` est False, aucune option n'est configurée et le modèle est retourné inchangé sans aucun wrapper appliqué.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `model` | Le modèle avec les options Chroma Radiance appliquées, ou le modèle inchangé si aucune option n'est active | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ChromaRadianceOptions/fr.md)

---
**Source fingerprint (SHA-256):** `761f1946fe1fd77158e97f6f34d002e2445cc00e008741f8c37cde5673900409`

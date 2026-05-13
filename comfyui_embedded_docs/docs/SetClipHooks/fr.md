> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetClipHooks/fr.md)

Le nœud SetClipHooks permet d'appliquer des hooks personnalisés à un modèle CLIP, permettant des modifications avancées de son comportement. Il peut appliquer des hooks aux sorties de conditionnement et activer optionnellement la fonctionnalité de planification CLIP. Ce nœud crée une copie clonée du modèle CLIP d'entrée avec les configurations de hooks spécifiées appliquées.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `clip` | CLIP | Oui | - | Le modèle CLIP auquel appliquer les hooks |
| `appliquer_à_conds` | BOOLEAN | Oui | - | Appliquer les hooks aux sorties de conditionnement (par défaut : True) |
| `programmer_clip` | BOOLEAN | Oui | - | Activer la planification CLIP (par défaut : False) |
| `crochets` | HOOKS | Non | - | Groupe de hooks optionnel à appliquer au modèle CLIP |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `clip` | CLIP | Un modèle CLIP cloné avec les hooks spécifiés appliqués |

---
**Source fingerprint (SHA-256):** `904a878638c015bdce1983ae0c11a2b580b271090fca39edb304f6ed90c8c66d`

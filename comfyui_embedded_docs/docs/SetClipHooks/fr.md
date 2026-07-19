# Définir les Crochets CLIP

Le nœud SetClipHooks permet d'appliquer des hooks personnalisés à un modèle CLIP, permettant des modifications avancées de son comportement. Il peut appliquer des hooks aux sorties de conditionnement et activer optionnellement la fonctionnalité de planification CLIP. Ce nœud crée une copie clonée du modèle CLIP d'entrée avec les configurations de hooks spécifiées appliquées.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `clip` | Le modèle CLIP auquel appliquer les hooks | CLIP | Oui | - |
| `appliquer_à_conds` | Appliquer les hooks aux sorties de conditionnement (par défaut : True) | BOOLEAN | Oui | - |
| `programmer_clip` | Activer la planification CLIP (par défaut : False) | BOOLEAN | Oui | - |
| `crochets` | Groupe de hooks optionnel à appliquer au modèle CLIP | HOOKS | Non | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `clip` | Un modèle CLIP cloné avec les hooks spécifiés appliqués | CLIP |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetClipHooks/fr.md)

---
**Source fingerprint (SHA-256):** `904a878638c015bdce1983ae0c11a2b580b271090fca39edb304f6ed90c8c66d`

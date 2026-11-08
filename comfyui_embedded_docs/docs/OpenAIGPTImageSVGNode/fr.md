# OpenAI GPT Image 2.6 SVG

## Aperçu

OpenAI GPT Image 2.6 SVG génère un SVG modifiable à partir d’une invite avec les modèles GPT Image d’OpenAI. Le résultat est un balisage vectoriel, de sorte que les formes et le texte restent modifiables dans un éditeur vectoriel. Deux modèles sont disponibles : `gpt-image-2.6-flare` et `gpt-image-2.6-sunburst`.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Le modèle GPT Image à utiliser pour le SVG. | DYNAMIC_COMBO | Oui | `"gpt-image-2.6-flare"`<br>`"gpt-image-2.6-sunburst"` |

### Entrées gpt-image-2.6-flare et gpt-image-2.6-sunburst

Les deux modèles partagent les mêmes paramètres.

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model.prompt` | Description du SVG à dessiner. (par défaut : `""`) | STRING | Oui | N/A |
| `model.size` | Taille de l’image de référence à partir de laquelle le SVG est dessiné. (par défaut : `"1024x1024"`) | COMBO | Oui | `"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"` |
| `model.background` | Arrière-plan de l’image de référence. (par défaut : `"auto"`) | COMBO | Oui | `"auto"`<br>`"opaque"`<br>`"transparent"` |
| `model.quality` | Qualité de l’image de référence à partir de laquelle le SVG est dessiné. (par défaut : `"low"`) | COMBO | Oui | `"low"`<br>`"medium"`<br>`"high"`<br>`"xhigh"`<br>`"max"` |
| `model.complexity` | Dans quelle mesure le modèle planifie l’image de référence avant le rendu. (par défaut : `"high"`) | COMBO | Oui | `"low"`<br>`"medium"`<br>`"high"` |
| `model.seed` | Contrôle si le nœud s’exécute à nouveau ; les résultats ne sont pas déterministes, quelle que soit la graine. (par défaut : `42`) | INT | Oui | 0 à 2147483647 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `svg` | L’image vectorielle générée sous forme de balisage SVG. | SVG |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIGPTImageSVGNode/fr.md)

---
**Source fingerprint (SHA-256):** `8ac2f473b265d3b6857e6280a1c017301b124fc6d671ec83a59c677218062c90`

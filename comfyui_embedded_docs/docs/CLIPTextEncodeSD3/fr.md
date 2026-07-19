# CLIPTextEncodeSD3

Le nœud CLIPTextEncodeSD3 traite les entrées textuelles pour les modèles Stable Diffusion 3 en encodant plusieurs invites textuelles à l'aide de différents modèles CLIP. Il gère trois entrées textuelles distinctes (`clip_g`, `clip_l` et `t5xxl`) et propose des options pour gérer le remplissage de texte vide. Le nœud assure un alignement correct des jetons entre les différentes entrées textuelles et renvoie des données de conditionnement adaptées aux pipelines de génération SD3.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `clip` | Le modèle CLIP utilisé pour l'encodage du texte | CLIP | Oui | - |
| `clip_l` | Entrée textuelle pour le modèle CLIP local. Prend en charge le texte multiligne et les invites dynamiques. | STRING | Oui | - |
| `clip_g` | Entrée textuelle pour le modèle CLIP global. Prend en charge le texte multiligne et les invites dynamiques. | STRING | Oui | - |
| `t5xxl` | Entrée textuelle pour le modèle T5-XXL. Prend en charge le texte multiligne et les invites dynamiques. | STRING | Oui | - |
| `remplissage_vide` | Contrôle la gestion des entrées textuelles vides. Lorsqu'il est défini sur "none", les entrées textuelles vides pour `clip_g`, `clip_l` ou `t5xxl` produiront des listes de jetons vides au lieu d'un remplissage. Il s'agit d'un paramètre avancé (par défaut : "none"). | COMBO | Oui | `"none"`<br>`"empty_prompt"` |

**Contraintes des paramètres :**

- Lorsque `empty_padding` est défini sur "none", les entrées textuelles vides pour `clip_g`, `clip_l` ou `t5xxl` produiront des listes de jetons vides au lieu d'un remplissage
- Le nœud équilibre automatiquement les longueurs de jetons entre les entrées `clip_l` et `clip_g` en remplissant la plus courte avec des jetons vides lorsque les longueurs diffèrent
- Toutes les entrées textuelles prennent en charge les invites dynamiques et la saisie de texte multiligne

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `CONDITIONING` | Les données de conditionnement textuel encodées, prêtes à être utilisées dans les pipelines de génération SD3 | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeSD3/fr.md)

---
**Source fingerprint (SHA-256):** `38f7538d05fe48e74f41f265550b83906b2f0c5d31f0783f6859f4df7b5cb9d3`

# CLIPTextEncodeSD3

CLIPTextEncodeSD3 traite les entrées de texte pour les modèles Stable Diffusion 3 en encodant plusieurs invites texte à l'aide de différents modèles CLIP. Il gère trois entrées de texte distinctes (`clip_g`, `clip_l` et `t5xxl`) et propose des options pour gérer le remplissage des textes vides. Le nœud assure un alignement correct des jetons entre les différentes entrées de texte et renvoie des données de conditionnement adaptées aux pipelines de génération SD3.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `clip` | Le modèle CLIP utilisé pour l'encodage du texte. | CLIP | Oui | - |
| `clip_l` | Entrée de texte pour le modèle CLIP local. Prend en charge le texte multiligne et les invites dynamiques. | STRING | Oui | - |
| `clip_g` | Entrée de texte pour le modèle CLIP global. Prend en charge le texte multiligne et les invites dynamiques. | STRING | Oui | - |
| `t5xxl` | Entrée de texte pour le modèle T5-XXL. Prend en charge le texte multiligne et les invites dynamiques. | STRING | Oui | - |
| `remplissage_vide` | Contrôle la gestion des entrées de texte vides. Lorsqu'elle est définie sur « none », les entrées de texte vides pour `clip_g`, `clip_l` ou `t5xxl` produisent des listes de jetons vides au lieu d'un remplissage. Lorsqu'elle est définie sur « empty_prompt », les entrées vides sont tokenisées comme des invites vides (comportement de remplissage standard). Il s'agit d'un paramètre avancé (par défaut : « none »). | COMBO | Oui | `"none"`<br>`"empty_prompt"` |

**Contraintes des paramètres :**

- Lorsque `empty_padding` est défini sur « none », les entrées de texte vides pour `clip_g`, `clip_l` ou `t5xxl` produisent des listes de jetons vides au lieu d'un remplissage.
- Le nœud équilibre automatiquement les longueurs de jetons entre les entrées `clip_l` et `clip_g` en remplissant la plus courte avec des jetons vides lorsque les longueurs diffèrent.
- Toutes les entrées de texte prennent en charge les invites dynamiques et la saisie de texte multiligne.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `CONDITIONING` | Les données de conditionnement de texte encodé prêtes à être utilisées dans les pipelines de génération SD3. | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeSD3/fr.md)

---
**Source fingerprint (SHA-256):** `874869bac024e6b5ac6b4bf4f79c31bb750e54f7096f6638647aac6b95bb202f`

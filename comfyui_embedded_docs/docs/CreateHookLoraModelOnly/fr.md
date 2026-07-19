# Créer un crochet LoRA (MO)

Ce nœud crée un hook LoRA (Adaptation de Bas Rang) qui s'applique uniquement au composant modèle, laissant le composant CLIP totalement inchangé. Il charge un fichier LoRA et l'applique avec une force spécifiée au modèle tout en réglant la force CLIP à zéro. Le nœud peut être chaîné avec des hooks précédents pour construire des pipelines de modification complexes.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `nom_lora` | Le nom du fichier LoRA à charger depuis le dossier loras | STRING | Oui | Plusieurs options disponibles |
| `force_modele` | Le multiplicateur de force pour appliquer le LoRA au composant modèle (par défaut : 1.0) | FLOAT | Oui | -20.0 à 20.0 |
| `crochets_precedents` | Hooks précédents optionnels à chaîner avec ce hook | HOOKS | Non | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `hooks` | Le hook LoRA créé qui peut être appliqué au traitement du modèle | HOOKS |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookLoraModelOnly/fr.md)

---
**Source fingerprint (SHA-256):** `10adbdfc2e37fcf317e93130f87d9a7038d00b091cb6d1b45f4658c81632ef80`

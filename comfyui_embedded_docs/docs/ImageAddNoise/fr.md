# Ajout de bruit à l'image

Le nœud ImageAddNoise ajoute un bruit aléatoire à une image d'entrée. Il utilise une graine aléatoire spécifiée pour générer des motifs de bruit cohérents et permet de contrôler l'intensité de l'effet de bruit. L'image résultante conserve les mêmes dimensions que l'entrée, mais avec une texture visuelle ajoutée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `image` | L'image d'entrée à laquelle le bruit sera ajouté | IMAGE | Oui | - |
| `seed` | La graine aléatoire utilisée pour créer le bruit (par défaut : 0). Ce paramètre prend en charge la fonctionnalité « contrôle après génération ». | INT | Oui | 0 à 18446744073709551615 |
| `strength` | Contrôle l'intensité de l'effet de bruit (par défaut : 0.5, pas : 0.01) | FLOAT | Oui | 0.0 à 1.0 |

**Remarque :** Les valeurs de bruit sont ajoutées à l'image et le résultat est borné à la plage 0.0–1.0. Si l'image d'entrée possède un canal alpha (4 canaux), le canal alpha d'origine est conservé inchangé — le bruit est uniquement appliqué aux canaux de couleur.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `image` | L'image de sortie avec le bruit ajouté | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageAddNoise/fr.md)

---
**Source fingerprint (SHA-256):** `e6b9815e7c075c7ee97c924c22a92dfef6d9c65b97b6e65b0f9e1c96628f39f2`

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProUltraImageNode/fr.md)

Génère des images en utilisant Flux Pro 1.1 Ultra via API, en fonction d'une instruction textuelle et d'une résolution. Ce nœud se connecte à un service externe pour créer des images selon votre description textuelle et les dimensions spécifiées.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `prompt` | STRING | Oui | - | Instruction textuelle pour la génération d'image (valeur par défaut : chaîne vide) |
| `prompt_upsampling` | BOOLEAN | Non | - | Indique s'il faut effectuer un sur-échantillonnage de l'instruction textuelle. Si activé, modifie automatiquement l'instruction pour une génération plus créative, mais les résultats ne sont pas déterministes (une même graine ne produira pas exactement le même résultat). (valeur par défaut : False) |
| `seed` | INT | Non | 0 à 18446744073709551615 | La graine aléatoire utilisée pour créer le bruit. (valeur par défaut : 0) |
| `aspect_ratio` | STRING | Non | - | Rapport hauteur/largeur de l'image ; doit être compris entre 1:4 et 4:1. (valeur par défaut : "16:9") |
| `raw` | BOOLEAN | Non | - | Lorsque True, génère des images moins traitées et d'apparence plus naturelle. (valeur par défaut : False) |
| `image_prompt` | IMAGE | Non | - | Image de référence optionnelle pour guider la génération |
| `image_prompt_strength` | FLOAT | Non | 0.0 à 1.0 | Mélange entre l'instruction textuelle et l'image de référence. (valeur par défaut : 0.1) |

**Remarque :** Le paramètre `aspect_ratio` doit être compris entre 1:4 et 4:1. Lorsque `image_prompt` est fourni, `image_prompt_strength` devient actif et contrôle l'influence de l'image de référence sur le résultat final. Si `image_prompt` n'est pas fourni, le paramètre `prompt` est validé pour s'assurer qu'il n'est pas vide.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `output_image` | IMAGE | L'image générée par Flux Pro 1.1 Ultra |

---
**Source fingerprint (SHA-256):** `8632aeb76e9007d65d7f3fd51465fe78f56ba92264ef65ce505db2fc95cfd25b`

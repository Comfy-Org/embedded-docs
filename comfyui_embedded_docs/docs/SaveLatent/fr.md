# EnregistrerLatent

Le nœud SaveLatent enregistre des échantillons latents sur le disque sous forme de fichiers .latent pour une utilisation ou un partage ultérieur. Il écrit les données du tenseur latent dans le dossier de sortie en utilisant le préfixe de nom de fichier spécifié, et intègre des métadonnées facultatives telles que les informations de prompt. Le nœud renvoie également les échantillons latents d'origine inchangés, afin que le workflow puisse continuer à les utiliser.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `samples` | Les échantillons latents à enregistrer sur le disque | LATENT | Oui | - |
| `filename_prefix` | Le préfixe utilisé pour générer le nom de fichier de sortie et le chemin du sous-dossier (par défaut : "latents/ComfyUI") | STRING | Oui | - |
| `prompt` | Les données de prompt du workflow, stockées sous forme de métadonnées JSON dans le fichier enregistré (entrée masquée, fournie automatiquement) | PROMPT | Non | - |
| `extra_pnginfo` | Métadonnées supplémentaires du workflow, stockées sous forme de JSON dans le fichier enregistré (entrée masquée, fournie automatiquement) | EXTRA_PNGINFO | Non | - |

Remarque : Les métadonnées sont écrites dans le fichier .latent enregistré, sauf si ComfyUI est démarré avec l'argument `--disable-metadata`. Le fichier enregistré est nommé selon le modèle `{filename}_{compteur à 5 chiffres}_.latent`, par exemple `ComfyUI_00001_.latent`.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `samples` | Les échantillons latents d'origine, renvoyés inchangés | LATENT |
| `ui` | Détails de l'emplacement du fichier (nom de fichier, sous-dossier et type de sortie) pour le fichier latent enregistré | UI |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveLatent/fr.md)

---
**Source fingerprint (SHA-256):** `137d52d589d93d8229940a8572621ab6eeb25a4e13ac05172e9f8609f1af038a`

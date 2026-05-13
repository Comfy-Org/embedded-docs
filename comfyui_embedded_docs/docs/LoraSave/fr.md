> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraSave/fr.md)

Le nœud LoraSave extrait et enregistre des fichiers LoRA (Adaptation de Bas Rang) à partir de différences de modèles. Il peut traiter les différences de modèles de diffusion, les différences d'encodeur de texte, ou les deux, en les convertissant au format LoRA avec un rang et un type spécifiés. Le fichier LoRA résultant est sauvegardé dans le répertoire de sortie pour une utilisation ultérieure.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `filename_prefix` | STRING | Oui | - | Le préfixe pour le nom du fichier de sortie (par défaut : "loras/ComfyUI_extracted_lora") |
| `rank` | INT | Oui | 1-4096 | La valeur de rang pour le LoRA, contrôlant la taille et la complexité (par défaut : 8) |
| `lora_type` | COMBO | Oui | `"standard"`<br>`"locon"`<br>`"loha"`<br>`"lokr"`<br>`"dylora"` | Le type de LoRA à créer (par défaut : "standard") |
| `bias_diff` | BOOLEAN | Oui | - | Indique s'il faut inclure les différences de biais dans le calcul LoRA (par défaut : True) |
| `model_diff` | MODEL | Non | - | La sortie ModelSubtract à convertir en lora |
| `text_encoder_diff` | CLIP | Non | - | La sortie CLIPSubtract à convertir en lora |

**Remarque :** Au moins l'un des paramètres `model_diff` ou `text_encoder_diff` doit être fourni pour que le nœud fonctionne. Si les deux sont omis, le nœud ne produira aucune sortie.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| - | - | Ce nœud enregistre un fichier LoRA dans le répertoire de sortie mais ne renvoie aucune donnée via le workflow |

---
**Source fingerprint (SHA-256):** `fdf020915ee233cf68250dcdcf87e7862d13ccc4fa73d8da8245727fdac46015`

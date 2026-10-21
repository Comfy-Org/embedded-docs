# Bria FIBO 2.0 Image Generate

Génère une nouvelle image à partir d'un prompt textuel, d'un prompt JSON structuré ou d'une seule image de référence avec Bria FIBO 2.0. Le nœud envoie la requête à l'API Bria, attend la fin de la génération et renvoie l'image ainsi qu'un prompt structuré permettant de la recréer ou de l'affiner lors d'une exécution ultérieure.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Description en langage naturel de l'image à générer (par défaut : vide). | STRING | Oui | Texte multiligne |
| `structured_prompt` | Prompt structuré JSON provenant d'un résultat Bria FIBO précédent. Avec la même graine, il recrée cette image ; modifiez le JSON ou ajoutez un prompt pour l'affiner (par défaut : vide). | STRING | Oui | Texte multiligne |
| `aspect_ratio` | Ratio d'aspect de sortie (par défaut : `"1:1"`). Les ratios à partir de `"16:10"` sont des tailles FIBO 2.0 avec des exigences supplémentaires, listées ci-dessous. | COMBO | Oui | `"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"`<br>`"16:10"`<br>`"10:16"`<br>`"2:1"`<br>`"1:2"`<br>`"21:9"`<br>`"9:21"`<br>`"3:1"`<br>`"1:3"`<br>`"4:1"`<br>`"1:4"`<br>`"5:1"`<br>`"1:5"` |
| `resolution` | Résolution de sortie en mégapixels (par défaut : `"1MP"`). | COMBO | Oui | `"1MP"`<br>`"4MP"` |
| `seed` | Graine qui initialise la génération (par défaut : 42). | INT | Oui | 1 à 2147483647 |
| `moderation` | Paramètres de modération. Sélectionner `"true"` révèle les entrées de modération listées ci-dessous. | DYNAMIC_COMBO | Oui | `"false"`<br>`"true"` |
| `image` | Image de référence facultative sur laquelle s'appuyer. Le résultat est une nouvelle image au ratio d'aspect sélectionné, et non une édition de cette image. | IMAGE | Non | - |

### Entrées de modération

Lorsque `moderation` est défini sur `"true"`, ces entrées supplémentaires deviennent disponibles :

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt_content_moderation` | Indique s'il faut modérer le texte du prompt ; la requête échoue lorsque la modération le rejette (par défaut : false). | BOOLEAN | Non | `true`<br>`false` |
| `visual_input_moderation` | Indique s'il faut modérer l'image de référence ; la requête échoue lorsque la modération la rejette (par défaut : false). | BOOLEAN | Non | `true`<br>`false` |
| `visual_output_moderation` | Indique s'il faut modérer l'image générée ; la requête échoue lorsque la modération la rejette (par défaut : false). | BOOLEAN | Non | `true`<br>`false` |

**Contraintes importantes :**

- Fournissez au moins l'un des éléments suivants : `prompt`, `structured_prompt` ou une `image` de référence. Si les trois sont vides, le nœud génère une erreur.
- Une image de référence ne peut pas être combinée avec `structured_prompt` : utilisez l'un ou l'autre.
- Les ratios FIBO 2.0 (`"16:10"`, `"10:16"`, `"2:1"`, `"1:2"`, `"21:9"`, `"9:21"`, `"3:1"`, `"1:3"`, `"4:1"`, `"1:4"`, `"5:1"`, `"1:5"`) nécessitent `resolution` `"1MP"` et exactement l'un de `prompt` ou `structured_prompt`.
- Ce nœud est un nœud API payant ; ComfyUI facture environ 0,0572 USD par exécution.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `IMAGE` | L'image générée renvoyée par l'API Bria. | IMAGE |
| `structured_prompt` | Description structurée de l'image générée, pour la recréer ou l'affiner avec ce nœud. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaImageGenerate/fr.md)

---
**Source fingerprint (SHA-256):** `4d53fe457e2e349ac41b5c8a0d3d5599eafa53cb653c470335853f1d4517688f`

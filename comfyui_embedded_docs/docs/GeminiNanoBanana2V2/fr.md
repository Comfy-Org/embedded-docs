# Nano Banana 2

Ce nœud génère ou modifie des images en envoyant une invite texte à l'API Vertex AI de Google via les modèles Gemini 3.1 Flash Image. Il crée de nouvelles images à partir d'une description ou modifie des images existantes à l'aide d'images de référence facultatives.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Invite texte décrivant l'image à générer ou les modifications à appliquer. Incluez toutes les contraintes, styles ou détails que le modèle doit suivre. Ne doit pas être vide. | STRING | Oui | N/A |
| `modèle` | Sélectionne le modèle Gemini à utiliser pour la génération d'images. Ce paramètre inclut des sous-paramètres supplémentaires pour la résolution, le rapport d'aspect, le niveau de réflexion et les entrées de référence. | DYNAMIC_COMBO | Oui | `"Nano Banana 2 (Gemini 3.1 Flash Image)"`<br>`"Nano Banana 2 Lite"` |
| `graine` | Lorsque le seed est fixé à une valeur spécifique, le modèle fait de son mieux pour fournir la même réponse aux requêtes répétées. La sortie déterministe n'est pas garantie. De plus, modifier le modèle ou les paramètres, tels que la température, peut entraîner des variations dans la réponse même si vous utilisez la même valeur de seed. Par défaut, une valeur de seed aléatoire est utilisée. (par défaut : 42) | INT | Oui | 0 à 18446744073709551615 |
| `modalités de réponse` | Détermine le format de réponse. IMAGE renvoie uniquement une image ; IMAGE+TEXT renvoie une image et une réponse texte. (par défaut : IMAGE) Paramètre avancé. | COMBO | Oui | `"IMAGE"`<br>`"IMAGE+TEXT"` |
| `invite système` | Instructions fondamentales qui régissent le comportement d'une IA. Par défaut, il s'agit d'une invite intégrée qui ordonne au modèle de toujours produire une image. Paramètre avancé. | STRING | Non | N/A |
| `température` | Contrôle le caractère aléatoire de la génération. Une valeur plus faible donne un résultat plus ciblé/déterministe. (par défaut : 1.0) Paramètre avancé. | FLOAT | Non | 0.0 à 2.0 (pas de 0.01) |
| `top_p` | Seuil d'échantillonnage nucleus. Une valeur plus faible est plus ciblée, une valeur plus élevée est plus diversifiée. (par défaut : 0.95) Paramètre avancé. | FLOAT | Non | 0.0 à 1.0 (pas de 0.01) |

### Nano Banana 2 (Gemini 3.1 Flash Image) Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `aspect_ratio` | Si elle est définie sur 'auto', la valeur correspond au rapport d'aspect de votre image d'entrée ; si aucune image n'est fournie, un format 16:9 est généralement généré. (par défaut : auto) | COMBO | Oui | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"`<br>`"21:9"`<br>`"1:4"`<br>`"4:1"`<br>`"8:1"`<br>`"1:8"` |
| `resolution` | Résolution de sortie cible. | COMBO | Oui | `"1K"`<br>`"2K"`<br>`"4K"` |
| `thinking_level` | Sélectionne le niveau de réflexion utilisé par le modèle. | COMBO | Oui | `"MINIMAL"`<br>`"HIGH"` |

### Nano Banana 2 Lite Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `aspect_ratio` | Si elle est définie sur 'auto', la valeur correspond au rapport d'aspect de votre image d'entrée ; si aucune image n'est fournie, un format 16:9 est généralement généré. (par défaut : auto) | COMBO | Oui | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"`<br>`"21:9"`<br>`"1:4"`<br>`"4:1"`<br>`"8:1"`<br>`"1:8"` |
| `resolution` | Résolution de sortie cible. | COMBO | Oui | `"1K"` |
| `thinking_level` | Sélectionne le niveau de réflexion utilisé par le modèle. | COMBO | Oui | `"MINIMAL"`<br>`"HIGH"` |

### Entrées de référence

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `images` | Image(s) de référence facultative(s). Jusqu'à 14 images au total. Emplacement extensible : connectez `image_1` à `image_14`. | IMAGE | Non | 0 à 14 images |
| `files` | Fichier(s) facultatif(s) à utiliser comme contexte pour le modèle. Accepte les entrées du nœud Gemini Generate Content Input Files. | GEMINI_INPUT_FILES | Non | N/A |

**Remarque :** Un maximum de 14 images de référence peut être connecté à l'entrée `images`.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `IMAGE` | L'image générée ou modifiée. | IMAGE |
| `STRING` | Une description textuelle ou une légende générée par le modèle. | STRING |
| `image de réflexion` | Première image du processus de réflexion du modèle. Disponible uniquement avec `thinking_level` HIGH et la modalité IMAGE+TEXT. | IMAGE |

**Remarque :** La sortie `STRING` est vide lorsque `response_modalities` est défini sur `IMAGE`.

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNanoBanana2V2/fr.md)

---
**Source fingerprint (SHA-256):** `347d28aeb46aa91f7515a31c385a3e3f805a1861116a21dd2ef6575ab7fd4f3e`

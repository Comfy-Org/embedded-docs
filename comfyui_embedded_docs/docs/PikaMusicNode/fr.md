# Pika Music

Ce nœud génère de la musique à partir d’une description textuelle et de paroles facultatives, ou reprend une chanson que vous fournissez, avec Pika. Choisissez `"text to music"` pour écrire une nouvelle chanson d’une durée que vous définissez, ou `"cover"` pour réenregistrer une chanson en conservant sa durée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `mode` | Ce que fait le nœud : `"text to music"` écrit une nouvelle chanson, `"cover"` réenregistre une chanson fournie. Chaque mode affiche ses propres entrées ci-dessous. Par défaut : `"text to music"`. | DYNAMIC_COMBO | Oui | `"text to music"`<br>`"cover"` |

### Entrées Text to Music

Ces entrées apparaissent lorsque `mode` est défini sur `"text to music"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | L’aspect sonore souhaité pour la musique. Ne doit pas être vide. Par défaut : "" (chaîne vide). | STRING | Oui | 1 à 4000 caractères |
| `lyrics` | Paroles facultatives. Les balises de section telles que `[Verse]` et `[Chorus]` sont autorisées. Par défaut : "" (chaîne vide). | STRING | Oui | 0 à 8000 caractères |
| `duration` | Durée de la chanson en secondes. Par défaut : 30.0. | FLOAT | Oui | 10.0 à 360.0 (pas : 0.1) |
| `rewrite_prompt` | Développe un prompt court ou vague à l’aide d’un modèle avant la génération. Par défaut : False. | BOOLEAN | Oui | true<br>false |
| `seed` | Graine pour l’échantillonnage. Par défaut : 42. | INT | Oui | 0 à 2147483647 |

### Entrées Cover

Ces entrées apparaissent lorsque `mode` est défini sur `"cover"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `source_audio` | La chanson à reprendre. Le résultat a la même durée, limitée entre 5 et 360 secondes. | AUDIO | Oui | - |
| `prompt` | L’aspect sonore souhaité pour la reprise. Ne doit pas être vide. Par défaut : "" (chaîne vide). | STRING | Oui | 1 à 4000 caractères |
| `lyrics` | Paroles facultatives. Les balises de section telles que `[Verse]` et `[Chorus]` sont autorisées. Par défaut : "" (chaîne vide). | STRING | Oui | 0 à 8000 caractères |
| `rewrite_prompt` | Développe un prompt court ou vague à l’aide d’un modèle avant la génération. Par défaut : False. | BOOLEAN | Oui | true<br>false |
| `seed` | Graine pour l’échantillonnage. Par défaut : 42. | INT | Oui | 0 à 2147483647 |

**Contraintes :**

* Le prompt doit contenir entre 1 et 4000 caractères, et les paroles 8000 caractères ou moins.
* Le mode Cover ignore `duration` : la sortie correspond à la durée de `source_audio`, limitée entre 5 et 360 secondes.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `AUDIO` | La chanson générée, ou la reprise de la piste fournie. | AUDIO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaMusicNode/fr.md)

---
**Source fingerprint (SHA-256):** `e3051b2d0cfff72cf7e359d7383f4e0d133df0338ff42a00f0649387f504ec28`

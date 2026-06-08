Voici la traduction en français de la documentation technique du nœud ComfyUI, conformément à vos règles :

---

### Aperçu

Le nœud Fenêtres de Contexte (Manuel) vous permet de configurer manuellement les fenêtres de contexte pour les modèles lors de l'échantillonnage. Il crée des segments de contexte qui se chevauchent, avec une longueur, un chevauchement et des motifs de planification spécifiés, afin de traiter les données par blocs gérables tout en maintenant la continuité entre les segments. Ce nœud offre des options avancées pour contrôler la manière dont les fenêtres de contexte sont appliquées, notamment le mélange de bruit, la conservation du conditionnement et les corrections de fenêtre causale.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle auquel appliquer les fenêtres de contexte lors de l'échantillonnage. | MODEL | Oui | - |
| `longueur_contexte` | La longueur de la fenêtre de contexte (par défaut : 16). | INT | Non | 1+ |
| `chevauchement_contexte` | Le chevauchement de la fenêtre de contexte (par défaut : 4). | INT | Non | 0+ |
| `planification_contexte` | Le pas de la fenêtre de contexte. | COMBO | Non | `STATIC_STANDARD`<br>`UNIFORM_STANDARD`<br>`UNIFORM_LOOPED`<br>`BATCHED` |
| `pas_contexte` | Le pas de la fenêtre de contexte ; applicable uniquement aux planifications uniformes (par défaut : 1). | INT | Non | 1+ |
| `boucle_fermée` | Indique s'il faut fermer la boucle de la fenêtre de contexte ; applicable uniquement aux planifications en boucle (par défaut : Faux). | BOOLEAN | Non | - |
| `méthode_fusion` | La méthode à utiliser pour fusionner les fenêtres de contexte (par défaut : PYRAMID). | COMBO | Non | `PYRAMID`<br>`LIST_STATIC` |
| `dimension` | La dimension à laquelle appliquer les fenêtres de contexte (par défaut : 0). | INT | Non | 0-5 |
| `bruit_libre` | Indique s'il faut appliquer le mélange de bruit FreeNoise, ce qui améliore le fondu entre les fenêtres (par défaut : Faux). | BOOLEAN | Non | - |
| `cond_retain_index_list` | Liste des indices latents à conserver dans les tenseurs de conditionnement pour chaque fenêtre. Par exemple, définir cette valeur sur '0' utilisera l'image de départ initiale pour chaque fenêtre (par défaut : ""). | STRING | Non | - |
| `split_conds_to_windows` | Indique s'il faut diviser les conditionnements multiples (créés par ConditionCombine) en chaque fenêtre en fonction de l'index de région (par défaut : Faux). | BOOLEAN | Non | - |
| `causal_window_fix` | Indique s'il faut ajouter une image de correction causale aux fenêtres de contexte dont l'index n'est pas 0 (par défaut : Vrai). | BOOLEAN | Non | - |

**Contraintes des paramètres :**

- `context_stride` est utilisé uniquement lorsque des planifications uniformes sont sélectionnées
- `closed_loop` est applicable uniquement aux planifications en boucle
- `dim` doit être compris entre 0 et 5 inclus
- `cond_retain_index_list` attend une liste d'indices entiers séparés par des virgules, sous forme de chaîne de caractères (par exemple, "0,1,2")

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `modèle` | Le modèle avec les fenêtres de contexte appliquées lors de l'échantillonnage. | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ContextWindowsManual/fr.md)

---
**Source fingerprint (SHA-256):** `b05ddda0ba38588305e6f733cd218c8b462268c39d16226ca961d09054187261`

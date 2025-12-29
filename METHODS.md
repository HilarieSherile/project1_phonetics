# Methods

This document describes the methodological and design considerations behind the IPA Converter project.  
The focus is on clarity, extensibility, and pedagogical usefulness rather than full-scale speech recognition or production-grade modeling.

---

## 1. Task Definition

The goal of the system is **grapheme-to-phoneme (G2P) conversion**:  
mapping written text (words) to their phonemic representations using the International Phonetic Alphabet (IPA).

- **Input unit**: character-level text (single words in the MVP)
- **Output unit**: phoneme-level representation (IPA)

At the current stage, the system operates at the **word level**, not sentence-level prosody or connected speech.

---

## 2. Transcription Type

The system uses **phonemic transcription** rather than narrow phonetic transcription.

**Rationale**:
- Phonemic IPA is more accessible to learners without formal linguistic training
- It provides sufficient detail for pronunciation learning
- It avoids overwhelming users with allophonic or articulatory detail

The goal is **pedagogical clarity**, not phonetic precision.

---

## 3. Representation Choice (IPA vs ARPAbet)

- **User-facing output**: IPA only
- **Internal representations**: may rely on ARPAbet or IPA-mapped dictionaries

ARPAbet is commonly used in computational resources (e.g., CMU Pronouncing Dictionary), but IPA is more widely recognized by language learners.  
For this reason, ARPAbet (if used) remains internal and is converted to IPA before display.

---

## 4. Data Sources and Lexical Coverage

For the MVP, the system relies on:
- A **manually defined pronunciation dictionary** (JSON-based)
- One-to-one word → IPA mappings

Future versions may incorporate:
- CMU Pronouncing Dictionary (English)
- Language-specific pronunciation lexicons for French and Mandarin
- Data filtering (e.g., lowercase normalization, punctuation removal)

Only **single-word entries** are considered at this stage.

---

## 5. Pronunciation Variants

The system returns **one pronunciation at a time**.

- Users select a target variety (e.g., American English, Canadian English, British English)
- This avoids cognitive overload and maintains consistency
- Multiple pronunciations are treated as configuration options rather than simultaneous outputs

---

## 6. Error Handling and Graceful Failure

When the system cannot find an IPA transcription:
- The original word is returned
- The word is visually highlighted (e.g., in red in future interfaces)
- No guessed or automatically generated transcription is shown

---

## 7. Model Considerations (Future Work)

At the MVP stage, the system does **not** use machine learning.

Potential future directions include:
- Character-to-phoneme sequence-to-sequence models
- Neural G2P architectures trained on pronunciation dictionaries
- Probabilistic handling of homographs and multiple pronunciations

These approaches are explicitly deferred to later stages to maintain interpretability and control.

---

## 8. Evaluation (Future)

If machine learning is introduced, evaluation metrics may include:
- **Phoneme Error Rate (PER)** using edit distance
- Word-level exact match accuracy

Evaluation is not performed in the current rule-based MVP.

---

## 9. Design Philosophy

This project prioritizes:
- Pedagogical clarity over linguistic exhaustiveness
- Transparency over automated guessing
- Incremental development over premature optimization

The system is designed as a learning tool first and a computational experiment second.

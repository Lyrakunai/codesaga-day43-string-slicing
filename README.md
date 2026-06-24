# ✂️ Day 43 - String Slicing

## 📚 Topics Covered

- String Slicing
- Substrings
- Start Include, End Exclude Rule
- Length Formula (end - start)
- Indexing vs Slicing
- Empty Slices
- Out-of-Range Slicing
- Full Slice
- Negative Slicing
- Positive + Negative Index Mixing

## 🧠 What I Learned

- Slicing is used to extract a continuous part of a string (substring).
- The start index is included.
- The end index is excluded.
- Number of returned characters can be checked using: `end - start`
- Indexing returns a single character.
- Slicing returns a string/substrings.
- Empty slices return an empty string, not an error.
- Out-of-range slicing does not cause an error.
- Negative indexing changes the position reference, not the direction.
- Positive and negative indexes can be used together in one slice.
- Full slicing (`[:]`) returns the complete string.

## ⚠️ Mistakes I Fixed

- Thought empty slices should produce errors.
- Thought out-of-range slices should produce errors.
- Confused indexing with slicing.
- Confused negative indexing with reverse direction.
- Thought negative indexing changes the reading direction.

## 🌍 Real-World Uses

- Username extraction
- Email domain extraction
- Employee ID extraction
- Website text previews
- Account number masking
- File extension extraction
  
## Status 
✅ Day 43 Complete

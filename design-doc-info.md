# NOTE: This document has nothing to do with this Github project. Just needed to host some markdown.

# CS 4ZP6 2020 - Design Doc Rubric
![Rubric](https://imgur.com/5HC1frU.png)
You will refine your SRS into something that better describes the software that you will (or ought to) implement. Of course, you should incorporate the lessons learned through implementing your prototype in here.  The deliverable will consist of the following information:

- **A list of anticipated changes (and its rationale)**
  - These are the things that might change in the future, either during your implementation, or in some potential future life for your project. Common items here are a) data representation, b) behaviour, c) hardware specifics, d) configuration, e) security requirements. There are, of course, many more categories, the above are just for illustration. The rationale should trace back to the SRS (hopefully with explicit links).
- **A list of unlikely changes (and rationale)**
  - These are the things that are basically imposed on you externally. They can be in all the same categories as the anticipated changes but, for one reason or another (that you should document), will not change. These are things that you can rely on. The rationale should trace back to the SRS (hopefully with explicit links).
- **A list of concepts pertaining to your problem domain, and whether these concepts are design-time entities or run-time entities.**
  - For example, if 'sorting' was an important item in your problem domain, then 'permutations' would be an important concept too; however, it is extremely unusual for permutations to exist in code, they are a design-time concept in most sorting algorithms. In the same domain, comparison functions are another concept, but needs to exist at run-time (when sorting proper names or addresses, the comparison functions involved are highly non-trivial if one is to respect usual conventions). There will be overlap between these and points 1-2 above.
- **A list of modules and the secret(s) that each module hides from the rest of the implementation.**
  - Your modules should be derived from the information in 1-3 above. Each module will own a certain idea, that it will keep secret from the rest of the implementation.
- **For each module, you will also give the interface that it offers (i.e. what services it gives). Be careful that your interface does not leak its secrets.**
- **A list of changes that you made to your SRS, because you learned of mistakes, or simply needed improvements, because of doing the above.**
- **A diagram of the "depends on" relation between your modules. A module A usually depends on module B when A does an explicit call to a method of B. Circular dependencies are usually a sign of a bad decomposition (but not always).**
- **For the modules that contain significant algorithms, or maintain non-trivial invariants, these should be documented too.**

Marks will be allocated for completeness, meaning that your design document adequately covers everything that was discussed in your SRS. This will also be tied to traceability: your explicitly linking of design points to particular parts of the SRS. In other words, it is up to you to provide explicit evidence of completeness, not up to us to do the work to verify it; we will be auditing your document, not verifying it.

There is no specific format for this document. However, some recommendations:

    This is best done using a Wiki, that can link directly to the SRS
    A lot of the information is best presented using various tabular formats
    You should be linking to the appropriate literature when documenting your concepts.
    Doing this assignment is time-consuming. It will take you more than 1 day per person per team.

Chapter 4 of the CS 2ME3 textbook is the perfect reference for all of this material. You cannot go wrong following it as a guide for doing this.

#  Installation instructions:

1. Create a new layer
2. Go to layer -> Custom scripts -> New
3. Copy and paste from [javelin-taipo](/javelin-taipo.javelin-script) into new script
4. Set up keys

    Go to each key and set the press and release scripts for each key

    0 for left, 1 for right

   ### Examples on how to make the press and release scripts

    press script for left inner button:
    ```cpp
    pressTaipoInner(0);
    ```

    release script for right R button:
    ```cpp
    releaseTaipoR(1);
    ```

    
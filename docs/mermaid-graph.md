graph TD
    N1((1. def karatsuba_multiplication))
    N2((2. if num1 < 10 or num2 < 10))
    N3((3. return traditional_multiplication))
    N4((4. convert to string, calc max_digits))
    N5((5. if max_digits % 2 != 0))
    N6((6. max_digits += 1))
    N7((7. zfill, split, recurse, combine))
    N8((8. end))
        
    N1 --> N2
    N2 -->|True| N3
    N2 -->|False| N4
    N3 --> N8
    N4 --> N5
    N5 -->|True| N6
    N5 -->|False| N7
    N6 --> N7
    N7 --> N8